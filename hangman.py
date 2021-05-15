import string
import random

def LoadWords():
	inFile = open('words.txt', 'r')
	line = inFile.readline()
	wordlist = line.split()
	print(" ", len(wordlist), "words loaded.")
	return wordlist

def chooseWord(wordlist):
	return random.choice(wordlist)

def isWordGuessed(secretWord, GuessList):
	bingo = True
	for item in secretWord:
		if item not in GuessList:
			bingo = False
			break
	return bingo

def getGuessedWord(secretWord, GuessList):
	printOutGuessedWord = ''
	for letter in secretWord:
		if letter in GuessList:
			printOutGuessedWord += letter
		else:
			printOutGuessedWord += '_ '
	return printOutGuessedWord

def getAvailabLetters(GuessList):
	AtoZ = list(string.ascii_lowercase)
	AZ = ""
	for letter in GuessList:
		if letter in AtoZ:
			AtoZ.remove(letter)
	for letter in AtoZ:
		AZ += letter
	return AZ

passed = False
WordList = LoadWords()
secretWord = chooseWord(WordList).lower()
print("SecrectWord = ", secretWord)
GuessList = []


while not passed:
	GuessList.append(input("Guess: "))
	passed = isWordGuessed(secretWord, GuessList)
	if not passed:
		print(getGuessedWord(secretWord, GuessList))
		print(getAvailabLetters(GuessList))
		print("********************")

print(secretWord)
print("Corrent Answer")
