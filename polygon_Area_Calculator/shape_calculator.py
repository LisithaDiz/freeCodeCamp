class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        line = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            y = self.height
            while y > 0:
                line = line + '*' * self.width + "\n"
                y -= 1
        return line

    def get_amount_inside(self, s):
        max_width = self.width // s.width
        max_height = self.height // s.height
        return max_width * max_height


class Square(Rectangle):

    def __init__(self, side):
        super(Square, self).__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"
