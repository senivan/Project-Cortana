from math import pi

def path_length(h, H, S):
  """Calculates path length of squirrel climbing a tree."""
  return round(H * pi * S / h, 4)


################################ Попросив написати в один рядок

from math import pi; print(round((lambda h,H,S: H//h*S + pi*(H%h)/h)(4,16,3),4))

################################ Дав тестів з кодворсу

def squirrel(h, H, S):
  """Calculates path length of squirrel climbing a tree."""
  loops, remainder = divmod(H, h)
  return round(loops * S + pi * remainder / h, 4)

################################Дав формулул

def squirrel(h,H,S):return round((h*h+S*S)**.5*H/h,4)

###############################Просив укоротити

def squirrel(h,H,S):return round((h**2+S**2)**.5*H/h,4)


###############################

squirrel=lambda h,H,S: round((h*h+S*S)**.5*H/h,4)

# It took a lot of negotiations and feeding the answear to make him write this code