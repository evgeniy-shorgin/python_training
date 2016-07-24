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
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="name", header="header", footer="footer"))
    app.session.logout()


def test_add_group_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()