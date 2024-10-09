# L61
# Mac Weber-Hess & Serenity Schuler

def mood_color_star():

    def emotion_to_color(x):
        if x == "happy":
            return "goldenrod"
        elif x == "sad":
            return "dark slate grey"
        elif x == "sleepy":
            return "cornflower blue"
        elif x == "angry":
            return "maroon"
        else:
            print("Enter a valid emotion.")
            mood_color_star()

    emotion = input("Are you feeling happy, sad, sleepy, or angry?\n")
    color = emotion_to_color(emotion)

    import turtle

    ted = turtle.Turtle()
    ted.width(10)
    ted.speed(10)

    def draw_star(x):
        ted.color(x)
        for side in range(5):
            ted.forward(100)
            ted.right(144)

    draw_star(color)

mood_color_star()