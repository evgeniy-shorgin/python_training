from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", company_address="",
                    homephone="", mobilephone="", workphone="", telephone_fax="", email="", email2="", email3="",
                    homepage="", birthday_year="", anniversary="", secondary_address="", secondaryphone="",
                    secondary_notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            company_address=random_string("company_address", 10), homephone=random_string("homephone", 10),
            mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
            telephone_fax=random_string("telephone_fax", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            homepage=random_string("homepage", 10), birthday_year=random_string("birthday_year", 10),
            anniversary=random_string("anniversary", 10), secondary_address=random_string("secondary_address", 10),
            secondaryphone=random_string("secondaryphone", 10), secondary_notes=random_string("secondary_notes", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_modify_some_contact(app, contact):
    print("\n")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    print("index = %s" % index)
    contact.ident = old_contacts[index].ident
    print("old_contacts = %s" % old_contacts)
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    print("old_contacts = %s" % old_contacts)
    print("new_contacts = %s" % new_contacts)
    print("sorted(old_contacts) = %s" % sorted(old_contacts))
    print("sorted(new_contacts) = %s" % sorted(new_contacts))
    assert sorted(old_contacts) == sorted(new_contacts)
