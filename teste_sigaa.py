import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class SigaaLoginTest(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(current_dir, 'chromedriver.exe')

        if not os.path.isfile(chromedriver_path):
            raise FileNotFoundError(f"ChromeDriver não encontrado no caminho: {chromedriver_path}")

        self.service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver

        url = "https://sigaa.ufrrj.br/sigaa/verTelaLogin.do"

        driver.get(url)

        usuario_input = driver.find_element(By.NAME, "user.login")
        usuario_input.send_keys("login_para_substituir") #substitua pelo seu login

        senha_input = driver.find_element(By.NAME, "user.senha")
        senha_input.send_keys("senha_para_substituir") #substitua pela sua senha

        login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Entrar']")
        login_button.click()

        time.sleep(3)

        try:
            sair_sistema = driver.find_element(By.XPATH, "//span[@class='sair-sistema']/a[@href='/sigaa/logar.do?dispatch=logOff']")
            self.assertTrue(sair_sistema.is_displayed())
            print("Login bem-sucedido!")
        except Exception as e:
            self.fail(f"Falha no login! {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
