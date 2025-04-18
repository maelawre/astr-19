#define function f(x)

def f(x):
	return x**3 +8

#define main function

def main():
	result = f(9)
	print(result)
	if result >= 27: 
		print("YAY!")

if __name__ == '__main__':
	main()