from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                               nickname="nickname", title="title", company="company",
                               company_address="company_address", telephone_home="telephone_home",
                               telephone_mobile="telephone_mobile", telephone_work="telephone_work",
                               telephone_fax="telephone_fax", email="email", email2="email2",
                               email3="email3", homepage="homepage", birthday_year="birthday_year",
                               anniversary="anniversary", secondary_address="secondary_address",
                               secondary_phone_home="secondary_phone_home", secondary_notes="secondary_notes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
