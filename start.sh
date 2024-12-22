#!/bin/bash

# Start FastAPI in the background on port 8089
uvicorn main:app --host 0.0.0.0 --port 8089 &

# Start Streamlit on port 8501
streamlit run app.py --server.port 8501 --server.address=0.0.0.0
