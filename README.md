# requesta_evaluation
a web application built to collect data for ReQUESTA evaluation 

```bash

python -m venv .venv && source .venv/scripts/activate

# terminal 
# run the backend
cd backend
pip install -r requirements.txt

# run the app from repo root
cd ../ # to make sure you are running the app from the repo root if you were in "backend" directory
uvicorn backend.main:app --reload --env-file .env


```