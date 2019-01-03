#Ball drop gravity simulation
import pygame
(width,height)= 1280,720 #Change to be an input later
screen = pygame.display.set_mode((width,height))
#Window Properties
pygame.display.set_caption("Physics Simulation v1.0 by Bill")
backgroundcolor = (255,255,255)
screen.fill(backgroundcolor)

#Draws a circle

#Balls
class ball:
    def __init__(self,position,size):
        self.x, self.y = position
        self.size = size
        self.colour = (0,0,255) #Possible change to variable later
        self.thickness = 1
#Display Balls
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
 #Testing Balls
testball = ball((200,200),14)
testball.display()

#Flip command. Call last! IMPORTANT
pygame.display.flip()
#Code loop that allows window for close
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()
