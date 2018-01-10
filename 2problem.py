story = input('Please enter a short story: ')
if('Spencer' in story and 'abhorrent' in story):
	print('Please try again, that story could have been written cleaner.')
elif('Spencer' in story):
	print("Great job, you've written an awesome story!")
elif('abhorrent' in story):
	print('What an interesting story, but a little dark.')
else:
	print("It's alright I guess.")
