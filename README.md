# End-to-End-Chest-Cancer-Classification




## For Dagshub 

import dagshub
dagshub.init(repo_owner='AshishSMehra', repo_name='End-to-End-Chest-Cancer-Classification', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)



## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml