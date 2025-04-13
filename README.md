# End-to-End-Chest-Cancer-Classification




## For Dagshub 

import dagshub
dagshub.init(repo_owner='AshishSMehra', repo_name='End-to-End-Chest-Cancer-Classification', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)



