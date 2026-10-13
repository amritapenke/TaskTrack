from tasktrack import remove_task_by_number


def test_remove_first_task():
    # Arrange
    tasks = ["Study", "Exercise", "Read"]

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task == "Study"
    assert tasks == ["Exercise", "Read"]


def test_remove_middle_task():
    tasks = ["Study", "Exercise", "Read"]

    removed_task = remove_task_by_number(tasks, 2)

    assert removed_task == "Exercise"
    assert tasks == ["Study", "Read"]


def test_remove_last_task():
    tasks = ["Study", "Exercise", "Read"]

    removed_task = remove_task_by_number(tasks, 3)

    assert removed_task == "Read"
    assert tasks == ["Study", "Exercise"]


def test_reject_zero():
    tasks = ["Study", "Exercise", "Read"]

    removed_task = remove_task_by_number(tasks, 0)

    assert removed_task is None
    assert tasks == ["Study", "Exercise", "Read"]


def test_reject_number_above_list_length():
    tasks = ["Study", "Exercise", "Read"]

    removed_task = remove_task_by_number(tasks, 4)

    assert removed_task is None
    assert tasks == ["Study", "Exercise", "Read"]
def test_remove_from_empty_list():
    tasks = []
    removed_task = remove_task_by_number(tasks, 1)
    assert removed_task is None
    assert tasks == []