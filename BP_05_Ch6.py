#기초파이썬 6장 연습문제 터틀그래픽


7. #다음 그래픽과 반복을 사용하여 눈 모양을 그려보자.

import turtle
 
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.lt(90)
 
for i in range (6):
    t.fd(100); t.fd(-30); t.lt(60); t.fd(30); t.fd(-30)
    t.rt(120); t.fd(30); t.fd(-30); t.lt(60); t.fd(-70); t.lt(60)
t.screen.exitonclick()
    
    
8. #우리는 이번 장에서 터틀 그래픽으로 별을 그려보았다. 
   #이 코드를 응용하여서 다음과 같이 10개의 별을 그리는 프로그램을 작성하라. 별들은 시작 각도가 약간씩 다르다.
   
import turtle
 
t = turtle.Turtle()
t.color("red")
 
for i in range(10):
    for i in range(1,6):
        t.lt(144)
        t.fd(200)
    t.lt(10)
t.screen.exitonclick()


9. #반복과 난수를 함께 사용하면 화면에 랜덤한 원을 그릴 수 있다. 
   #화면에 10개의 랜덤한 원을 그리는 프로그램을 작성하라. 원의 중심과 반지름이 모두 난수이어야 한다.
   
import random as rd
import turtle
 
t = turtle.Turtle()
t.shape("turtle")
 
for i in range(10):
    x=rd.randint(-150,150)
    y=rd.randint(-150,150)
    r=rd.randint(1,100)
 
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(r)
t.screen.exitonclick()


10. #다음과 같이 거북이를 왕복 달리기시키는 프로그램을 작성해보자.

import turtle
 
t = turtle.Turtle()
t.shape("turtle")
 
for i in range(5):
    t.fd(200)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.fd(20)
    t.lt(90)
t.screen.exitonclick()


11. #다음의 터틀 그래픽 프로그램을 분석해보자. 학습하지 않은 함수가 있다면 인터넷에서 조사하여 보자.

import turtle
 
t = turtle.Turtle()
t.shape("turtle")
t.color("red", "yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos())< 1:
        break
t.end_fill()
t.screen.exitonclick()


12. #터틀 그래픽과 반복을 사용하여 싸인(sine) 그래프를 그려보자. 거북이를 싸인값에 따라서 움직이면 된다.

import turtle
import math
 
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
 
for i in range(360):
    sine=math.sin(math.pi*i/180)
    print(sine)
    t.goto(i,sine*100)
t.screen.exitonclick()