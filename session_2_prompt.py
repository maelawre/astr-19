#define variables for the floating point numbers
x = 1.0
y = 5.0
a = x + y

#define variable for the integers
w = 2
z = 8
b = z - w

#define variable for product of float and in
c = x * w 
def sumOfFloats(): 
	print(f"1.0 + 2.0 =   {a}")
	print(f"This is a {type(a)}")

def differenceOfIntegers():
	print(f"8 - 2 =  {b}")
	print(f"This is a { type(b)}")

def productOfBoth():
	print(f"1.0 x 2 =  {c}")
	print(f"This is a {type(c)}")

def main(): 
	sumOfFloats()
	differenceOfIntegers()
	productOfBoth()

if __name__ == '__main__':
	main()