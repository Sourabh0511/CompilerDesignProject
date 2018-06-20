x = 10
y = 15
i = 0

t1 = 100 * 500
j = t1
L1:
t2 = x > 0

ifFalse t2 goto L2

t3 = x - 1
x = t3

t4 = j + 1
j = t4
L3:
t5 = y > 0

ifFalse t5 goto L4

t6 = i + 1
i = t6
m = 19

t7 = m * i
k = t7

t8 = k + 1
k = t8
goto L3
L4:
goto L1
L2:
param @@ THANK YOU @@
call(cout, 1)
