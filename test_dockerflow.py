from dockerflow import use_numpy
from prefect import Flow
import numpy as np
import pytest


@pytest.fixture
def task_state():
    with Flow(name="test_return") as flow:
        nptask = use_numpy()  # must be in flow context
        flow.tasks = [nptask]
        state = flow.run()

    return nptask, state


def test_flow_state(task_state):
    _, state = task_state
    assert state.is_successful()


def test_return(task_state):
    task, state = task_state
    assert (state.result[task].result == np.arange(10)).all
