abc = 76
param @@HELLO@@
call(cout, 1)
number = 10
param number
param @@Local variable is  @@
call(cout, 2)
param abc
param @@Global variable is @@
call(cout, 2)

t1 = number >= 0

ifFalse t1 goto L1

t2 = 10 * 5

t3 = number + t2

t4 = abc / number

t5 = t3 + t4
number = t5
goto L2
L1:
number = 0

L2:
param @@ This line is always printed @@
call(cout, 1)
