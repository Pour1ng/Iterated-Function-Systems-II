"""SYST/CYSE 130
Pb4: Iterated Function Systems II
Author: Joshua R Obee
"""

# import statements
import turtle as t
import random
import json
import os

probabilities = [.33, .33, .34]
coefficients = [[.50, .00, .00, .00, .50, .00], [.50, .00, .50, .00, .50, .00], [.50, .00, .25, .00, .50, .433]]

script_dir = os.path.dirname(__file__)  # Directory of the script
data_path = os.path.join(script_dir, 'data.json')

    
def get_data():
    with open(data_path) as f:
        data = json.load(f)
    return data


def generate_point(x, y, coefficients):
    x1 = coefficients[0] * x + coefficients[1] * y + coefficients[2]
    y1 = coefficients[3] * x + coefficients[4] * y + coefficients[5]
    return x1, y1


def random_select(probabilities, coefficients):
    a = random.random()
    for p, c in zip(probabilities, coefficients):
        if a < p:
            return c
        a -= p
    return coefficients[-1]


def initialize():
    t.clear()
    t.setworldcoordinates(0, 0, 1, 1)
    t.tracer(10000)
    t.speed(0)
    t.hideturtle()


def plot(x, y):
    t.penup()
    t.goto(x, y)
    t.dot(3)


def draw(probabilities, coefficients, n):
    x, y = 0, 0
    for i in range(n):
        c = random_select(probabilities, coefficients)
        x, y = generate_point(x, y, c)
        plot(x, y)


# main
while True:
    try:
        n = int(input("Enter the number of iterations: "))
        option = int(input("Enter drawing option (1-3) to draw a cool image: "))
        if n < 50000:
            print("Hmm...that doesn't seem quite right...")
            print("Hint: Try inputting 50000 or more for the number of iterations.")
        if option < 1 or option > 3:
            raise ValueError()
        data = get_data()
        if option == 1:
            probabilities = data['p0']
            coefficients = data['c0']
        elif option == 2:
            probabilities = data['p1']
            coefficients = data['c1']
        else:
            probabilities = data['p2']
            coefficients = data['c2']
        initialize()
        draw(probabilities, coefficients, n)
        t.update()
    except ValueError:
        print("I think you entered an invalid option entry. Try again?")
        print("Tip: If trying to end session, close window with the created drawing.")
        t.done()
