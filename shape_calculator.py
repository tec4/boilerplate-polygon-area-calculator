class Rectangle:
    def __init__(self, width, height):
        self.width = width  
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        output = ''
        row = '*' * self.width + "\n"
        for n in range(self.height):
            output = output + row

        return output

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def set_side(self, length):
        self.height = length
        self.width = length

    def __str__(self):
        return 'Square(side=' + str(self.height) + ')'
