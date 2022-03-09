from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from bs4 import BeautifulSoup
from sqlalchemy import func
from selenium.webdriver.common.by import By
from loginData import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# initializes web driver that opens the browser
driver = webdriver.Chrome("/Users/chiac/Desktop/chromedriver98")

url = 'https://albiware.com'

# opens the window
driver.get(url)
# sets the amount of time that the driver should try to do something before giving up and throwing an error. time stays consistent throughout the session.
driver.implicitly_wait(5)


# functions for logging in
def clickLoginButton():
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div[2]/div/div[2]/div/div/div[1]/ul/li[6]/a").click()
    except:
        print("didn't find login button")

def enterLoginEmail():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[1]/input").send_keys(user)
    except:
        print("couldnt enter username")

def enterPassword():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[2]/div/input").send_keys(password)
    except:
        print("couldnt enter ur password")

def clickSubmit():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button").click()
    except:
        print("couldnt click the submit button")


#functions for making an organization
def clickOnRelationships():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/ul/li[6]/a/span[1]").click()
    except:
        print("didnt find relationships")

def clickOnOrganizations():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/ul/li[6]/ul/li[1]/a").click()
    except:
        print("didnt click on organizations")

def clickCreateNewTask():
    try:
        driver.find_element(By.CSS_SELECTOR, "#page-wrapper > div.row.wrapper.border-bottom.gray-bg.page-heading > div.col-sm-8 > div > a:nth-child(1)").click()
    except:
        print("couldnt click create new")

def inputName():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[1]/input").send_keys("sophia")
    except:
        print("name")

def clickOpenTypeMenu():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[2]/div/span/div/button/span").click()
    except:
        print("type")

def clickType():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[2]/div/span/div/ul/li[2]/a/label").click()
    except:
        print("contractor")

def enterEmail():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[3]/input").send_keys("sophia.cole@albiware.com")
    except:
        print("couldnt do ur email")

def enterPhoneNumber():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[4]/input").click()
        sleep(.5)
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[4]/input").send_keys("224")
        sleep(.5)
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[4]/input").send_keys("500")
        sleep(.5)
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[4]/input").send_keys("0231")
        sleep(.5)
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[4]/input").send_keys(Keys.RETURN) #***
    except:
        print("failed to do phone number")

def setSalesperson():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[5]/span[1]/span[1]/span/span[1]").click()
    except:
        print("didnt click 'salesperson'")
    try:
        driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[4]").click()
    except:
        print("didnt click dropdown menu")

def setReferalSource():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[7]/span[1]/span[1]/span/span[1]").click()
    except:
        print("couldnt click referral source")
    try:
        driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[2]").click()
    except:
        print("couldnt click 'online marketing'")

def clickSave():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[3]/button[2]").click()
    except:
        print("couldnt click save")

def enterAddress1():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[2]/div[1]/div/input").send_keys("1234 yee st")
    except:
        print("couldnt enter address 1")

def enterAddress2():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[2]/div[2]/div/input").send_keys("4321 yeee st")
    except:
        print("couldnt enter address2")

def enterCity():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[2]/div[3]/input").send_keys("narnia")
    except:
        print("couldnt enter city")

def enterState():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[2]/div[4]/input").send_keys("illinois")
    except:
        print("couldnt enter state")

def enterZipCode():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[2]/div[5]/input").send_keys("60515")
    except:
        print("couldnt enter zip code")

def enterCountry():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[2]/div[6]/input").send_keys("USA")
    except:
        print("couldnt enter country")

def enterSandbox():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[3]/div/textarea").send_keys("This organization belongs to Sophia.")
    except:
        print("couldnt type in textbox")

# this function consists of all the functions from line 68 to this point to simplify the process of recalling each function in order
def fillOutForm():
    inputName()
    clickOpenTypeMenu()
    clickType()
    enterEmail()
    enterPhoneNumber()
    setSalesperson()
    setReferalSource()
    enterAddress1()
    enterAddress2()
    enterCity()
    enterState()
    enterZipCode()
    enterCountry()
    enterSandbox()
    sleep(3)
    clickSave()


