from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(ident="272"))
    # l = db.get_contact_list()

    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()


# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
