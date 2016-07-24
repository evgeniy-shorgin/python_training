# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group_filled(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="name", header="header", footer="footer"))
    app.logout()


def test_add_group_empty(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()