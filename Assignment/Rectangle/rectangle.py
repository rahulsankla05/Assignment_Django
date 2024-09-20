class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  

    def __iter__(self):
        self._index = 0  
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # Stop after all iteration completion
        

# example 
rect = Rectangle(60, 55)

# Iterating over the rectangle
for dimension in rect:
    print(dimension)    # {'length': 60}{'width': 55}  it will be the output
