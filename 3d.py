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
    t = 0
    cube = Object3d("tetrahedron", 0, 0, t, "#ff0000")
    mat = matrix.Matrix4.perspecProjMat(1, -1, 1, -1, 1, 10)
    points = self.translate(cube, mat)
    while self.running:
      self.window.fill("#000000")
      t += 0.1
      if cube.rotation > 2 * math.pi:
        cube.rotation -= 2 * math.pi
      cube = Object3d("tetrahedron", 0, 0, t, "#ff0000")
      points = self.translate(cube, mat)
      self.draw3d(cube, points)

      self.eventHandle()
      pg.display.flip()
      self.clock.tick(10)

  def eventHandle(self):
    for ev in pg.event.get():
      if ev.type == pg.QUIT:
        self.running = False 
  
  def draw3d(self, obj, point):
    for i in obj.edges:
      pg.draw.aaline(self.window, obj.color, point[i[0]][:2], point[i[1]][:2])
        
  def translate(self, obj, mat):
    points = []
    for i in obj.vertices:
      vec = i.multiplyMat(mat)
      newVec = [0]*3
      newVec[0] = int((1 + (vec.vec[0]/vec.vec[3]))*self.windowSize[0]/2)
      newVec[1] = int((1 + (vec.vec[1]/vec.vec[3]))*self.windowSize[1]/2)
      newVec[2] = vec.vec[2]
      points.append(newVec)
    return points


class Object3d:
  def __init__(self, objType, pos, scale, t, color):
    self.objType = objType
    self.rotation = t
    self.color = color
    #self.vertices = [(x, y, z) for z in range(2) for y in range(2) for x in range(2)]
    if objType == "cube":
      self.vertices = [(0.5, 0.5, 2), (0.5, 0.5, 3), (-0.5, 0.5, 2), (-0.5, 0.5, 3), (0.5, -0.5, 2), (0.5, -0.5, 3), (-0.5, -0.5, 2), (-0.5, -0.5, 3)]
      self.edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 6), (4, 5), (5, 7), (6, 7)]

    if objType == "tetrahedron":
      #self.vertices = [matrix.Vector4((math.sin(t)/(2*math.sqrt(2)), 0, 3)), matrix.Vector4((-math.sin(t+1)/(2*math.sqrt(2)), 0, 3)), matrix.Vector4((math.sin(t+2), 0, 2 + (math.sqrt(3))/4)), matrix.Vector4((0, (1/2), (math.sqrt(3)/4)+ 2))]
      self.vertices = [matrix.Vector4((math.sin(t+math.pi*4/3)/2, -0.15, 2+math.cos(t+math.pi*4/3)/2, 1)), matrix.Vector4((math.sin(t+math.pi*2/3)/2, -0.15, 2+math.cos(t+math.pi*2/3)/2, 1)), matrix.Vector4((math.sin(t)/2, -0.15, 2+math.cos(t)/2, 1)), matrix.Vector4((0, math.sqrt(3)/2, 2, 1))]
      self.edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    if self.objType == "cubeWithBones":
      self.vertices = [matrix.Vector4((x-0.5+math.sin(t)/2, y-0.5, z + math.cos(t)/2, 1)) for x in range(2) for y in range(2) for z in range(2, 4)]
      self.edges = [(i, j) for i in range(len(self.vertices)) for j in range(i, len(self.vertices)) if i != j]


  


def main():
  game = Game()
  game.run()
  pg.quit()

if __name__ == "__main__":
  main()