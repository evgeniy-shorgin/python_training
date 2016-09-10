from model.contact import Contact
import random


def test_modify_some_contact(app, db, json_contacts):
    contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact_to_modify = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact_to_modify.ident, contact)
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact_to_modify)] = contact
    assert old_contacts == new_contacts
