# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                    nickname="nickname", title="title", company="company",
                                    company_address="company_address", telephone_home="telephone_home",
                                    telephone_mobile="telephone_mobile", telephone_work="telephone_work",
                                    telephone_fax="telephone_fax", email="email", email2="email2",
                                    email3="email3", homepage="homepage", birthday_year="birthday_year",
                                    anniversary="anniversary", secondary_address="secondary_address",
                                    secondary_phone_home="secondary_phone_home", secondary_notes="secondary_notes"))
    app.session.logout()