from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                         nickname="nickname", title="title", company="company",
                                         company_address="company_address", telephone_home="telephone_home",
                                         telephone_mobile="telephone_mobile", telephone_work="telephone_work",
                                         telephone_fax="telephone_fax", email="email", email2="email2",
                                         email3="email3", homepage="homepage", birthday_year="birthday_year",
                                         anniversary="anniversary", secondary_address="secondary_address",
                                         secondary_phone_home="secondary_phone_home",
                                         secondary_notes="secondary_notes"))
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # we don't now id, it is in alphabet order
    # contact.ident = new_contacts[len(new_contacts)-1].ident
    # old_contacts.append(contact)
    # assert sorted(old_contacts) == sorted(new_contacts)
