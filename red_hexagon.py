import turtle as t

n = 6 #6각형
t.shape('turtle')
t.color('red')
t.begin_fill() #색 영역 시작
for i in range(n):
    t.fd(100)
    t.right(360/n)
t.end_fill()  #색 영역 끝

