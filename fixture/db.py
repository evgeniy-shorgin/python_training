import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (ident, name, header, footer) = row
                list.append(Group(ident=str(ident), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, middlename, lastname, nickname, title, company, address, "
                           "home, mobile, work, fax, email, email2, email3, homepage, byear, ayear, address2, "
                           "phone2, notes FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (ident, firstname, middlename, lastname, nickname, title, company, company_address,
                 homephone, mobilephone, workphone, telephone_fax, email, email2, email3,
                 homepage, birthday_year, anniversary, secondary_address, secondaryphone,
                 secondary_notes) = row
                list.append(Contact(ident=str(ident), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, title=title, company=company, company_address=company_address,
                                    homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                                    telephone_fax=telephone_fax, email=email, email2=email2, email3=email3,
                                    homepage=homepage, birthday_year=birthday_year, anniversary=anniversary,
                                    secondary_address=secondary_address, secondaryphone=secondaryphone,
                                    secondary_notes=secondary_notes,
                                    all_emails_from_homepage=email + email2 + email3,
                                    all_phones_from_homepage=homephone + mobilephone + workphone + secondaryphone))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
