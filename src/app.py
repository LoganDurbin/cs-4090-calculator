import math


def add (a, b):
  return a + b

def subtract (a, b):
  return a - b

def multiply (a, b):
  return a * b

def divide (a, b): 
  if b == 0:
      raise ValueError("Cannot divide by zero.")
  return a / b

def square (a):
  return a * a

def square_root (a):
  if a < 0:
      raise ValueError("Cannot take the square root of a negative number.")
  return a ** 0.5

def percent (a, b):
  if b == 0:
      raise ValueError("Cannot divide by zero.")
  return (a / b) * 100

def log (a, base):
  if a <= 0:
      raise ValueError("Logarithm is undefined")
  if base <= 1:
      raise ValueError("Logarithm base must be greater than one.")
  return math.log(a, base)

def sin (a):
  return math.sin(a)

def cos (a):
  return math.cos(a)

def main(): # pragma: no cover
  switch = {
      'add': add,
      'subtract': subtract,
      'multiply': multiply,
      'divide': divide,
      'square': square,
      'squareroot': square_root,
      'percent': percent,
      'log': log,
      'sin': sin,
      'cos': cos
  }
  print("Available operations: " + ", ".join(switch.keys()))
  choice = input("Enter the operation you want to perform: ").strip().lower()
  if choice in switch:
      if choice in ['square', 'squareroot', 'sin', 'cos']:
          num = float(input("Enter the number: "))
          print(f"Result: {switch[choice](num)}")
      elif choice in ['log']:
          num = float(input("Enter the number: "))
          base = float(input("Enter the base: "))
          print(f"Result: {switch[choice](num, base)}")
      else:
          num1 = float(input("Enter the first number: "))
          num2 = float(input("Enter the second number: "))
          print(f"Result: {switch[choice](num1, num2)}")
  else:
      print("Invalid operation.")

if __name__ == "__main__": # pragma: no cover
  main()
