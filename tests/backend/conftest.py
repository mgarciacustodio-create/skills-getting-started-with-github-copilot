from copy import deepcopy
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from app import activities


@pytest.fixture(autouse=True)
def restore_activities():
    original_activities = deepcopy(activities)

    yield

    activities.clear()
    activities.update(original_activities)