#functions for making a contact
def goToContacts():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/ul/li[6]/ul/li[2]/a").click()
    except:
        print("couldnt click contacts")

def clickCreateNewContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/a").click()
    except:
        print("xPath failed")
        try:
            driver.find_element(By.CSS_SELECTOR, "#page-wrapper > div.row.wrapper.border-bottom.gray-bg.page-heading > div.col-sm-8 > div > a").click()
        except:
            print("failed to click create new contact")

def enterContactFirstName():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[1]/input").send_keys("Sophia")
    except:
        print("xpath failed in 'enterContactFirstName'")
        try:
            driver.find_element(By.CSS_SELECTOR, "#FirstName").send_keys("Sophia")
        except:
            print("couldnt enter first name")

def enterContactLastName():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[2]/input").send_keys("Cole")
    except:
        print("couldnt enter last name")

def setContactType():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[5]/span[1]/div/button").click()
    except:
        print("couldnt click on contact")

    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[5]/span[1]/div/ul/li[7]/a/label/input").click()
    except:
        print("couldnt click 'customer'")

def setContactReferalSource():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[7]/span[1]/span[1]/span/span[1]").click()
    except:
        print("click referal source")

    try:
        driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[3]").click()
    except:
        print("click vehicle wraps")

def enterContactPhoneNumber():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[3]/input").click()
        sleep(.5)
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[3]/input").send_keys("224")
        sleep(.5)
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[3]/input").send_keys("500")
        sleep(.5)
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[3]/input").send_keys("0231")
        sleep(.5)
    except:
        print("failed to do phone number")

def inputEmailContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[4]/input").send_keys("sophia.cole@albiware.com")
    except:
        print("couldnt enter contact email")

def setOrganization():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[8]/span[1]/span[1]/span/span[1]").click()
    except:
        print("couldnt click organization box")

    try:
        driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[3]").click()
    except:
        print("couldnt click ruby de leon")

def setParentOrganization():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[9]/span[1]/span[1]/span/span[1]").send_keys()
    except:
        print()

    try:
        driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[34]").click()
    except:
        print("couldnt click yes organization")

def setSalesPersonContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[1]/div[10]/span[1]/span[1]/span/span[1]").click()
    except:
        print("couldnt click salesperson")

    try:
        driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[2]").click()
    except:
        print("couldnt click alex duta")

def inputAddress1Contact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[2]/div[1]/input[1]").send_keys("1234 street road")
    except:
        print("couldnt input address 1 contact")

def inputAddress2Contact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[2]/div[2]/input").send_keys("4321 street road")
    except:
        print("couldnt input address 2 contact")

def inputCityContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[2]/div[3]/input").send_keys("narnia")
    except:
        print("couldnt input city contact")

def inputStateContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[2]/div[4]/input").send_keys("alaska")
    except:
        print("couldnt input state contact")

def inputZipCodeContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[2]/div[5]/input").send_keys("123456")
    except:
        print("couldnt input zip code contact")

def inputCountryContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[2]/div[6]/input").send_keys("panem")
    except:
        print("couldnt input country contact")

def inputSandboxContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[2]/div/div[3]/div/textarea").send_keys("thinking lots of thoughts.")
    except:
        print("couldnt input sandbox contact")

def clickContactSubmit():
    try:
        driver.find_element(By.XPATH, "/html/body/div[30]/div/div[2]/form/div[3]/button[2]").click()
    except:
        print("couldnt submit contact")

# same concept as the comment on line 174
def fillOutContactForm():
    enterContactFirstName()
    enterContactLastName()
    setContactType()
    setContactReferalSource()
    enterContactPhoneNumber()
    inputEmailContact()
    setOrganization()
    setParentOrganization()
    setSalesPersonContact()
    inputAddress1Contact()
    inputAddress2Contact()
    inputCityContact()
    inputStateContact()
    inputZipCodeContact()
    inputCountryContact()
    inputSandboxContact()
    clickContactSubmit()



# functions for editing a contact
def findMyContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/div/div/div[4]/table/tbody/tr[3]/td[12]/div/a[1]").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/div/div/div[4]/table/tbody/tr[3]/td[12]/div/a[1]").click()
    except:  
        print("couldnt click on contact")

