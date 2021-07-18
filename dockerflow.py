from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker
import numpy as np


@task(log_stdout=True)
def use_numpy():

    return np.arange(10)


with Flow("use_numpy") as flow:
    flow.storage = Docker(python_dependencies=["numpy"])
    flow.run_config = DockerRun()
    nptask = use_numpy()

# flow.register(project_name="dockerflow")
