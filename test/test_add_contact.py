from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                         nickname="nickname", title="title", company="company",
                                         company_address="company_address", homephone="homephone",
                                         mobilephone="mobilephone", workphone="workphone",
                                         telephone_fax="telephone_fax", email="email", email2="email2",
                                         email3="email3", homepage="homepage", birthday_year="birthday_year",
                                         anniversary="anniversary", secondary_address="secondary_address",
                                         secondaryphone="secondaryphone",
                                         secondary_notes="secondary_notes"))
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # if contacts is the same new contact add to the end of equal contacts
    # contact.ident = new_contacts[new_contacts.index(contact) + new_contacts.count(contact) - 1].ident
    old_contacts.append(contact)
    # new_contacts already sorted
    assert sorted(old_contacts) == new_contacts
