from input_variables import a ,b
from subtract_module import subtract
from multiply_module import multuply
from addition_module import addition

subtraction = subtract(a,b)
multiplication = multuply(a,b)
sum = addition(a,b)

print("addition of two number is  : " , sum)
print("addition of the both of the results of subtration and multiplication is : " , subtraction + multiplication)

