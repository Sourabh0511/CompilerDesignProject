
t1 = 3 * 4

t2 = t1 + 5
globaal = t2
i = 10
j = 10
k = 10
param i
param j
param k
call(cout, 3)
i = 10
global_array[50]
i = 0
L1:
t3 = 2 < 10

ifFalse t3 goto L2

t4 = i < 4

ifFalse t4 goto L3

t5 = 1 + 2

goto L4
L3:
L5:
t6 = i > 10

ifFalse t6 goto L6

t7 = i - 1
i = t7
goto L5
L6:

t8 = i >= 0

ifFalse t8 goto L7

t9 = 3 + 4

t10 = t9 + 5

goto L8
L7:

t11 = 222 + 333

t12 = 8 * 40
global_array[t12] = 1

L8:

t13 = 3 + 4


L4:
goto L1
L2:
globaal = 4
