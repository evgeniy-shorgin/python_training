from model.contact import Contact
import random


def test_modify_some_contact(app, data_contacts):
    contact = data_contacts
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact.ident = old_contacts[index].ident
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts) == sorted(new_contacts)
