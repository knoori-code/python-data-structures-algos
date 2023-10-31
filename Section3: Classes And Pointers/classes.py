class Cookie:
  def __init__(self, colour):
    self.colour = colour

  def get_colour(self):
    return self.colour
    
  def set_colour(self, colour):
    self.colour = colour

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_colour())
print('Cookie two is', cookie_two.get_colour())

cookie_one.set_colour('red')
cookie_two.set_colour('purple')

print('Cookie one is', cookie_one.get_colour())
print('Cookie two is', cookie_two.get_colour())