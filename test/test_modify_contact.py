from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="firstname_e")
    contact.ident = old_contacts[index].ident
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    print(sorted(old_contacts))
    print(sorted(new_contacts))
    assert sorted(old_contacts) == sorted(new_contacts)
    contact1 = Contact(firstname="firstname_e")
    contact2 = Contact(firstname="firstname_e")
    if contact1 == contact2:
        print("ok")


# def test_modify_contact_middlename(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(middlename="test"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(middlename="middlename_e"))
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
