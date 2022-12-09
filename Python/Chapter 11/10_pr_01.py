class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return (f"The 2D Vector is: {self.icap}i + {self.jcap}j")

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return (f"The 3D Vector is: {self.icap}i + {self.jcap}j + {self.kcap}k")

v2d = C2dVec(2, 4)
print(v2d)
v3d = C3dVec(3, 5, 9)
print(v3d)


