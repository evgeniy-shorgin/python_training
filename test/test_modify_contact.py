from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="firstname_e"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="middlename_e"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
