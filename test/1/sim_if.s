number = 10
param @@HELLO@@
call(cout, 1)
param number
param @@number is equal to @@
call(cout, 2)

t1 = number > 0

ifFalse t1 goto L1

t2 = number * 100
number = t2
L1:
param @@ Multiplied number by 100 @@
call(cout, 1)
