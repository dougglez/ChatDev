import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

from chatdev.roster import Roster


def test_exist_employee_case_insensitive():
    r = Roster()
    r._recruit("Alice")
    assert r._exist_employee("alice") is True


def test_exist_employee_ignore_spaces_and_underscores():
    r = Roster()
    r._recruit("Alice_Smith")
    assert r._exist_employee("Alice Smith") is True


def test_exist_employee_new_name():
    r = Roster()
    r._recruit("Alice")
    assert r._exist_employee("Bob") is False


def test_exist_employee_spaces_in_record():
    r = Roster()
    r._recruit("Alice Smith")
    assert r._exist_employee("Alice_Smith") is True
