from utils import *
from scraper import *
import sys

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
Surf.surface = screen

logIn()
clickOnRelationships()

menu = Screen(
    [
        Button("Create Organization", pygame.Rect(21, 40, 26, 12), 30, onclickFunc=createAnOrganization),
        Button("Create Contact", pygame.Rect(51, 40, 26, 12), 30, onclickFunc=createAContact),
        Button("Edit Contact", pygame.Rect(21, 56, 26, 12), 30, onclickFunc=editAContact),
        Button("Create Activity", pygame.Rect(51, 56, 26, 12), 30, onclickFunc=createAnActivity)
    ],
    [
        Text("Which test would you like to run?", "title", Colors.textCol, (50,3), True, True)
    ]
)

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