# this file handles the gui
from utils import *
from seleniumTester import *
import sys
# from screens import *

WIDTH = 500
HEIGHT = 300
screen = pygame.display.set_mode([WIDTH, HEIGHT])
Surf.surface = screen
currentTest = 0
ranTest = True
testTitles = ["Testing Create Organization", "Testing Create Contact", "Testing Edit Contact", "Testing Create Activity"]
tests = [createAnOrganization, createAContact, editAContact, createAnActivity]


logIn()
clickOnRelationships()

def resetScreen1():
    screen1.texts[0] = Text(testTitles[currentTest], "title", Colors.textCol, (50, 15), True)

def setDefaultVars():
    global ranTest
    Screen.state = 1
    resetScreen1()
    ranTest = False
    pygame.time.set_timer(pygame.USEREVENT, 1000)

def runTestCreateOrganization():
    global currentTest
    currentTest = Tests.CreateOrganization
    setDefaultVars()

def runTestCreateContact():
    global currentTest
    currentTest = Tests.CreateContact
    setDefaultVars()

def runTestEditContact():
    global currentTest
    currentTest = Tests.EditContact
    setDefaultVars()

def runTestCreateActivity():
    global currentTest
    currentTest = Tests.CreateActivity
    setDefaultVars()

def setStateMenu():
    Screen.state = 0

menu = Screen(
    [
        Button("Create Organization", pygame.Rect(5, 25, 40, 20), 30, onclickFunc=runTestCreateOrganization),
        Button("Create Contact", pygame.Rect(55, 25, 40, 20), 30, onclickFunc=runTestCreateContact),
        Button("Edit Contact", pygame.Rect(5, 50, 40, 20), 30, onclickFunc=runTestEditContact),
        Button("Create Activity", pygame.Rect(55, 50, 40, 20), 30, onclickFunc=runTestCreateActivity)
    ],
    [
        Text("Which test would you like to run?", "title", Colors.textCol, (50,3), True, True)
    ]
)

screen1 = Screen(
    [
        Button("Back", pygame.Rect(35, 65, 30, 15), 30, onclickFunc=setStateMenu)
    ],
    [
        Text(testTitles[currentTest], "title", Colors.textCol, (50, 15), True)
    ]
)

def screen1Input(events):
    global ranTest
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in screen1.buttons:
                if button.checkMouseOver(pos):
                    if button.onClickFunc != None:
                        button.onClickFunc()
        if ranTest == False:
            if event.type == pygame.USEREVENT:
                tests[currentTest]()
                ranTest = True

screen1.inputFunction = screen1Input

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            driver.close()
            pygame.quit()
            sys.exit()
    
    Screen.run(screen, events)
    pygame.display.flip()