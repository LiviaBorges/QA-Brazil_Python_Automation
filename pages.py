from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    # Definir o endereço
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Selecionar o plano Comfort
    taxi_option_locator = (By.XPATH, '//button[contains(text(), "Chamar")]')
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    # Preencher o numero de telefone
    add_phone_number = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(), "Confirmar")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    # Adicionar um cartao de credito
    add_forma_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    add_finish_card = (By.XPATH, '//button[contains(text(), "Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, 'payment-picker.open, .close-button')
    confirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    # Adicionar comentario para o motorista
    add_comment = (By.ID, 'comment')

    # Pedir um cobertor e lenços
    switch_blanket = (By.CSS_SELECTOR, 'switch')
    switch_blanket_active = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open >')

    # Pedir 2 sorvetes
    add_ice_cream = (By.CSS_SELECTOR, '.counter-plus')
    number_of_ice_creams = (By.CSS_SELECTOR, '.counter-value')

    # Pedir um taxi com a tarifa Comfort
    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-header-title')

    def __init__ (self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.from_field)
        )
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.to_field)
        )
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self. from_field)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self. to_field)
        ).get_attribute('value')

    def click_taxi(self):
        self.driver.find_element(*self.taxi_option_locator).click()

    def click_comfort_icon(self):
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(
                Ec.visibility_of_element_located(self.comfort_active))
            return "active" in active_button.get_attribute("class")
        except: return False

    def click_number_text(self, telefone):
        self.driver.find_element(*self.number_text_locator).click()
        self.driver.find_element(*self.number_enter).send_keys(telefone)
        self.driver.find_element(*self.number_confirm).click()

        code = retrieve_phone_code(self.driver)

        code_input = WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.number_code)
        )
        code_input.clear()
        code_input.send_keys(code)

        self.driver.find_element(*self.code_confirm).click()

    def numero_telefone_confirmado(self):
       numero = WebDriverWait(self.driver, 10).until(
           Ec.visibility_of_element_located(self.number_finish))
       return numero.text


    def click_add_card(self,card,code):
       self.driver.find_element(*self.add_forma_pagamento).click()
       self.driver.find_element(*self.add_card).click()
       time.sleep(1)
       self.driver.find_element(*self.number_card).send_keys(card)
       time.sleep(1)
       self.driver.find_element(*self.code_card).send_keys(code)
       time.sleep(1)
       self.driver.find_element(*self.add_finish_card).click()
       self.driver.find_element(*self.close_button_card).click()

    def confirm_cartao(self):
        return self.driver.find_element(*self.confirm_card).text

    def add_comentario(self, comentario):
        self.driver.find_element(*self.add_comment).send_keys(comentario)

    def comment_confirm(self):
        return self.driver.find_element(*self.add_comment).get_attribute('value')

    def switch_cobertor(self):
        switch_active = self.driver.find_element(*self.switch_blanket)
        switch_active.click()

    def switch_cobertor_ativo(self):
        switch = WebDriverWait(*self.driver, 10).until(
            Ec.presence_of_element_located(self.switch_blanket))
        return switch.is_selected()

    def add_sorvete(self):
        self.driver.find_element(*self.add_ice_cream).click()

    def quant_sorvete(self):
        return self.driver.find_element(*self.number_of_ice_creams).text

    def call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def janela_pop_up(self):
        pop_up = WebDriverWait(self.driver, 10).until(
            Ec.presence_of_element_located(self.pop_up)
        )
        return pop_up.text





