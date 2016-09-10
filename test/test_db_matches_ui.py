from model.group import Group
from model.contact import Contact


def test_groups_in_db_matches_ui(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(ident=group.ident, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list) == sorted(db_list)


def test_contacts_in_db_matches_ui(app, db):
    ui_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       company_address=contact.company_address.strip(), ident=contact.ident.strip(),
                       all_emails_from_homepage=contact.all_emails_from_homepage.strip(),
                       all_phones_from_homepage=contact.all_phones_from_homepage.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list) == sorted(db_list)
