from turtle import*
#ვხატავთ სახლს

width(4)
color("black")
begin_fill()
speed(5)
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
end_fill()
#უნდა დავხატოთ კარი

forward(100)
color("white")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

#დავხატოთ სახურავი

penup()
goto(0, 250)
pendown()
color("grey")
begin_fill()
left(120)
forward(150)
right(60)
forward(145)
end_fill()

exitonclick()