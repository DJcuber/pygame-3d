
class Matrix4:
  def __init__(self, mat):
    self.mat = mat

  @staticmethod
  def perspecProjMat(r, l, t, b, n, f):
    mat = [[], [], [], []]
    mat[0] = [2*n / (r-l), 0, -(r+l) / (r-l), 0]
    mat[1] = [0, 2*n / (b-t), -(b+t) / (b-t), 0]
    mat[2] = [0, 0, f / (f - n), -f*n / (f-n)]
    mat[3] = [0, 0, 1, 0]
    return Matrix4(mat)
  
  @staticmethod
  def perspecMat(n, f):
    mat = [[], [], [], []]
    mat[0] = [n, 0, 0, 0]
    mat[1] = [0, n, 0, 0]
    mat[2] = [0, 0, (f+2), -f*n]
    mat[3] = [0, 0, 1, 0]
    return Matrix4(mat)
    
class Vector4:
  def __init__(self, vec):
    self.vec = vec

  def multiplyMat(self, mat: Matrix4):
    x = (self.vec[0] * mat.mat[0][0]) + (self.vec[1] * mat.mat[0][1]) + (self.vec[2] * mat.mat[0][2]) + (self.vec[3] * mat.mat[0][3])
    y = (self.vec[0] * mat.mat[1][0]) + (self.vec[1] * mat.mat[1][1]) + (self.vec[2] * mat.mat[1][2]) + (self.vec[3] * mat.mat[1][3])
    z = (self.vec[0] * mat.mat[2][0]) + (self.vec[1] * mat.mat[2][1]) + (self.vec[2] * mat.mat[2][2]) + (self.vec[3] * mat.mat[2][3])
    w = (self.vec[0] * mat.mat[3][0]) + (self.vec[1] * mat.mat[3][1]) + (self.vec[2] * mat.mat[3][2]) + (self.vec[3] * mat.mat[3][3])
    self.vec = [x, y, z, w]
  
  def multiplyScalar(self, n):
    self.vec[0] *= n
    self.vec[1] *= n
    self.vec[2] *= n
    self.vec[3] *= n

if __name__ == "__main__":
  #mat = Matrix4.perspecMat(1, 2)
  mat = Matrix4.perspecProjMat(1, -1, 1, -1, 1, 10)
  vec = Vector4([6, 6, 3, 1])
  vec.multiplyMat(mat)
  vec.multiplyScalar(1/vec.vec[3])
  print(vec.vec)