"""SYST/CYSE 130
Pb4: Iterated Function Systems II
Author: Joshua R Obee
Purpose: This program creates fractal-style 
images using Iterated Function Systems (IFS). 
Users can choose the number of iterations 
and a drawing option to generate unique, 
visually interesting patterns.
"""

# Import statements
import turtle as t
import random
import json
import os

# Default probabilities and coefficients for transformations
probabilities = [.33, .33, .34]
coefficients = [[.50, .00, .00, .00, .50, .00], [.50, .00, .50, .00, .50, .00], [.50, .00, .25, .00, .50, .433]]

# Construct the file path for the JSON data file
script_dir = os.path.dirname(__file__)  # Directory of the script
data_path = os.path.join(script_dir, 'data.json')

# Function to load transformation data from a JSON file    
def get_data():
    with open(data_path) as f:
        data = json.load(f)
    return data

# Function to generate a new point based on the current point and transformation coefficients
def generate_point(x, y, coefficients):
    x1 = coefficients[0] * x + coefficients[1] * y + coefficients[2]
    y1 = coefficients[3] * x + coefficients[4] * y + coefficients[5]
    return x1, y1

# Function to randomly select a transformation based on probabilities
def random_select(probabilities, coefficients):
    a = random.random()
    for p, c in zip(probabilities, coefficients):
        if a < p:
            return c
        a -= p
    return coefficients[-1]

# Function to initialize the Turtle graphics environment
def initialize():
    t.clear()
    t.setworldcoordinates(0, 0, 1, 1)
    t.tracer(10000)
    t.speed(0)
    t.hideturtle()

# Function to plot a point on the screen
def plot(x, y):
    t.penup()
    t.goto(x, y)
    t.dot(3)

# Function to draw the fractal pattern
def draw(probabilities, coefficients, n):
    x, y = 0, 0
    for i in range(n):
        c = random_select(probabilities, coefficients)
        x, y = generate_point(x, y, c)
        plot(x, y)


# Main loop to interact with the user
while True:
    try:
        # Prompt the user for the number of iterations
        n = int(input("Enter the number of iterations (For best results choose between 30000 and 65000): "))
        
        # Prompt the user to select a drawing option
        option = int(input("Enter drawing option (1-3) to draw a cool image: "))
        
        # Provide feedback if the input number of iterations is too low
        if n < 20000:
            print("Hmm...that doesn't seem quite right...")
            print("Hint: Try inputting 50000 for the number of iterations.")
            raise BaseException
        
        # Provide feedback if the input number of iterations is too high
        elif n > 80000:
            print("\nThat may be too much for your CPU. Try inputting a lower iteration value.")
            raise BaseException
        
        # Validate the drawing option
        elif n >= 20000 and n <= 80000:
            if n > 65000:
                print("Drawing may take a 1-2 minutes to complete...")
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
            
            # Initialize the Turtle graphics environment and draw the fractal
            initialize()
            print("\nLook in taskbar below for new tab with drawing --->")
            draw(probabilities, coefficients, n)

            # Update the screen with the drawn points
            t.update()

        # Prompt the user to redraw or quit
        if t.textinput('Redraw', 'Enter Yes or Y to draw new image; Enter any other key to quit.') in ['Yes', 'yes', 'Y', 'y']:
            print("Loading new prompt...\n")
        else:
            # Exit the program
            print("\nThank you for your time!")
            t.hideturtle()
            t.done()
            break
            
    except ValueError: # Handle invalid input
        print("I think you entered an invalid option entry. Try again?")
    except BaseException:
        print("")
    
        
