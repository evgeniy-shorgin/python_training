# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="firstname_e", middlename="middlename_e", lastname="lastname_e",
                               nickname="nickname_e", title="title_e", company="company_e",
                               company_address="company_address_e", telephone_home="telephone_home_e",
                               telephone_mobile="telephone_mobile_e", telephone_work="telephone_work_e",
                               telephone_fax="telephone_fax_e", email="email_e", email2="email2_e",
                               email3="email3_e", homepage="homepage_e", birthday_year="birthday_year_e",
                               anniversary="anniversary_e", secondary_address="secondary_address_e",
                               secondary_phone_home="secondary_phone_home_e", secondary_notes="secondary_notes_e"))
    app.session.logout()