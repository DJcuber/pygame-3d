import pygame as pg
import math
import matrix

class Game:
  def __init__(self):
    pg.init()
    self.windowSize = (800, 600)
    self.window = pg.display.set_mode(self.windowSize)
    self.clock = pg.time.Clock()
    self.running = True
  
  def run(self):
    pyramid = Object3d("tetrahedron", 0, 0, 0, "#ff0000")
    while self.running:
      self.window.fill("#000000")
      pyramid.rotation += 0.1
      if pyramid.rotation > 2 * math.pi:
        pyramid.rotation -= 2 * math.pi

      pyramid.update()
      self.draw3d(pyramid)
      self.eventHandle()
      pg.display.flip()
      self.clock.tick(10)

  def eventHandle(self):
    for ev in pg.event.get():
      if ev.type == pg.QUIT:
        self.running = False 
  
  def draw3d(self, obj):
    point = []
    for i in obj.vertices:
      point.append((int(self.windowSize[0]*i[0]/i[2] + self.windowSize[0]/2), int(self.windowSize[1]*i[1]/i[2] + self.windowSize[1]/2)))
    for i in obj.edges:
      pg.draw.aaline(self.window, obj.color, point[i[0]], point[i[1]])
        

class Object3d:
  def __init__(self, objType, pos, scale, rotation, color):
    self.objType = objType
    self.rotation = rotation
    self.color = color
    #self.vertices = [(x, y, z) for z in range(2) for y in range(2) for x in range(2)]
    if objType == "cube":
      self.vertices = [(0.5, 0.5, 2), (0.5, 0.5, 3), (-0.5, 0.5, 2), (-0.5, 0.5, 3), (0.5, -0.5, 2), (0.5, -0.5, 3), (-0.5, -0.5, 2), (-0.5, -0.5, 3)]
      self.edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 6), (4, 5), (5, 7), (6, 7)]

    if objType == "tetrahedron":
      self.vertices = [(1/(2*math.sqrt(2)), 0.5, 3), (-1/(2*math.sqrt(2)), 0.5, 3), (0, 0, 2 + (math.sqrt(3))/4), (0, (1/2), (math.sqrt(3)/4)+ 2)]
      self.edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

  def update(self):
    if self.objType == "cube":
      self.vertices = [(0.5, 0.5, 2), (0.5, 0.5, 3), (-0.5, 0.5, 2), (-0.5, 0.5, 3), (0.5, -0.5, 2), (0.5, -0.5, 3), (-0.5, -0.5, 2), (-0.5, -0.5, 3)] 
      self.edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 6), (4, 5), (5, 7), (6, 7)]

    if self.objType == "tetrahedron":
      self.vertices = [(1/(2*math.sqrt(2)), 0.5, 3), (-1/(2*math.sqrt(2)), 0.5, 3), (0, 0, 2 + (math.sqrt(3))/4), (0, (1/2), (math.sqrt(3)/4)+ 2)]
      self.edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

  


def main():
  game = Game()
  game.run()
  pg.quit()

if __name__ == "__main__":
  main()

