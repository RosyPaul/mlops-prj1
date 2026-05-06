import dagshub
import mlflow

mlflow.set_tracking_uri('https://dagshub.com/RosyPaul/mlops-prj1.mlflow')
dagshub.init(repo_owner='RosyPaul', repo_name='mlops-prj1', mlflow=True)


import mlflow
with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)