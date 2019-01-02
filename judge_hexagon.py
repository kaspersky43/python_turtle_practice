#별 그리기 문제 

import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fast')

for i in range(n):
    t.fd(line)
    t.rt(2*360/n)
    t.fd(line)
    t.lt(360/n)
