"""
Создаём класс-помощник ContactHelper по работе с контактами
"""

from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_page_to_add_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def data_form_completion(self, contact_obj):
        wd = self.app.wd
        # Заполняем/модифицируем форму данных для создаваемого контакта
        self.change_field_value("firstname", contact_obj.first_name)
        self.change_field_value("lastname", contact_obj.last_name)
        self.change_field_value("address", contact_obj.address)
        self.change_field_value("mobile", contact_obj.mobile_phone)
        self.change_field_value("email", contact_obj.email)
        # Указываем дату рождения при заполнении формы
        self.change_field_value_date("bday", contact_obj.day, "//option[@value={!r}]")
        self.change_field_value_date("bmonth", contact_obj.month, "//option[@value={!r}]")
        self.change_field_value("byear", contact_obj.year)

    def change_field_value_date(self, field_name, text, xpath):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath(xpath.format(text)).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact_obj):
        contact_obj = contact_obj
        wd = self.app.wd
        self.open_home_page()
        self.open_page_to_add_contact()
        # Заполняем форму данных для создаваемого контакта
        self.data_form_completion(contact_obj)
        # Подтверждаем создание контакта
        wd.find_element_by_xpath("//input[20]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, contact_obj):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # Вносим изменения в форму данных для выбранного контакта
        self.data_form_completion(contact_obj)
        # Подтверждаем изменение контакта
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

