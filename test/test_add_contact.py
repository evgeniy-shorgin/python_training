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


@pytest.mark.parametrize("a_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, a_contact):
    old_contacts = app.contact.get_contact_list()
    contact = app.contact.create(a_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # if contacts is the same new contact add to the end of equal contacts
    contact.ident = new_contacts[new_contacts.index(contact) + new_contacts.count(contact) - 1].ident
    old_contacts.append(contact)
    # new_contacts already sorted
    assert sorted(old_contacts) == sorted(new_contacts)
