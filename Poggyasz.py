class Poggyasz:
    def __init__(self, a, b, c, m):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.m = int(m)
      
    def __str__(self):
        return f"Szélesség: {self.a}, Magasság: {self.b}, Mélység: {self.c}, Tömeg: {self.m}"
