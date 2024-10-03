import random

name = input("What is your name? ")
print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'Love']

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:

	# counts the number of times a user fails
	failed = 0

	# all characters from the input
	# word taking one at a time.
	for char in word:

		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")

			# for every failure 1 will be
			# incremented in failure
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("You Win")

		# this print the correct word
		print("The word is: ", word)
		break

	print()
	guess = input("guess a character:")

	
	guesses += guess

	
	if guess not in word:

		turns -= 1
		print("Wrong")
		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose")
