import pytest

from tasktrack import load_tasks, remove_task_by_number, save_tasks


@pytest.fixture
def sample_tasks():
    return ["Study", "Exercise", "Shop"]


def test_remove_first_task(sample_tasks):
    # Arrange
    task_number = 1
    expected_removed = "Study"

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result == expected_removed
    assert sample_tasks == ["Exercise", "Shop"]


def test_remove_middle_task(sample_tasks):
    # Arrange
    task_number = 2
    expected_removed = "Exercise"

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result == expected_removed
    assert sample_tasks == ["Study", "Shop"]


def test_remove_last_task(sample_tasks):
    # Arrange
    task_number = 3
    expected_removed = "Shop"

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result == expected_removed
    assert sample_tasks == ["Study", "Exercise"]


@pytest.mark.parametrize(
    "task_number",
    [0, -1, 10],
    ids=["zero", "negative_number", "number_too_large"],
)
def test_invalid_task_numbers_return_none(task_number, sample_tasks):
    # Arrange
    original_tasks = sample_tasks.copy()

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result is None
    assert sample_tasks == original_tasks


def test_save_tasks_writes_all_tasks(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    tasks = ["Study", "Exercise", "Shop"]
    expected_text = "Study\nExercise\nShop\n"

    # Act
    save_tasks(tasks, test_file)

    # Assert
    assert test_file.read_text(encoding="utf-8") == expected_text


def test_load_tasks_reads_all_tasks(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    test_file.write_text("Study\nExercise\nShop\n", encoding="utf-8")
    expected_tasks = ["Study", "Exercise", "Shop"]

    # Act
    result = load_tasks(test_file)

    # Assert
    assert result == expected_tasks


def test_load_tasks_ignores_blank_lines(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    test_file.write_text("Study\n\nExercise\n  \nShop\n", encoding="utf-8")
    expected_tasks = ["Study", "Exercise", "Shop"]

    # Act
    result = load_tasks(test_file)

    # Assert
    assert result == expected_tasks


def test_load_tasks_returns_empty_list_for_missing_file(tmp_path):
    # Arrange
    test_file = tmp_path / "missing_tasks.txt"

    # Act
    result = load_tasks(test_file)

    # Assert
    assert result == []


def test_save_and_load_tasks_round_trip(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    original_tasks = ["Study", "Exercise", "Shop"]

    # Act
    save_tasks(original_tasks, test_file)
    loaded_tasks = load_tasks(test_file)

    # Assert
    assert loaded_tasks == original_tasks
