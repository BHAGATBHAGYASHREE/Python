import mymodule as mm
from mymodule import Addition
a=Addition()
a.add(3,4)
from mymodule import Subtraction
a=Subtraction()
a.sub(2,1)
from mymodule import Div
a=Div()
a.multi(10,5)
a.div(10,5)
print("module name & second",__name__)
mm.add(9,1)