from seleniumTester import *
from utils import *

###initializes variables

# initializes GUI screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# sets the surface variable in Surf class in utils.py. used in some other classes in utils
Surf.surface = screen
# variable used for checking if a test was run yet or not
ranTest = True

# default class for making screen UIs
class Screen:
    screens = []
    state = 0
    def __init__(self) -> None:
        self.bg = pygame.Surface((Fonts.WIDTH, Fonts.HEIGHT))
        gradient(Colors.bgCol1, Colors.bgCol2, self.bg)
        self.texts = []
        self.buttons = []
        self.clickedIndex = None
        Screen.screens.append(self)

    def render(self, surface):
        surface.blit(pygame.transform.scale(self.bg, (surface.get_width(), surface.get_height())), (0,0))
        for button in self.buttons:
            button.draw(surface)
        for text in self.texts:
            text.draw(surface)

    def update(self):
        pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.checkMouseOver(pos):
                button.hovering = True
            else:
                button.hovering = False

    def handleInput(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                i = 0
                for button in self.buttons:
                    if button.checkMouseOver(pos):
                        if button.onClickFunc != None:
                            self.clickedIndex = i
                            button.onClickFunc()
                    i += 1


    def run(screen, events):
        Screen.screens[Screen.state].render(screen)
        Screen.screens[Screen.state].update()
        Screen.screens[Screen.state].handleInput(events)

# menu screen that displays all the different modules
class MenuScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.texts = [
            Text("Modules", "title", Colors.textCol, (50, 3), True, True)
        ]
        self.buttons = [
            Button("Relationships", pygame.Rect(40, 45, 20, 10), 30, onclickFunc=self.buttonOnclick),
            # Button("Other", pygame.Rect(40, 60, 20, 10), 30, onclickFunc=self.buttonOnclick)
        ]
        self.buttonActions = [clickOnRelationships]
        self.modulesOpen = [False]
    
    def buttonOnclick(self):
        if self.clickedIndex != None:
            if self.modulesOpen[self.clickedIndex] == False:
                self.buttonActions[self.clickedIndex]()
                self.modulesOpen[self.clickedIndex] = True
                self.closeOtherModules()

            Screen.state = 1 + self.clickedIndex
        else:
            print("self clicked index is none")
    
    def closeOtherModules(self):
        for i in range(len(self.modulesOpen)):
            if self.modulesOpen[i] == True and i != self.clickedIndex:
                self.modulesOpen[i] = False

# screen that contains all the tests within the relationships module
class RelationshipsScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.texts = [
            Text("Which test would you like to run?", "title", Colors.textCol, (50,3), True, True)
        ]
        self.buttons = [
            Button("Create Organization", pygame.Rect(18, 25, 30, 15), 30, onclickFunc=self.buttonOnClick),
            Button("Create Contact", pygame.Rect(52, 25, 30, 15), 30, onclickFunc=self.buttonOnClick),
            Button("Edit Contact", pygame.Rect(18, 45, 30, 15), 30, onclickFunc=self.buttonOnClick),
            Button("Create Activity", pygame.Rect(52, 45, 30, 15), 30, onclickFunc=self.buttonOnClick),
            Button("Test All", pygame.Rect(35, 65, 30, 15), 30, onclickFunc=self.buttonOnClick)
        ]
        
        self.testTitles = ["Testing Create Organization", "Testing Create Contact", "Testing Edit Contact", "Testing Create Activity", "Testing All"]
        self.buttonActions = [createAnOrganization, createAContact, editAContact, createAnActivity, testAll]

    def buttonOnClick(self):
        global ranTest
        Screen.state += 1
        testScreen.texts = [Text(self.testTitles[self.clickedIndex], "title", Colors.textCol, (50, 5), True)]
        ranTest = False
        pygame.time.set_timer(pygame.USEREVENT, 1000)

# screen that is displayed while running a test. says "done" when its done
class TestingScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.texts = [
            Text("Test 1", "title", Colors.textCol, (50, 5), True)
        ]
        self.buttons = [
            Button("Back", pygame.Rect(35, 80, 30, 15), 30, onclickFunc=self.buttonOnClick)
        ]
        self.textPosition = 25 + 3

    def render(self, surface):
        super().render(surface)
        # pygame.draw.rect(surface, Colors.textCol, convertRect(surface, (10, 25, 80, 50)), 4)

    def update(self):
        super().update()

    def handleInput(self, events):
        global ranTest
        super().handleInput(events)
        for event in events:
            if ranTest == False:
                if event.type == pygame.USEREVENT:
                    lenBefore = len(Errors.errors)
                    relationshipMenu.buttonActions[relationshipMenu.clickedIndex]()
                    ranTest = True
                    self.texts.append(Text("Done!", "subtitle", Colors.textCol, (50,40), True))
                    if len(Errors.errors) > lenBefore:
                        self.texts.append(Text("Complete with errors", "paragraph", (220, 50, 65), (50, 47), True))
                    else:
                        self.texts.append(Text("Complete without errors", "paragraph", Colors.textCol, (50, 47), True))

    def addError(self, text):
        error = Text(text, "paragraph", Colors.textCol, (12, self.textPosition), False)
        self.texts.append(error)
        self.textPosition += 5

    def buttonOnClick(self):
        Screen.state = 0


menu = MenuScreen()
relationshipMenu = RelationshipsScreen()
testScreen = TestingScreen()