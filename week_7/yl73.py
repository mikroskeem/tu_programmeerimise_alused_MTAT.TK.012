from easygui import buttonbox, integerbox, msgbox

first = integerbox(msg = "Sisestage esimene täisarv lõigus 1-10:")
second = integerbox(msg = "Sisestage teine täisarv lõigus 1-10:")
action = buttonbox(msg = "Valige tehe:", choices = ["+", "-", "*"])

result = None
if action == "+":
    result = first + second
elif action == "-":
    result = first - second
elif action == "*":
    result = first * second

msgbox(msg = "Tehte tulemus on {}.".format(result))
