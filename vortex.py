# 선으로 복잡한 무늬를 그리기

import turtle as t

t.shape('triangle') 
t.speed('fastest')
for i in range(300):
    t.fd(i)
    t.right(91)     #91도 오른쪽으로 회전