def clickEdit():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div[1]/span/a").click()
    except:
        print()

def changeFirstName(newName):
    try:
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[2]/div/div[1]/div[1]/input").clear()
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[2]/div/div[1]/div[1]/input").send_keys(newName)
    except:
        print()

def changeLastName(newLastName):
    try:
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[2]/div/div[1]/div[2]/input").clear()
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[2]/div/div[1]/div[2]/input").send_keys(newLastName)
    except:
        print("couldnt change last name")

def changeType():
    try:
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[2]/div/div[1]/div[5]/span[1]/div/button").click()
    except:
        print("couldnt click 'type' when editing contact")

    try:
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[2]/div/div[1]/div[5]/span[1]/div/ul/li[2]/a/label/input").click()
    except:
        print("couldnt check 'referrer'")

def changeReferralSource():
    try:
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[2]/div/div[1]/div[7]/span[1]/span[1]/span/span[1]").click()
    except:
        print("couldnt click 'referral source'")
    
    try:
        driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[2]").click()
    except:
        print("couldnt click 'online marketing")

def clickSaveEditingContact():
    try:
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/form/div[3]/button[2]").click()
    except:
        print("couldnt click save edited contact")


#making an activity
def clickCreateActivity():
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/a[2]").click()
    except:
        print("couldnt click create activity")

def setOrganizationActivity():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[1]/span[1]/span/span[1]").click()
    except:
        print("couldnt click organization acivity")

    try:
        driver.find_element(By.XPATH, "/html/body/div[41]/div/div[3]/ul/li[1]").click()
    except:
        print("couldnt click little bosses")

def setTypeActivity():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[2]/span[1]/span/span[1]").click()
    except:
        print("couldnt click type activity")

    try:
        driver.find_element(By.XPATH, "/html/body/div[42]/div/div[3]/ul/li[2]").click()
    except:
        print("Couldnt select sent email activity")

def setDateActivity():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[1]/div[3]/span[1]/span/span[2]/span[1]/span").click()
    except:
        print("couldnt open date menu activity")
    sleep(.2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[43]/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr[3]/td[3]/a").click()
        # driver.find_element(By.CSS_SELECTOR, "#ca16a75d-3842-4802-845f-f068f998c09a > div.k-calendar-view.k-calendar-monthview > table > tbody > tr:nth-child(3) > td:nth-child(3) > a").click()
    except:
        print("couldnt set date activity")
    sleep(.3)
    try:
        driver.find_element(By.XPATH, "/html/body/div[43]/div/div/div[3]/button[2]").click()
    except:
        print("couldnt set the date activity")

def setNotesActivity():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[2]/div[2]/div[2]/textarea").send_keys("the sky is blue.")
    except:
        print("couldnt write notes activity")

def clickSaveActivity():
    try:
        driver.find_element(By.XPATH, "/html/body/div[40]/div/div[2]/form/div[3]/button[2]").click()
    except:
        print("xpath failed in 'clickSaveActivity")

# same concept as comment on line 174
def makeAnActivity():
    setOrganizationActivity()
    setTypeActivity()
    setDateActivity()
    setNotesActivity()
    clickSaveActivity()



# these functions organize all of the above functions into easily callable methods to be used in main.py

# this function runs all the functions that log the user in
def logIn():
    clickLoginButton()
    enterLoginEmail()
    enterPassword()
    clickSubmit()

# this function runs all the relevant functions for creating an organization
def createAnOrganization():
    clickOnOrganizations()
    clickCreateNewTask()
    fillOutForm()
    
# this function runs all the relevant functions for creating a contact
def createAContact():
    goToContacts()
    clickCreateNewContact()
    fillOutContactForm()

# this functions runs all the relevant functions for editing the contact
def editAContact():
    goToContacts()
    findMyContact()
    clickEdit()
    changeFirstName("Not Sophia")
    changeLastName("Testing 2")
    changeType()
    changeReferralSource()
    clickSaveEditingContact()

# this function runs all the relevant functions for creating an activity
def createAnActivity():
    clickOnOrganizations()
    clickCreateActivity()
    makeAnActivity()


