import turtle

#Turtle set up
turtle.width(2)
turtle.speed(2)

#Starting on the left side of the page so that the graphic is centered
turtle.hideturtle()
turtle.penup()
turtle.goto(-60,0)
turtle.pendown()

#Red part of graphic
turtle.color('red')
turtle.rt(-150)
turtle.fd(60)
turtle.rt(100)
turtle.fd(110)
turtle.rt(100)
turtle.fd(60)


#Blue part of graphic
turtle.color('blue')
turtle.rt(-100)
turtle.fd(60)
turtle.rt(100)
turtle.fd(110)
turtle.rt(100)
turtle.fd(60)

#Keep graphic
turtle.done()