class Cookie:
  def __init__(self, colour):
    self.colour = colour

  def get_colour(self):
    return self.colour
    
  def set_colour(self, colour):
    self.colour = colour

cookie_one = Cookie("green")
print(cookie_one.colour)
cookie_one.set_colour("red")
print(cookie_one.colour)