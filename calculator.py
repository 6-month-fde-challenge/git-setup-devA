from input_variables import a ,b
from subtract_module import subtract
from multiply_module import multuply
from addition_module import addition
from division_module import division

subtraction = subtract(a,b)
multiplication = multuply(a,b)
sum = addition(a,b)
div = division(a,b)

print("addition of two number is  : " , sum)
print("Division of two number is  : " , div)
print("addition of the both of the results of subtration and multiplication is : " , subtraction + multiplication)

