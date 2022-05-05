# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:15:58 2022

@author: Ritika
"""

from itertools import permutations, product, combinations

#nationality
french = 0
greek = 1
brazilian = 2
english = 3
spanish = 4
nationstr = ["french", "greek", "brazillian", "english", "spanish"]

#time
five = 0
six = 1
seven = 2
eight = 3
nine = 4
deptimestr = ["5:00", "6:00", "7:00", "8:00", "9:00"]

#cargo
tea = 0
coffee = 1
cocoa = 2
rice = 3
corn = 4
cargostr = ["tea", "coffee", "cocoa", "rice", "corn"]

#colour
blue = 0
red = 1
black = 2
white = 3
green = 4
colourstr = ["blue", "red", "black", "white", "green"]

#destination
genoa = 0
manila = 1
port_said = 2
hamburg = 3
marseille = 4
deststr = ["genoa", "manila", "port said", "hamburg", "marseille"]

#position
left = 0
middleleft = 1
middle = 2
middleright = 3
right = 4
posstr = ["left", "middle left", "middle", "middle right", "right"]

deptime = list(permutations([0,1,2,3,4], 5)
nation = list(permutations([0,1,2,3,4], 5)
destination = list(permutations([0,1,2,3,4], 5)
cargo = list(permutations([0,1,2,3,4], 5)
colour = list(permutations([0,1,2,3,4], 5)
 
# all possible solutions
#1. The Greek ship leaves at six and carries coffee.
def cond1(deptime, nationality, destination, cargo, colour):
    pos = nationality.index(greek)
    return deptime[pos] == six and cargo[pos] == coffee
 
#2. The ship in the middle has a black chimney.    
def cond2(deptime, nationality, destination, cargo, colour):
    pos = middle
    return color[pos] == black
    
#3. The English ship leaves at nine.
def cond3(deptime, nationality, destination, cargo, colour):
    pos = nationality.index(english)
    return deptime[pos] == nine

#4. The French ship with a blue chimney is to the left of a ship that carries coffee.    
def cond4(deptime, nationality, destination, cargo, colour):
    pos = nationality.index(french)
    return color[pos] == blue and pos - cargo.index(coffee) == -1

#5. To the right of the ship carrying cocoa is a ship going to Marseille.
def cond5(deptime, nationality, destination, cargo, colour):
    pos = cargo.index(cocoa)
    return pos < 4 and destination[pos + 1] == marseille   

#6. The Brazilian ship is heading for Manila.
def cond6(deptime, nationality, destination, cargo, colour):
    pos = nationality.index(brazilian)
    return destination[pos] == manila

#7. Next to the ship carrying rice is a ship with a green chimney.
def cond7(deptime, nationality, destination, cargo, colour):
    pos = cargo.index(rice)
    return colour[pos + 1] == green

#8. A ship going to Genoa leaves at five.
def cond8(deptime, nationality, destination, cargo, colour):
    pos = destination.index(genoa)
    return deptime[pos] == five

#9. The Spanish ship leaves at seven and is to the right of the ship going to Marseille.
def cond9(deptime, nationality, destination, cargo, colour):
    pos = nationality.index(spanish)
    return deptime[pos] == seven and pos - destination.index(marseille) == 1

#10. The ship with a red chimney goes to Hamburg.
def cond10(deptime, nationality, destination, cargo, colour):
    pos = colour.index(red)
    return destination[pos] == hamburg

#11. Next to the ship leaving at seven is a ship with a white chimney.
def cond11(deptime, nationality, destination, cargo, colour):
    pos = deptime.index(seven)
    return colour[pos + 1] == white

#12. The ship on the border carries corn.
def cond12(deptime, nationality, destination, cargo, colour):
    pos = right
    return cargo[pos] == corn

#13. The ship with a black chimney leaves at eight.
def cond13(deptime, nationality, destination, cargo, colour):
    pos = colour.index(black)
    return deptime[pos] == eight

#14. The ship carrying corn is anchored next to the ship carrying rice.
def cond14(deptime, nationality, destination, cargo, colour):
    pos = cargo.index(corn)
    return cargo[pos + 1] == rice

#15. The ship to Hamburg leaves at six.
def cond15(deptime, nationality, destination, cargo, colour):
    pos = destination.index(hamburg)
    return deptime[pos] == six

#looping through all possible solutions
sols = product(deptime, nation, destination, cargo, colour)

#prints solution
def pretty(sol):
   for i in range(5):
      print("The", colourstr[i], "ship is located at", posstr[i],", leaving at", deptimestr[i], "is carrying", cargostr[i] , "and is going to", deststr[i])

#checking condition and printing
for sol in sols:
    if cond1(sol[0], sol[1], sol[2], sol[3], sol[4])  and
       cond2(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond3(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond4(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond5(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond6(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond7(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond8(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond9(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond10(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond11(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond12(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond13(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond14(sol[0], sol[1], sol[2], sol[3], sol[4]) and
       cond15(sol[0], sol[1], sol[2], sol[3], sol[4]):
           pretty(sol)
       





 

