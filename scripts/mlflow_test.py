import mlflow
import random

# setting up tracking uri
mlflow.set_tracking_uri("http://127.0.0.1:5000/")

with mlflow.start_run():

    # log random parameters
    mlflow.log_param("parameter-1", random.randint(1, 100))
    mlflow.log_param("parameter-2",random.random())

    # log random metrics
    mlflow.log_metric("random-metric-1", random.random())
    mlflow.log_metric("random-metric-2", random.uniform(0.5, 2.5))
