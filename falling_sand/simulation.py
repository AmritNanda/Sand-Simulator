from grid import Grid
from particle import SandParticle
from particle import RockParticle
import pygame, sys
class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.cell_size = cell_size
        self.mode = "sand"
        self.brush_size = 3
        
    def draw(self, window):
         self.grid.draw(window)
         
    def add_particle(self, row, column):
        if self.mode == "sand":
            particle = SandParticle
        elif self.mode == "rock":
            particle = RockParticle
        
        
        self.grid.add_particle(row, column, particle)
    
    def remove_particle(self,row,column):
        self.grid.remove_particle(row, column, SandParticle)
    def update(self):
        for row in range(self.grid.rows-2,-1,-1):
            if row %2 == 0:
                column_range = range(self.grid.columns)
            else:
                column_range = reversed(range(self.grid.columns))
            for column in column_range:
                particle = self.grid.get_cell(row,column)
                if isinstance(particle, SandParticle):
                    new_pos = particle.update(self.grid, row, column)
                    if new_pos != (row, column):
                        self.grid.set_cell(new_pos[0], new_pos[1], particle)
                        self.grid.remove_particle(row,column)
                        
    def restart(self):
        self.grid.clear()
        
    def handle_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)
        self.handle_mouse()
        
    def handle_key(self, event):
        if event.key == pygame.K_SPACE:
            self.restart()
        elif event.key == pygame.K_s:
            print('Sand mode')
            self.mode = "sand"
        elif event.key == pygame.K_r:
            print("Rock mode")
            self.mode = "rock"
        elif event.key == pygame.K_e:
            print(" Eraser Mode")
            self.mode = "erase"
            
    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            pos = pygame.mouse.get_pos()
            row = pos[1]// self.cell_size
            column = pos[0] // self.cell_size
            self.apply_brush(row, column)
            
    def apply_brush(self,row,column):
        for r in range(self.brush_size):
            for c in range(self.brush_size):
                current_row = row + r
                current_col = column + c
                
                if self.mode == 'erase':
                    self.grid.remove_particle(current_row,current_col)
                else:
                    self.add_particle(current_row,current_col)