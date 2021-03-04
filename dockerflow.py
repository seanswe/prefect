from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker


@task(log_stdout=True)
def use_numpy():
    import numpy as np

    print(np.arange(10))


awsid = Secret("AWS_ACCESS_KEY_ID").get()
awskey = Secret("AWS_SECRET_ACCESS_KEY").get()

with Flow("use_numpy") as flow:
    flow.storage = Docker(python_dependencies=["numpy"])
    flow.run_config = DockerRun(
        env={"AWS_ACCESS_KEY_ID": awsid, "AWS_SECRET_ACCESS_KEY": awskey}
    )
    use_numpy()

flow.register(project_name="dockerflow")