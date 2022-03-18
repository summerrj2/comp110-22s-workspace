"""Underwater Fish Scene!

Something fun: I changed the pensize for the fish and waves. 
To avoid creating too complex of a function, I split up both the wave and fish drawing into three (fish) or four (wave) separate functions.
These are found on lines 16, 28, 42, and 51 (wave) and lines (60, 75, and 86). 
I utilized 8 different functions (beyond the requirement of 4).
"""

__author__ = "730322370"

from turtle import Turtle, colormode, done
Donatello: Turtle = Turtle()
Donatello.hideturtle()

def wave() -> None:
    """To Create the Ocean Wave Above Fish."""
    colormode(255)
    Donatello.color(0, 0, 255)
    Donatello.pensize(20)
    Donatello.penup()    
    Donatello.goto(-650, 250)
    Donatello.pendown()
    Donatello.right(285)
    components_of_wave()


def components_of_wave() -> None:
    """To Separate my Wave Funtion into Two Components."""
    wave_counter: int = 0
    conditional: bool = False
    while wave_counter < 12 and conditional is False: 
        if wave_counter % 2 == 0: 
            max_of_wave()
        elif wave_counter == 12: 
            conditional = True
        else:
            min_of_wave()
        wave_counter += 1
        

def max_of_wave() -> None:
    """To Separate My Wave Function and to Create the Top of the Wave."""
    wave_number: int = 0 
    while wave_number < 150: 
        Donatello.right(1)
        Donatello.forward(1)
        wave_number += 1 


def min_of_wave() -> None: 
    """To Separate My Wave Function and to Create the Bottom of the Wave."""
    wave_number = 0  
    while wave_number < 150: 
        Donatello.left(1)
        Donatello.forward(1)
        wave_number += 1


def head(x: float, y: float) -> None:
    """To Create the Head of the Fish."""
    Donatello.pensize(5)
    Donatello.penup()
    Donatello.goto(x, y) 
    Donatello.pendown()
    Donatello.color(255, 0, 0)
    Donatello.begin_fill()
    counter_curve: int = 0
    while counter_curve < 245: 
        Donatello.forward(1)
        Donatello.right(1)
        counter_curve += 1 


def tail() -> None:
    """To Create the Tail of the Fish."""
    Donatello.left(340)
    Donatello.forward(200)
    Donatello.right(230)
    Donatello.forward(140)
    Donatello.right(231)
    Donatello.forward(170)
    Donatello.end_fill()


def fish(x: float, y: float) -> None:
    """To Call Functions together to Create the Fish.""" 
    head(x, y)
    tail()


def main() -> None: 
    """The entrypoint of my scene."""
    wave()
    fish(-110.0, -200.0)
    fish(200.0, -200.0)
    fish(100.0, 150.0)
    fish(-450, -100)


if __name__ == "__main__": 
    main()
    done()