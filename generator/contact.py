from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            homepage=random_string("homepage", 10), birthday_year=random_string("", 4),
            anniversary=random_string("", 4), secondary_address=random_string("secondary_address", 10),
            secondaryphone=random_string("secondaryphone", 10), secondary_notes=random_string("secondary_notes", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
