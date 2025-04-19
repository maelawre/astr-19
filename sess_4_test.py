from session_4_prompt import favAnimal

def main():
	my_fav = favAnimal("Ladybug",[0], [6], [2], False, False)

	print(my_fav.name)
	print(my_fav.arms)
	print(my_fav.legs)
	print(my_fav.eyes)

	my_fav.fur_and_tail()


if __name__ == '__main__':
	main()