
t1 = 3 * 4

t2 = t1 + 5
globaal = t2
globaal = 0
i = 10

t3 = i < 4

ifFalse t3 goto L1

t4 = 1 + 2
k = t4
goto L2
L1:

t5 = i - 1
i = t5

L2:

t6 = i >= 0

ifFalse t6 goto L3

t7 = 3 + 4

t8 = t7 + 5
m = t8

t9 = m > 30

ifFalse t9 goto L5

t10 = i - 5
i = t10
goto L6
L5:

t11 = i + 1
i = t11

L6:
goto L4
L3:

t12 = 222 + 333


L4:

t13 = 3 + 4
kl = t13

t14 = i == 30

ifFalse t14 goto L7
i = 15
L7:
