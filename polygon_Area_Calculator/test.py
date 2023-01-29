class J:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def cal(self):
        return self.x + self.y

    def __str__(self):
        return f"Rectangle(width=, height=)"

    def exp(self, p, q):
        self.x = p
        self.y = q
        return p*q

    def exp_2(self):
        return self.

# width = 2
# height = 3
# if width >= 50 or height >= 50:
#     print("Too big for picture.")
# else:
#     while height > 0:
#         print('*' * 10)
#         height -= 1
