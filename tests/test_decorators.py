import pytest

from src.decorators import log


@log()
def divide(a, b):
    return a / b


def test_log_success_console(capsys):
    result = divide(10, 2)
    captured = capsys.readouterr()
    assert result == 5
    assert captured.out == "divide ok\n"


def test_log_error_console(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0)" in captured.out


def test_log_success_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    result = add(2,3)
    assert result == 5
    assert log_file.read_text(encoding="utf-8") == "add ok\n"


def test_log_error_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def divide_file(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide_file(10, 0)
    content = log_file.read_text(encoding="utf-8")
    assert "divide_file error: ZeroDivisionError" in content
