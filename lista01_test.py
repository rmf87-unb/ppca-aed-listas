from io import StringIO
import sys

from lista01 import (
    exe01,
    exe02,
    exe03,
    exe04,
    exe05,
    exe06,
    exe07,
    exe08,
    exe09,
    exe10,
    exe11,
    exe12,
    exe13,
)


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


def test_ex06(monkeypatch):
    inputs = StringIO("2")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe06()
    assert result.getvalue().strip() == "1\n2"


def test_exe06b(monkeypatch):
    inputs = StringIO("3")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe06()
    assert result.getvalue().strip() == "1\n3"


def test_exe06c(monkeypatch):
    inputs = StringIO("4")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe06()
    assert result.getvalue().strip() == "1\n2\n4"


def test_exe07(monkeypatch):
    inputs = StringIO("4\n5")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe07()
    assert result.getvalue().strip() == "x e menor que y"


def test_exe07b(monkeypatch):
    inputs = StringIO("3\n3")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe07()
    assert result.getvalue().strip() == "x e igual a y"


def test_exe07c(monkeypatch):
    inputs = StringIO("-1\n-2")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe07()
    assert result.getvalue().strip() == "x e maior que y"


def test_exe08(monkeypatch):
    inputs = StringIO("3\n1\n2\n3\n4\n5\n6\n7\n8\n9")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe08()
    assert result.getvalue().strip() == "9\n3"


def test_exe08b(monkeypatch):
    inputs = StringIO("-1\n-5\n-4\n10\n8\n0\n4\n3\n2\n1")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe08()
    assert result.getvalue().strip() == "10\n-1"


def test_exe08c(monkeypatch):
    inputs = StringIO("-2\n-4\n-8\n-16\n-32\n-64\n-128\n-256\n-512\n-2")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe08()
    assert result.getvalue().strip() == "-2\n-2"


def test_exec09(monkeypatch):
    inputs = StringIO("\nb")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe09()
    assert result.getvalue().strip() == "b\n\nTrue"


def test_exec09b(monkeypatch):
    inputs = StringIO("aaa\nbbb")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe09()
    assert result.getvalue().strip() == "aaabbb\naaa\nFalse"


def test_exec09c(monkeypatch):
    inputs = StringIO("cd\ncdd")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe09()
    assert result.getvalue().strip() == "cdcdd\ndc\nTrue"


def test_exec10(monkeypatch):
    inputs = StringIO("6")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe10()
    assert result.getvalue().strip() == "8 720 5"


def test_exec10b(monkeypatch):
    inputs = StringIO("1")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe10()
    assert result.getvalue().strip() == "1 1"


def test_exec10b(monkeypatch):
    inputs = StringIO("10")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe10()
    assert result.getvalue().strip() == "55 3628800"


def test_exec11(monkeypatch):
    inputs = StringIO("8 12")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe11()
    assert result.getvalue().strip() == "4"


def test_exec11b(monkeypatch):
    inputs = StringIO("9 27")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe11()
    assert result.getvalue().strip() == "9"


def test_exec11c(monkeypatch):
    inputs = StringIO("259 111")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe11()
    assert result.getvalue().strip() == "37"


def test_exec12(monkeypatch):
    inputs = StringIO("2 3")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe12()
    assert result.getvalue().strip() == "2 3 ok"


def test_exec12b(monkeypatch):
    inputs = StringIO("3 1")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe12()
    assert result.getvalue().strip() == "3 1 errados"


def test_exec12c(monkeypatch):
    inputs = StringIO("5 5")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe12()
    assert result.getvalue().strip() == "5 5 ok"


def test_exec12d(monkeypatch):
    inputs = StringIO("5 4")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe12()
    assert result.getvalue().strip() == "5 4 errados"


def test_exec12e(monkeypatch):
    inputs = StringIO("0 0")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe12()
    assert result.getvalue().strip() == "0 0 errados"


def test_exec13(monkeypatch):
    inputs = StringIO("7\n5\n8 \n7")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe13()
    assert (
        result.getvalue().strip()
        == "O número correto é maior.\nO número correto é menor.\nParabéns! Você acertou."
    )


def test_exec13b(monkeypatch):
    inputs = StringIO("-2\n-1\n-3\n-2")
    result = StringIO()
    monkeypatch.setattr(sys, "stdin", inputs)
    monkeypatch.setattr(sys, "stdout", result)
    exe13()
    assert (
        result.getvalue().strip()
        == "O número correto é menor.\nO número correto é maior.\nParabéns! Você acertou."
    )
