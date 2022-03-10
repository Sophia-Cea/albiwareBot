from utils import *

testTitles = ["Testing Create Organization", "Testing Create Contact", "Testing Edit Contact", "Testing Create Activity"]
# tests = [createAnOrganization, createAContact, editAContact, createAnActivity]

# menu = Screen(
#     [
#         Button("Create Organization", pygame.Rect(5, 25, 40, 20), 30, onclickFunc=runTestCreateOrganization),
#         Button("Create Contact", pygame.Rect(55, 25, 40, 20), 30, onclickFunc=runTestCreateContact),
#         Button("Edit Contact", pygame.Rect(5, 50, 40, 20), 30, onclickFunc=runTestEditContact),
#         Button("Create Activity", pygame.Rect(55, 50, 40, 20), 30, onclickFunc=runTestCreateActivity)
#     ],
#     [
#         Text("Which test would you like to run?", "title", Colors.textCol, (50,3), True, True)
#     ]
# )

# screen1 = Screen(
#     [
#         Button("Back", pygame.Rect(35, 65, 30, 15), 30, onclickFunc=setStateMenu)
#     ],
#     [
#         Text("deafault", "title", Colors.textCol, (50, 15), True)
#     ]
# )

# def screen1Input(events):
#     global ranTest
#     for event in events:
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             for button in screen1.buttons:
#                 if button.checkMouseOver(pos):
#                     if button.onClickFunc != None:
#                         button.onClickFunc()
#         if ranTest == False:
#             if event.type == pygame.USEREVENT:
#                 tests[currentTest]()
#                 ranTest = True

# screen1.inputFunction = screen1Input







class Screen:
    screens = []
    state = 0
    def __init__(self) -> None:
        self.bg = pygame.Surface((Fonts.WIDTH, Fonts.HEIGHT))
        gradient(Colors.bgCol1, Colors.bgCol2)
        self.texts = []
        self.buttons = []
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
                for button in self.buttons:
                    if button.checkMouseOver(pos):
                        if button.onClickFunc != None:
                            button.onClickFunc()

    def run(screen, events):
        Screen.screens[Screen.state].renderFunction(screen)
        Screen.screens[Screen.state].updateFunction()
        Screen.screens[Screen.state].inputFunction(events)




class MenuScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.texts = []
        self.buttons = []

    def render(self, surface):
        super().render(surface)
        pygame.draw.rect(surface, Colors.textCol, pygame.Rect())

    def update(self):
        super().update()

    def handleInput(self, events):
        super().handleInput(events)


