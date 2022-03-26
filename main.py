import random
# import os
import colour
import replit

gs = ["", "", "", "", "", ""]


# funkcja do spawdzania, czy wszystko działa
def check():
	n = 0
	g = ""
	l = ["grey", "grey", "grey", "grey", "grey"]
	for i in range(0, 5):
		if guess[i] in word:
			l[i] = "yellow"
			# kolorujemy literkę na żółto
			letter = colour.yellow + guess[i]

		if guess[i] == word[i]:
			# zmiana na zielono
			l[i] = "green"
			letter = colour.green + guess[i]

		if guess[i] != word[i] and guess[i] not in word:
			# szara literka - brakuje jej w słowie
			letter = colour.grey + guess[i]
		g = g + letter + colour.White

	gs[tries] = g
	for x in range(0,tries + 1):
		# wypisuje listę odgadnięć
		print(gs[n])
		n = n + 1
	if l == ["green", "green", "green", "green", "green"]:
		# jeśli wszystkie zielone to zwraca wygraną
		return True
			
n = 0

# pobierz słowa
file = open("wordList.txt", "r")
wordList = file.readlines()
word = wordList[random.randint(0, len(wordList)-1)].upper()

win = False
tries = 0
# upewniamy się, że słowo ma 5 liter
# - x amount of characters if too big
# replaces empty char slots with 'x'
for i in range(0,6):
	guess = str(input("Podaj słowo: ")).upper()
	while len(guess) != 5:
		if len(guess) < 5:
			guess = guess + "x"
		elif len(guess) > 5:
			guess = guess[:-1]
	replit.clear()
	# os.system('cls' if os.name == 'nt' else 'clear')
	if check() == True:
		win = True
		break
	n = n + 1
	tries = tries + 1

# sprawdzanie wygranej
if win == True:
	print(colour.Green + colour.bold + "\nUdało się!\n")
elif win == False:
	print(colour.Red + colour.bold + "\nPorażka...\nSzukane słowo to: {}".format(word))
