from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # wd.find_element_by_name("photo").click()
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.company_address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.telephone_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.change_field_value("byear", contact.birthday_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        self.change_field_value("ayear", contact.anniversary)
        self.change_field_value("address2", contact.secondary_address)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.secondary_notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit client creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contacts_cache = None
        return contact

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        # open modification form
        self.open_contact_to_modify_by_index(index)
        self.fill_contact_form(contact)
        # submit contact edit
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()
        self.contacts_cache = None

    def modify_contact_by_id(self, ident, contact):
        wd = self.app.wd
        # open modification form
        self.open_contact_to_modify_by_id(ident)
        self.fill_contact_form(contact)
        # submit contact edit
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()
        self.contacts_cache = None

    def open_contact_to_modify_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" % (index + 2)).click()

    def open_contact_to_modify_by_id(self, ident):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a[@href='edit.php?id=%s']/img" % ident).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[7]/a/img" % (index + 2)).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, ident):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % ident).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contacts_cache = None

    def delete_contact_by_id(self, ident):
        wd = self.app.wd
        self.select_contact_by_id(ident)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            # get list of contacts, include header of table
            for element in wd.find_elements_by_css_selector("tr"):
                # if it is a contact, not header of table
                if element.get_attribute("name") == "entry":
                    attributes = element.find_elements_by_css_selector("td")
                    ident = attributes[0].find_element_by_name("selected[]").get_attribute("value")
                    lastname = attributes[1].text
                    firstname = attributes[2].text
                    company_address = attributes[3].text
                    all_emails = attributes[4].text
                    all_phones = attributes[5].text
                    self.contacts_cache.append(Contact(firstname=firstname, lastname=lastname,
                                                       company_address=company_address, ident=ident,
                                                       all_emails_from_homepage=all_emails,
                                                       all_phones_from_homepage=all_phones))
        self.app.open_home_page()
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_modify_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        company_address = wd.find_element_by_name("address").get_attribute("value")
        ident = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, company_address=company_address, ident=ident,
                       email=email, email2=email2, email3=email3,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)
