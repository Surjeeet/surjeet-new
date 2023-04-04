
RED = "red"
BLUE = "blue"
YELLOW = "yellow"


color1 = input("Enter the first primary color: ")
color2 = input("Enter the second primary color: ")


if color1 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color1")
else:
    if color2 not in [RED, BLUE, YELLOW]:
        print("Error: Invalid Color2")
    else:
        if color1 == color2:
            print("Error: The two colors you entered are same")
        else:
            # mixing primary colors
            if color1 == RED:
                if color2 == BLUE:
                    secondary_color = "PURPLE"
                else:
                    secondary_color = "ORANGE"
            elif color1 == BLUE:
                if color2 == RED:
                    secondary_color = "PURPLE"
                else:
                    secondary_color = "GREEN"
            elif color1 == YELLOW:
                if color2 == RED:
                    secondary_color = "ORANGE"
                else:
                    secondary_color = "GREEN"
            
            
            print("The new secondary color is:", secondary_color)
