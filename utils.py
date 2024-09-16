import math

def area_retangulo(larg, compr):
  return larg * compr

def area_circulo(raio):
  return math.pi * raio**2

def unidade_adubo(valor):
  if valor > 1000:
    return f'{(valor / 1000):.1f}kg'
  else:
    return f'{valor}g'