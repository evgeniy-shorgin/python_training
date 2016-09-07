

def test_add_contact(app, json_contacts):
    a_contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    contact = app.contact.create(a_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # if contacts is the same new contact add to the end of equal contacts
    contact.ident = new_contacts[new_contacts.index(contact) + new_contacts.count(contact) - 1].ident
    old_contacts.append(contact)
    # new_contacts already sorted
    assert sorted(old_contacts) == sorted(new_contacts)
