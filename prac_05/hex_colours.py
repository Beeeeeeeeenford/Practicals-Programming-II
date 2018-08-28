"""
CP1404/CP5632 Practical
Colour names in a dictionary
Look up hexadecimal code
"""

COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "BlueViolet": "#8a2be2", "CadetBlue": "#5f9ea0", "CornflowerBlue": "#6495ed",
                "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400", "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc",
                "ForestGreen": "#228b22", "GreenYellow": "#adff2f"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")
