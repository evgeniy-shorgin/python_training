from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    print("\n")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    print("old_contacts %s" % old_contacts)
    index = randrange(len(old_contacts))
    contact = Contact(firstname="firstname_e", lastname="lastname_e", company_address="company_address_e")
    # contact.ident = old_contacts[index].ident
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # contact.ident = new_contacts[new_contacts.index(contact) + new_contacts.count(contact) - 1].ident
    old_contacts[index] = contact
    print("index %s" % index)
    print("old_contacts %s" % old_contacts)
    print("sor_old_cons %s" % sorted(old_contacts))
    print("new_contacts %s" % new_contacts)
    assert sorted(old_contacts) == new_contacts


# def test_modify_contact_middlename(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(middlename="test"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(middlename="middlename_e"))
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
