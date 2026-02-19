import math

diameter = float(input("Enter the diameter of the sphere (metres): "))
radius = diameter / 2
volume = (4/3) * math.pi * radius**3
print(f"Volume of the sphere: {volume:.2f} cubic metres")