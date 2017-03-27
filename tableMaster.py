from microbit import *
from random import randint

# Write your code here :-)
# display.scroll('144', wait=False, loop=True)

twelve = Image("09099\n"
               "99009\n"
               "09099\n"
               "09090\n"
               "09099")

eleven = Image("09009\n"
               "99099\n"
               "09009\n"
               "09009\n"
               "09009")

ten = Image("09099\n"
            "99099\n"
            "09099\n"
            "09099\n"
            "09099")

nine = Image("09990\n"
             "09090\n"
             "09990\n"
             "00090\n"
             "00090")

eight = Image("09990\n"
              "09090\n"
              "09990\n"
              "09090\n"
              "09990")

seven = Image("09990\n"
              "00090\n"
              "00900\n"
              "09000\n"
              "09000")

six = Image("09990\n"
            "09000\n"
            "09990\n"
            "09090\n"
            "09990")

five = Image("09990\n"
             "09000\n"
             "09990\n"
             "00090\n"
             "09990")

four = Image("09000\n"
             "09090\n"
             "09990\n"
             "00090\n"
             "00090")

three = Image("09990\n"
              "00090\n"
              "09990\n"
              "00090\n"
              "09990")

two = Image("09990\n"
            "00090\n"
            "09990\n"
            "09000\n"
            "09990")

one = Image("00090\n"
            "00990\n"
            "00090\n"
            "00090\n"
            "00090")

times = Image("00000\n"
              "09090\n"
              "00900\n"
              "09090\n"
              "00000")

numbers = [0, one, two, three, four, five, six,
           seven, eight, nine, ten, eleven, twelve]

# B - Choose table, iterate sequentially

# A - Select, start

# A - New table

# B - Show answer

# (Reset - start again)

currentTable = 1
debounce = 180  # A good debounce


def ask_question(a, b):
    display.show(numbers[a])
    sleep(1000)
    display.show(times)
    sleep(500)
    display.show(numbers[b])
    sleep(1200)
    display.clear()
    sleep(300)


display.show(numbers[currentTable])

while True:
    if button_a.is_pressed():
        if currentTable >= 12:
            currentTable = 1
        else:
            currentTable += 1

    display.show(numbers[currentTable])
    sleep(debounce)  # A good debounce value

    if button_b.is_pressed():
        multiple = randint(2, 12)
        display.clear()
        sleep(400)
        display.show(Image.HAPPY)
        sleep(700)
        display.clear()
        sleep(400)        
        while True:  # Begin inner game loop
            ask_question(currentTable, multiple)
            # Loop listen for button presses (repeat, or answer & new)
            while True:
                if button_a.is_pressed():
                    # Repeat answer
                    break
                if button_b.is_pressed():
                    # Display answer and break for displaying it
                    answer = currentTable * multiple
                    display.scroll(str(answer))
                    sleep(200)
                    multiple = randint(2, 12)
                    break
