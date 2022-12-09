class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ''
        index = 0
        # for i in range(len(self.vec)):
        #     str1 += f" {self.vec[i]}a{index} +"  # Alternate way
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        if (len(self.vec) == len(vec2.vec)):
            newList = []
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
            return Vector(newList)
        else:
            return "The vectors are of different dimensions, can't add"
        
    
    def __mul__(self, vec2):
        if (len(self) == len(vec2)):  # (len(self.vec) == len(vec2.vec)) will also work
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
            return sum
        else:
            return "The vectors are of different dimensions, can't take dot product"

    def __len__(self):
        return len(self.vec)

# v1 = Vector([1, 4, 6, 34, 55, 43])
v1 = Vector([1, 4, 6, 8])
v2 = Vector([1, 6, 9])

# print(len(v1))
# print(len(v2))

print(v1+v2)
print(v1*v2)


