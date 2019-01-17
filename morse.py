import sys
def main():

	
	thisdict =	{
	  "a": ".-",
	  "b": "-...",
	  "c": "-.-.",
	  "d": "-..",
	  "e": ".",
	  "f": "..-.",
	  "g": "--.",
	  "h": "....",
	  "i": "..",
	  "j": ".---",
	  "k": "-.-",
	  "l": ".-..",
	  "m": "--",
	  "n": "-.",
	  "o": "---",
	  "p": ".--.",
	  "q": "--.-",
	  "r": ".-.",
	  "s": "...",
	  "t": "-",
	  "u": "..-",
	  "v": "...-",
	  "w": ".--",
	  "x": "-..-",
	  "y": "-.--",
	  "z": "--.."
	 

	}
	words = raw_input("please enter a string: ")
	words = words.split()

	for x in words:

		for i in x:
			sys.stdout.write(thisdict[i])
		sys.stdout.write(" ")

main()