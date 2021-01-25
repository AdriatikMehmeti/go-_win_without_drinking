from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random, string, datetime
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

info = {"Emri":"Input_Name","Mbiemri":"Input_sureName","Teli":"Input_PhoneNumber","Qyteti":"Input_City","Nuk_egziston":"Kodi i dhene nuk eshte i vlefshem","Kodi_i_vlefshum":"Nuk keni fituar por jeni bere pjese e shortit per premite kryesore. Luaj perseri dhe rrit shansat."}
f = open('GO_Plus_KEY.txt', 'w').close()

def rujeKod(kodi,flag):
    f = open('GO_Plus_KEY.txt', 'a')
    f.write("\n" + str(datetime.datetime.now()) + " " + str(kodi) + " " + str(flag)); f.close()

while True:
    try:
        Kodi = random.choice(string.ascii_uppercase)+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=Options().add_argument("user-agent={}".format(UserAgent().random)))
        driver.get('https://www.lojagoplus.com/')
        driver.execute_script('window.scrollTo(0,1000000)')
        driver.implicitly_wait(3)
        emri = driver.find_element_by_xpath("//input[@placeholder='Emri']").send_keys(info.get("Emri"))
        mbiemri = driver.find_element_by_xpath("//input[@placeholder='Mbiemri']").send_keys(info.get("Mbiemri"))
        Tel = driver.find_element_by_xpath("//input[@placeholder='Nr. Telefonit']").send_keys(info.get("Teli"))
        Qytet = driver.find_element_by_xpath("//input[@placeholder='Vendbanimi']").send_keys(info.get("Qyteti"))
        kodi = driver.find_element_by_xpath("//input[@placeholder='Kodi']").send_keys(Kodi)
        nextButton = driver.find_elements_by_xpath("//input[@placeholder='SUBMIT']")[0].click()
        if driver.find_element_by_xpath("//h3[@class='errori border-red-500']").text == info.get("Nuk_egziston"): print(Kodi,'Nuk eshte VALID');driver.close()
        elif driver.find_element_by_xpath("//h3[@class='mesazhi border-red-500']").text == info.get("Kodi_i_vlefshum"): print(Kodi,'VALID po ska sen');rujeKod(Kodi,'VALID po ska sen');driver.close()
        else: print(Kodi,'VALID, ke fitu Diqka');rujeKod(Kodi,'VALID, ke fitu Diqka')
    except:
        print('Error -',info.get("Emri"))
