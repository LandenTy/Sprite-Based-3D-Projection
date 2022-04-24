"""
Render_Attempt_259
Description:
"""
# Import and Initalize Pygame
import pygame, sys
pygame.init()

# Variable
playerSpeed = 2
s = 5

tx = 0
ty = 0
tz = 0

win = pygame.display.set_mode([400, 400])

class Vertice():
    
    def __init__(self, coordinates):
        
        global s
        
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        
        zAxis = s * self.y / self.z
        
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), round(self.z))
        pygame.display.flip()

class Wireframe():
    
    def __init__(self, (v1, v2)):
        
        self.v1 = v1
        self.v2 = v2
        average = self.v1.z + self.v2.z / 2
        
        pygame.draw.line(win, (0, 0, 0), (self.v1.x, self.v1.y), (self.v2.x, self.v2.y), round(average))
        pygame.display.flip()

class Quad():
    
    def __init__(self, instanceID):
        
        self.instanceID = instanceID
        
    def Render(self, position):
        
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        
        v1 = Vertice([50 + position[0], 300 + position[1], 5 + position[2]])
        v2 = Vertice([50 + position[0], 100 + position[1], 5 + position[2]])
        v3 = Vertice([250 + position[0], 300 + position[1], 5 + position[2]])
        v4 = Vertice([250 + position[0], 100 + position[1], 5 + position[2]])
        
        Wireframe((v1, v2))
        Wireframe((v1, v3))
        Wireframe((v2, v4))
        Wireframe((v3, v4))

cube = Quad(10173)
cube.Render([tx, ty, tz])

while True:
    
    for ev in pygame.event.get():
        
        key = pygame.key.get_pressed()
        
        if ev.type == pygame.QUIT:
            sys.exit()
        
        if ev.type == pygame.KEYDOWN:
                
            if key[pygame.K_s]:
                
                # Size Based on Space from Virtual-Camera Plane
                tz -= 1
                cube.Render([tx, ty, tz])
                win.fill((255, 255, 255))
            
            if key[pygame.K_w]:
                
                # Size Based on Space from Virtual-Camera Plane
                tz += 1
                cube.Render([tx, ty, tz])
                win.fill((255, 255, 255))
            
            if key[pygame.K_a]:
                
                # Camera X-Movemtent
                tx += 5
                cube.Render([tx, ty, tz])
                win.fill((255, 255, 255))
            
            if key[pygame.K_d]:
                
                # Camera X-Movemtent
                tx -= 5
                cube.Render([tx, ty, tz])
                win.fill((255, 255, 255))
