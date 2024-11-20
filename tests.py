import pytest
import io
from src import *

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

def test_username_with_user_input_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(' '))
    assert get_user_name_from_input() is None

def test_username_with_user_input_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('YU TING'))
    assert get_user_name_from_input() is None

def test_username_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('YUTING'))
    assert get_user_name_from_input() == 'YUTING'

def test_password_with_user_input_short(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('short'))
    assert get_password_from_input() is None

def test_password_with_user_input_missing_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('password!'))
    assert get_password_from_input() is None

def test_password_with_user_input_missing_special_char(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('password123'))
    assert get_password_from_input() is None

def test_password_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Password123!'))
    assert get_password_from_input() == 'Password123!'
