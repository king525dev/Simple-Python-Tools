# Import the turtle library for
# drawing the required curve
import turtle as tt

# Set the background color as black,
# pensize as 2 and speed of drawing
# curve as 10(relative)
tt.Screen().bgcolor('black')
tt.pensize(2)
tt.speed(0)
tt.hideturtle()

# Iterate six times in total
for i in range(6):

	# Choose your color combination
	for color in ('red', 'magenta', 'blue',
				'cyan', 'green', 'white',
				'yellow'):
		tt.color(color)

		# Draw a circle of chosen size, 100 here
		tt.circle(100)

		# Move 10 pixels left to draw another circle
		tt.left(10)

	# Hide the cursor(or turtle) which drew the circle
	tt.hideturtle()

tt.clear()

def draw_attractive_design2():
     colors = ["red", "orange", "yellow", "green", "blue", "purple"]
     pen = tt.Turtle()
     pen.hideturtle()
     tt.hideturtle()
     pen.speed(10)
     tt.bgcolor("black")  
     pen.pensize(2)

     initial_size = 30  

     for i in range(1000):
          pen.color(colors[i % 6])
          pen.forward(initial_size + i)
          pen.left(59)

     pen.hideturtle()


draw_attractive_design2()

tt.done()