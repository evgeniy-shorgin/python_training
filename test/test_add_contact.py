

def test_add_contact(app, db, json_contacts, check_ui):
    a_contact = json_contacts
    old_contacts = db.get_contact_list()
    contact = app.contact.create(a_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)
    if check_ui:
        assert sorted(new_contacts) == sorted(app.contact.get_contact_list())
