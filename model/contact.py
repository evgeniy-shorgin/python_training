from sys import maxsize


class Contact:
    
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 company_address=None, homephone=None, mobilephone=None, workphone=None,
                 telephone_fax=None, email=None, email2=None, email3=None, homepage=None, birthday_year=None,
                 anniversary=None, secondary_address=None, secondaryphone=None, secondary_notes=None, ident=None):
        self.ident = ident
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.company_address = company_address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.telephone_fax = telephone_fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_year = birthday_year
        self.anniversary = anniversary
        self.secondary_address = secondary_address
        self.secondaryphone = secondaryphone
        self.secondary_notes = secondary_notes

    def __eq__(self, other):
        return (self.ident is None or other.ident is None or self.ident == other.ident) and \
               self.firstname == other.firstname and \
               self.lastname == other.lastname and \
               self.company_address == other.company_address  # and \
               # self.middlename == other.middlename and \
               # self.nickname == other.nickname and \
               # self.title == other.title and \
               # self.company == other.company and \
               # self.homephone == other.homephone and \
               # self.mobilephone == other.mobilephone and \
               # self.workphone == other.workphone and \
               # self.telephone_fax == other.telephone_fax and \
               # self.email == other.email and \
               # self.email2 == other.email2 and \
               # self.email3 == other.email3 and \
               # self.homepage == other.homepage and \
               # self.birthday_year == other.birthday_year and \
               # self.anniversary == other.anniversary and \
               # self.secondary_address == other.secondary_address and \
               # self.secondaryphone == other.secondaryphone and \
               # self.secondary_notes == other.secondary_notes

    def __lt__(self, other):
        return self.firstname < other.firstname

    def __repr__(self):
        repstr = "{"
        if self.ident is not None: 
            repstr += "%s|" % self.ident
        if self.firstname is not None: 
            repstr += "%s|" % self.firstname
        if self.middlename is not None: 
            repstr += "%s|" % self.middlename
        if self.lastname is not None: 
            repstr += "%s|" % self.lastname
        if self.nickname is not None: 
            repstr += "%s|" % self.nickname
        if self.title is not None: 
            repstr += "%s|" % self.title
        if self.company is not None: 
            repstr += "%s|" % self.company
        if self.company_address is not None: 
            repstr += "%s|" % self.company_address
        if self.homephone is not None:
            repstr += "%s|" % self.homephone
        if self.mobilephone is not None:
            repstr += "%s|" % self.mobilephone
        if self.workphone is not None:
            repstr += "%s|" % self.workphone
        if self.telephone_fax is not None: 
            repstr += "%s|" % self.telephone_fax
        if self.email is not None: 
            repstr += "%s|" % self.email
        if self.email2 is not None: 
            repstr += "%s|" % self.email2
        if self.email3 is not None: 
            repstr += "%s|" % self.email3
        if self.homepage is not None: 
            repstr += "%s|" % self.homepage
        if self.birthday_year is not None: 
            repstr += "%s|" % self.birthday_year
        if self.anniversary is not None: 
            repstr += "%s|" % self.anniversary
        if self.secondary_address is not None: 
            repstr += "%s|" % self.secondary_address
        if self.secondaryphone is not None:
            repstr += "%s|" % self.secondaryphone
        if self.secondary_notes is not None: 
            repstr += "%s|" % self.secondary_notes
        repstr = repstr[:-1]
        return repstr + "}"

    def id_or_max(self):
        if self.ident:
            return int(self.ident)
        else:
            return maxsize
