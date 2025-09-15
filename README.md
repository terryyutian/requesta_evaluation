# requesta_evaluation
a web application built to collect data for ReQUESTA evaluation 

```bash

python -m venv .venv && source .venv/scripts/activate

# terminal 1
# run the backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# terminal 2 (static hosting for convenience)
cd frontend
python -m http.server 5500

# Then open http://localhost:5500/consent.html
# If your backend runs on a different address, set window.API_BASE_OVERRIDE in any HTML:
# <script>window.API_BASE_OVERRIDE = "http://127.0.0.1:8000";</script>


```