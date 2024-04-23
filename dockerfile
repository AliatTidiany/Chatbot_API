# official python
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


WORKDIR /app

COPY . /app
#COPY model_pipeline.joblib .
#COPY reponses.joblib .
# Install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 4020

# environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "4020"]
