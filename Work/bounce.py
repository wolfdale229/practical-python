# bounce.py
# Exercise 1.5
'''A rubber ball is dropped from a height of 100 meters and each time it hits the 
ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that
prints a table showing the height of the first 10 bounces.
'''
height = 100

for n in range(1, 11):
    height = (3/5) * height
    print(f'{n} : {round(height, 4)}')