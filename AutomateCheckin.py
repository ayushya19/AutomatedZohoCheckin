from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-user-media-security=true")

driver  = webdriver.Chrome(executable_path='D:\Web Drivers Browser for Selenium\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)

driver.get("https://login.microsoftonline.com/bad261a0-0019-43fe-870f-f790b0d4a322/saml2?SAMLRequest=fVJba9swFP4rRu%2B2JV8TEQe8hrFAt5km60NfimIfJwJZynTk7PLrp6hrCYwVBELn8l3O0QrFpM68nd1JP8D3GdBFPyelkYdEQ2aruREokWsxAXLX8137%2BZ5nCeVna5zpjSLRdtOQ53w8MFhWYzEuhqIe8kVdiSwXgpaloP7FqpLVJSXRI1iURjfEg%2FhexBm2Gp3QzodolsW09GfPGM8Zpyxhi%2FqJRB%2BN7SEIbcgoFMK1tROI8gJvke6vpA9SD1If39d%2FeClC%2Fmm%2F7%2BLu625PohYRrPPq7ozGeQK7A3uRPXx7uG%2FIybkz8jQVfW9m7TD5bU4mkTpFedTXy88Mz2lFKWVFtizLikQbP1KphQuGXwGUOUqdTLK3Bs3ojFZSQ9KbKT2IIauYoLGHWMZFPkK8qOkYj%2FWSHuhQiDzLAk8WzF7kAPaLd9aQJ6%2BFrFfXHA8ztTebfH8Q4tU0WRuvI7jyYlbpDdgL8plfybabzijZ%2F4papcyPOwvCeQHOzhDWNAn3fz6%2FzhCRQzyGUg6TkKodBguI3kD6L89b8Pafrv8A&RelayState=aHR0cHM6Ly9wZW9wbGUuem9oby5pbi9wZW9wbGVfX0lBTV9fem9ob3Blb3BsZQ%3D%3D&sso_reload=true")
email = driver.find_element_by_id('i0116')
email.send_keys('ayushya.r@holosuit.com')
submit=driver.find_element_by_id('idSIButton9').click()

password = driver.find_element_by_id('i0118')
password.send_keys("myCHEMICALromance1#")
signin = driver.find_elements_by_class_name('win-button button_primary button ext-button primary ext-primary')
print(signin.isenabled())
signin.click()

try:
    check_page_load = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ZPD_Top_Att_Stat"))
    )
    
finally:
    # ZPD_Top_Att_Stat
    checkin_button = driver.find_element_by_id('ZPD_Top_Att_Stat')
    if(checkin_button.text == "Check-in"):
        checkin_button.click()
        print("Logged In !!")
    else:
        print("Already checkedin")
    driver.close()
    driver.quit()