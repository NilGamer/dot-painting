# import colorgram
#
# colors = colorgram.extract('spots.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     rgb = color.rgb
#     rgb_colors.append((rgb.r, rgb.g, rgb.b))
#
# print(rgb_colors)
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
colors_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
               (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122),
               (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
               (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95),
               (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]
# colors = ['red','green','blue']
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
row_start_pos = tim.ycor()
col_start_pos = tim.xcor()

for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)

    tim.setx(col_start_pos)
    tim.sety(row_start_pos + 50)
    row_start_pos = row_start_pos + 50

screen = turtle.Screen()
screen.exitonclick()
