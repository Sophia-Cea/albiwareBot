# this file handles the gui
from utils import *
from seleniumTester import *
import sys
from screens import *

# TODO : test to make sure its all still working

ranTest = True

logIn()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            driver.close()
            Errors.logErrors()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Errors("yee", "yeeeee")
            if event.key == pygame.K_RETURN:
                for error in Errors.errors:
                    print(error.toString())
    
    Screen.run(screen, events)
    pygame.display.flip()