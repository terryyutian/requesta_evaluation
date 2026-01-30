# backend/database.py
from __future__ import annotations

import os
from functools import lru_cache
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.models import Base

try:
    import boto3  # type: ignore
except Exception:
    boto3 = None


@lru_cache()
def _get_ssm_param(name: str, decrypt: bool = True) -> Optional[str]:
    """Fetch a secure parameter from AWS Systems Manager Parameter Store."""
    if boto3 is None:
        return None
    region = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION") or "us-west-2"
    try:
        ssm = boto3.client("ssm", region_name=region)
        return ssm.get_parameter(Name=name, WithDecryption=decrypt)["Parameter"]["Value"]
    except Exception:
        return None


def _get(env_key: str, default: Optional[str] = None, ssm_path: Optional[str] = None, secure: bool = False) -> Optional[str]:
    """Resolve a config value from ENV > SSM > default."""
    val = os.getenv(env_key)
    if val:
        return val
    if ssm_path:
        val = _get_ssm_param(ssm_path, decrypt=secure)
        if val:
            return val
    return default


def build_aurora_database_url() -> str:
    """
    Build the Aurora/MySQL database URL.

    Priority:
    1. DATABASE_URL (ENV or /requesta/DATABASE_URL in SSM)
    2. Individual components (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    """
    # First: try DATABASE_URL (env or SSM)
    url = os.getenv("DATABASE_URL") or _get_ssm_param("/requesta/DATABASE_URL", decrypt=True)
    if url:
        return url

    # Fallback: build from individual pieces
    user = _get("DB_USER", ssm_path="/requesta/DB_USER")
    password = _get("DB_PASSWORD", ssm_path="/requesta/DB_PASSWORD", secure=True)
    host = _get("DB_HOST", ssm_path="/requesta/DB_HOST")
    port = _get("DB_PORT", default="3306", ssm_path="/requesta/DB_PORT")
    name = _get("DB_NAME", ssm_path="/requesta/DB_NAME")

    if not all([user, password, host, name]):
        raise RuntimeError(
            "Aurora MySQL config missing. Provide DATABASE_URL or DB_USER/DB_PASSWORD/DB_HOST/DB_NAME."
        )

    driver = os.getenv("MYSQL_DRIVER", "pymysql") 
    return f"mysql+{driver}://{user}:{password}@{host}:{port}/{name}"


# Create engine + sessionmaker for Aurora usage
AURORA_DB_URL = build_aurora_database_url()
engine = create_engine(AURORA_DB_URL, pool_pre_ping=True, pool_recycle=300)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """Create tables if they do not exist."""
    Base.metadata.create_all(bind=engine)
