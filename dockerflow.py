import prefect
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker

storage = Docker(python_dependencies=["numpy"])


@task(log_stdout=True)
def use_numpy():
    import numpy as np

    print(np.arange(10))


with Flow("dockerflow") as flow:
    use_numpy()

flow.run_config = DockerRun()

flow.register(project_name="dockerflow")