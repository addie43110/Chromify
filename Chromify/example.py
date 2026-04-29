from Chromify import Color, steps, gradient

def main():
    # Print text in a specific color
    red = Color("#FF0000")
    print("This text should be white.")
    print(f"Only {red("red")} should be {red("red")}")

    # Print text manually in a gradient using steps()
    yellow = Color("#FFEE00")
    green = Color("#51FF00")
    red_yel = steps(red, yellow, 10, style="color")
    yel_green = steps(yellow, green, 10, style="color")
    red_green = red_yel + yel_green

    s = ""
    for i in range(20):
        s+=f"{red_green[i](i)}"
    
    print("Gradient with 20 steps from red to yellow to green.")
    print("".join(s))

    # Print text in a gradient using gradient()
    robin_blue = Color("#83E5EB")
    royal_blue = Color("#1D2EA3")
    print(gradient(robin_blue, royal_blue, "This text was mading using gradient()."))


if __name__=="__main__":
    main()