from io import StringIO
import sys

from lista02 import decimal2binario, exe02, exe03, exe04, exe05


def test_exe01():
    assert decimal2binario(10) == "1010"


def test_exe01b():
    assert decimal2binario(0) == "0"


def test_exe02(monkeypatch):
    inputs = StringIO("2 5 +")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "7"


def test_exe02b(monkeypatch):
    inputs = StringIO("1 2 + 3 4 + *")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "21"


def test_exe02c(monkeypatch):
    inputs = StringIO("1 2 + 3 4 + * 1 2 + 3 4 + * +")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "42"


def test_exe02d(monkeypatch):
    inputs = StringIO("1 2 + 3 4 + * 1 2 + 3 4 + * + 1 2 + 3 4 + * 1 2 + 3 4 + * + +")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "84"


def test_exe02d(monkeypatch):
    inputs = StringIO(
        "1 2 + 3 4 + * 1 2 + 3 4 + * + 1 2 + 3 4 + * 1 2 + 3 4 + * + + 4 +"
    )
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "88"


def test_exe02e(monkeypatch):
    inputs = StringIO("2 3 * 4 +")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "10"


def test_exe02f(monkeypatch):
    inputs = StringIO("1 2 3 4 5 * + * +")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "47"


def test_exe03(monkeypatch):
    inputs = StringIO("()")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe03()
    assert result.getvalue().strip() == "True"


def test_exe03b(monkeypatch):
    inputs = StringIO("(()")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe03()
    assert result.getvalue().strip() == "False"


def test_exe03c(monkeypatch):
    inputs = StringIO("())")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe03()
    assert result.getvalue().strip() == "False"


def test_exe03d(monkeypatch):
    inputs = StringIO("((")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe03()
    assert result.getvalue().strip() == "False"


def test_exe03d(monkeypatch):
    inputs = StringIO(")")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe03()
    assert result.getvalue().strip() == "False"


def test_exe04(monkeypatch):
    inputs = StringIO("10")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe04()
    assert result.getvalue().strip() == "55"


def test_exe05(monkeypatch):
    inputs = StringIO("([{}])")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe05()
    assert result.getvalue().strip() == "True"


def test_exe05b(monkeypatch):
    inputs = StringIO("(]")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe05()
    assert result.getvalue().strip() == "False"


def test_exe05c(monkeypatch):
    inputs = StringIO("]")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe05()
    assert result.getvalue().strip() == "False"


def test_exe05c(monkeypatch):
    inputs = StringIO("]]")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe05()
    assert result.getvalue().strip() == "False"
