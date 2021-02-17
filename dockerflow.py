from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker


@task(log_stdout=True)
def use_numpy():
    import numpy as np

    print(np.arange(10))


with Flow(
    "use_numpy",
    storage=Docker(python_dependencies=["numpy"]),
    run_config=DockerRun(),
) as flow:
    use_numpy()

flow.register(project_name="dockerflow")