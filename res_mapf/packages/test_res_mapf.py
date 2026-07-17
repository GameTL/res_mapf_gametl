""" USAGE
cd res_mapf
uv run pytest packages/test_res_mapf.py -v -s   # verbose names + show prints
"""
import importlib 
import pytest 
from rich.pretty import pprint

# ========================================== 1. Import ===========================================

PACKAGES = [
    "res_mapf",
    "res_mapf_planning",
    "res_plan_execution",
    "res_plan_server",
    "res_pybullet",
    # "btich",
]

@pytest.mark.parametrize("name", PACKAGES)
def test_can_import(name: str) -> None:
    importlib.import_module(name)


# ========================================== 2. Plan server ======================================
from res_plan_server.task_status import TaskStatus

def test_task_status_planning_exist() -> None:
    assert TaskStatus.PLANNING is TaskStatus["PLANNING"]
    assert TaskStatus.PLANNING.value == 1 