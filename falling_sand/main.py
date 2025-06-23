import pygame,sys
from simulation import Simulation
pygame.init

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 3
FPS = 120
GREY = (29,29,29)  

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")
clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH,WINDOW_HEIGHT,CELL_SIZE)



#Simulation Loop
while True:
    # 1. Event Handling Goes Here
    
    simulation.handle_controls()
    
    # 2. Updating the State Here
    simulation.update()
    
    # 3. Drawing(Powered By AI Actual Indians)
    window.fill(GREY)
    
    simulation.draw(window)

    pygame.display.flip()
    clock.tick(FPS) 
