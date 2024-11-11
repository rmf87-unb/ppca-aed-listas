from io import StringIO
import sys

from lista01 import exe01, exe02, exe03, exe04, exe05


def test_exe01(monkeypatch):
    input = "Olá, Mundo"
    result = StringIO()
    monkeypatch.setattr("builtins.input", lambda: input)
    monkeypatch.setattr(sys, "stdout", result)
    exe01()
    assert result.getvalue() == "Olá, Mundo\n"


def test_ex02(monkeypatch):
    inputs = StringIO("4\n4")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe02()
    assert result.getvalue().strip() == "4.00"


def test_ex03(monkeypatch):
    inputs = StringIO("4\n4\n4\n4\n4")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe03()
    assert result.getvalue().strip() == "4.000"


def test_ex04(monkeypatch):
    inputs = StringIO("1.0 7.0\n5.0 9.0\n2j")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe04()
    assert result.getvalue().strip() == "4.4721\n2.0000"


def test_ex04b(monkeypatch):
    inputs = StringIO("-2.5 0.4\n12.1 7.3\n1+2j")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe04()
    assert result.getvalue().strip() == "16.1484\n2.2361"


def test_ex05(monkeypatch):
    inputs = StringIO("4\n-2 5\n3 3\n-10 3\n4 4")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe05()
    assert result.getvalue().strip() == "15\n15\n-21\n32\n32\n-21\n5.50"


def test_ex05b(monkeypatch):
    inputs = StringIO("3\n-5 1\n-3 2\n-10 3\n4 4")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe05()
    assert result.getvalue().strip() == "-5\n-4\n-21\n-4\n-21\n-12.50"


def test_ex05c(monkeypatch):
    inputs = StringIO("2\n-5 2\n-5 4")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe05()
    assert result.getvalue().strip() == "-8\n-8\n-8\n-8\n-8.00"
