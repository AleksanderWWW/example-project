from tutorial.tutorial_runner import (
    Runner,
    Tutorial,
)


def test_tutorial_run_returns_correct_status_code():
    tut = Tutorial(id="1", name="example")
    code = tut.run()
    assert code == 0


def test_runner_returns_correct_status_code():
    tut = Tutorial(id="3", name="example_tutorial")

    runner = Runner(id="1", name="example_runner")

    code = runner.run_tutorial(tut)
    assert code == 0
