from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class Test1(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Edge() 

    def url (self):
        url = self.driver.get("https://www.corotos.com.do")
        return url   
    
    #Historia de usuario 1- inicio de sesion
    def test_01_inicio_de_sesion_valido(self):
        
        self.url()
        self.inicio_de_sesion = self.driver.find_element(By.ID, 'g4-taco-signin-button')
        self.inicio_de_sesion.click()
        self.inicio_de_sesion = self.driver.find_element(By.ID, 'app_user_email')
        self.inicio_de_sesion.send_keys("dp673162@gmail.com")
        self.inicio_de_sesion = self.driver.find_element(By.ID, 'app_user_password')
        self.inicio_de_sesion.send_keys("paoladaniel16")
        #Primera captura de pantalla
        screenshots = r"C:\\Users\\User\\OneDrive\\Desktop\\Automatizacion\\capturas"
        test_01_img_1 = "test_01_inicio_de_sesion_valido.png"
        concatenar = screenshots + "/" + test_01_img_1
        self.driver.save_screenshot(concatenar)
        self.inicio_de_sesion.submit()
        time.sleep(5)
        #Segunda captura de pantalla
        test_01_img_2 = "test_01_inicio_de_sesion_valido_2.png"
        concatenar2 = screenshots + "/" + test_01_img_2
        self.driver.save_screenshot(concatenar2)
        
    #Historia de usuario 1- inicio de sesion invalido
    def test_02_inicio_de_sesion_invalido(self):
        
        self.url()
        self.inicio_de_sesion = self.driver.find_element(By.ID, 'g4-taco-signin-button')
        self.inicio_de_sesion.click()
        self.inicio_de_sesion = self.driver.find_element(By.ID, 'app_user_email')
        self.inicio_de_sesion.send_keys("123@gmail.com")
        self.inicio_de_sesion = self.driver.find_element(By.ID, 'app_user_password')
        self.inicio_de_sesion.send_keys("123")
        #Primera captura de pantalla
        screenshots = r"C:\\Users\\User\\OneDrive\\Desktop\\Automatizacion\\capturas"
        test_02_img_1 = "test_02_inicio_de_sesion_invalido.png"
        concatenar = screenshots + "/" + test_02_img_1
        self.driver.save_screenshot(concatenar)
        self.inicio_de_sesion.submit()
        time.sleep(5)
        #Segunda captura de pantalla
        test_02_img_2 = "test_02_inicio_de_sesion_invalido_2.png"
        concatenar2 = screenshots + "/" + test_02_img_2
        self.driver.save_screenshot(concatenar2)
    
   #Historia de usuario 2- busqueda
    def test_03_busqueda(self):
        
        self.url()
        self.busqueda = self.driver.find_element(By.ID, 'search')
        self.busqueda.send_keys("laptops")
        #Primera captura de pantalla
        screenshots = r"C:\\Users\\User\\OneDrive\\Desktop\\Automatizacion\\capturas"
        test_03_img_1 = "test_03_busqueda.png"
        concatenar = screenshots + "/" + test_03_img_1
        self.driver.save_screenshot(concatenar)
        self.busqueda = self.driver.find_element(By.CLASS_NAME,'common-search-bar__field__icon')
        self.busqueda.click()
        time.sleep(3)
        #Segunda captura de pantalla
        test_03_img_2 = "test_03_busqueda_2.png"
        concatenar2 = screenshots + "/" + test_03_img_2
        self.driver.save_screenshot(concatenar2)
    
    #Historia de usuario 3-filtro    
    def test_04_filtro(self):
        
        self.url()
        self.filtro = self.driver.find_element(By.CLASS_NAME, 'navbar-desktop__categories_and_more')
        self.filtro.click()
        #Primera captura de pantalla
        screenshots = r"C:\\Users\\User\\OneDrive\\Desktop\\Automatizacion\\capturas"
        test_04_img_1 = "test_04_filtro.png"
        concatenar = screenshots + "/" + test_04_img_1
        self.driver.save_screenshot(concatenar)
        self.filtro = self.driver.find_element(By.ID, 'g4-taco-elements-display-menu-electronics-link')
        self.filtro.click()
        time.sleep(3)
        #Segunda captura de pantalla
        test_04_img_2 = "test_04_filtro_2.png"
        concatenar2 = screenshots + "/" + test_04_img_2
        self.driver.save_screenshot(concatenar2)
    
    #Historia de usuario 4- Cambiar la ubicación de búsqueda
    def test_05_ubicacion_preferencia (self):
        
        self.url()
        self.ubicacion = self.driver.find_element(By.CLASS_NAME, 'navbar-desktop__categories_and_more')
        self.ubicacion.click()
        self.ubicacion = self.driver.find_element(By.ID, 'g4-taco-elements-display-menu-electronics-link')
        self.ubicacion.click()
        # Espera hasta que el elemento esté visible
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div[3]/div[1]/div[1]/div[2]/div[1]/span')))
        self.ubicacion = self.driver.find_element(By.XPATH, '/html/body/div/div/div/main/div/div[3]/div[1]/div[1]/div[2]/div[1]/span')
        self.ubicacion.click()
        #Primera captura
        screenshots = r"C:\\Users\\User\\OneDrive\\Desktop\\Automatizacion\\capturas"
        test_05_img_1 = "test_05_ubicacion.png"
        concatenar = screenshots + "/" + test_05_img_1
        self.driver.save_screenshot(concatenar)
        time.sleep(5)
        self.ubicacion = self.driver.find_element(By.ID, 'province-option-27').click()
        #Segunda captura
        test_05_img_2 = "test_05_ubicacion_2.png"
        concatenar2 = screenshots + "/" + test_05_img_2
        self.driver.save_screenshot(concatenar2)
        self.ubicacion = self.driver.find_element(By.XPATH, '/html/body/div/div/div/main/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]/button[2]').click()
        time.sleep(3)
        #tercera captura
        test_05_img_3 = "test_05_ubicacion_3.png"
        concatenar3 = screenshots + "/" + test_05_img_3
        self.driver.save_screenshot(concatenar3)
    
    #Historia de usuario 5- Establecer un rango de precios mínimo y máximo
    def test_06_min_max_precio (self):
        
        self.url()
        self.min_max = self.driver.find_element(By.CLASS_NAME, 'navbar-desktop__categories_and_more')
        self.min_max.click()
        self.min_max = self.driver.find_element(By.ID, 'g4-taco-elements-display-menu-electronics-link')
        self.min_max.click()
        self.min_max = self.driver.find_element(By.CLASS_NAME, "common-input-text")
        self.min_max.send_keys("5000")
        #Primera captura
        screenshots = r"C:\\Users\\User\\OneDrive\\Desktop\\Automatizacion\\capturas"
        test_06_img_1 = "test_06_min_max.png"
        concatenar = screenshots + "/" + test_06_img_1
        self.driver.save_screenshot(concatenar)
        self.min_max = self.driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/div[3]/div[1]/div[1]/div[5]/div/div[2]/div[2]/label/div/div/input")
        self.min_max.send_keys("27000")
        #Segunda captura
        test_06_img_2 = "test_06_min_max_2.png"
        concatenar2 = screenshots + "/" + test_06_img_2
        self.driver.save_screenshot(concatenar2)
        self.min_max = self.driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/div[3]/div[1]/div[1]/div[5]/div/button").click()
        time.sleep(3)
        test_06_img_3 = "test_06_min_max_3.png"
        concatenar3 = screenshots + "/" + test_06_img_3
        self.driver.save_screenshot(concatenar3)
    
    #Historia de usuario 6- Elegir entre productos nuevos y usados    
    def test_07_nuevo_usado (self):
        
        self.url()
        self.nuevo_usado = self.driver.find_element(By.CLASS_NAME, 'navbar-desktop__categories_and_more')
        self.nuevo_usado.click()
        self.nuevo_usado = self.driver.find_element(By.ID, 'g4-taco-elements-display-menu-electronics-link')
        self.nuevo_usado.click()
        self.nuevo_usado = self.driver.find_element(By.CLASS_NAME, 'common-option-box__input').click()
        #Primera captura
        screenshots = r"C:\\Users\\User\\OneDrive\\Desktop\\Automatizacion\\capturas"
        test_07_img_1 = "test_07_nuevo_usado.png"
        concatenar = screenshots + "/" + test_07_img_1
        self.driver.save_screenshot(concatenar)
        time.sleep(4)
        #Segunda captura
        test_07_img_2 = "test_07_nuevo_usado_2.png"
        concatenar2 = screenshots + "/" + test_07_img_2
        self.driver.save_screenshot(concatenar2)
        
    def tearDown(self):
        self.driver.close   
if __name__ == '__main__' :
    unittest.main()
    
    