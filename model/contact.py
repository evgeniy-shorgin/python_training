class Contact:
    
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 company_address=None, telephone_home=None, telephone_mobile=None, telephone_work=None,
                 telephone_fax=None, email=None, email2=None, email3=None, homepage=None, birthday_year=None,
                 anniversary=None, secondary_address=None, secondary_phone_home=None, secondary_notes=None, ident=None):
        self.ident = ident
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.company_address = company_address
        self.telephone_home = telephone_home
        self.telephone_mobile = telephone_mobile
        self.telephone_work = telephone_work
        self.telephone_fax = telephone_fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_year = birthday_year
        self.anniversary = anniversary
        self.secondary_address = secondary_address
        self.secondary_phone_home = secondary_phone_home
        self.secondary_notes = secondary_notes

    def __eq__(self, other):
        return self.ident == other.ident and \
               self.firstname == other.firstname and \
               self.lastname == other.lastname and \
               self.company_address == other.company_address  # and \
               # self.middlename == other.middlename and \
               # self.nickname == other.nickname and \
               # self.title == other.title and \
               # self.company == other.company and \
               # self.telephone_home == other.telephone_home and \
               # self.telephone_mobile == other.telephone_mobile and \
               # self.telephone_work == other.telephone_work and \
               # self.telephone_fax == other.telephone_fax and \
               # self.email == other.email and \
               # self.email2 == other.email2 and \
               # self.email3 == other.email3 and \
               # self.homepage == other.homepage and \
               # self.birthday_year == other.birthday_year and \
               # self.anniversary == other.anniversary and \
               # self.secondary_address == other.secondary_address and \
               # self.secondary_phone_home == other.secondary_phone_home and \
               # self.secondary_notes == other.secondary_notes

    def __lt__(self, other):
        return self.ident < other.ident

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
        if self.telephone_home is not None: 
            repstr += "%s|" % self.telephone_home
        if self.telephone_mobile is not None: 
            repstr += "%s|" % self.telephone_mobile
        if self.telephone_work is not None: 
            repstr += "%s|" % self.telephone_work
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
        if self.secondary_phone_home is not None: 
            repstr += "%s|" % self.secondary_phone_home
        if self.secondary_notes is not None: 
            repstr += "%s|" % self.secondary_notes
        repstr = repstr[:-1]
        return repstr + "}"
