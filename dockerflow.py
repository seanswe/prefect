from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker
from prefect.tasks.secrets import PrefectSecret


@task(log_stdout=True
def use_numpy(access_key, secret_key):
    import numpy as np

    print(np.arange(10))


with Flow("use_numpy") as flow:
    flow.storage = Docker(python_dependencies=["numpy"])
    flow.run_config = DockerRun()

    access_key = PrefectSecret("AWS_ACCESS_KEY_ID")
    secret_key = PrefectSecret("AWS_SECRET_ACCESS_KEY"),

    use_numpy(access_key, secret_key)

flow.register(project_name="dockerflow")