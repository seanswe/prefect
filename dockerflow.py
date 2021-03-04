from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker
from prefect.tasks.secrets import PrefectSecret


@task(log_stdout=True)
def use_numpy():
    import numpy as np

    print(np.arange(10))


with Flow("use_numpy") as flow:
    flow.storage = Docker(python_dependencies=["numpy"])
    flow.run_config = DockerRun(
        env={
            "AWS_ACCESS_KEY_ID": PrefectSecret("AWS_ACCESS_KEY_ID").get(),
            "AWS_SECRET_ACCESS_KEY": PrefectSecret("AWS_SECRET_ACCESS_KEY").get(),
        }
    )
    use_numpy()

flow.register(project_name="dockerflow")