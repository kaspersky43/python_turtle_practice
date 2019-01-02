import turtle as t

t.shape('turtle')

#t.circle(120) #반지름 120

n = 60 #원 갯수
t.speed('fastest')
for i in range(n):
    t.circle(120)
    t.right(360/n) #오른쪽으로 6도 회전
