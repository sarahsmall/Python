# @author sarah small
# @date 17/01/19
# @module AC31007



import sys

def main():

	#get user input
	words = input("please enter a string: ")
	words = words.split()

	#find the longest word in a string
	longest_word =  max(words, key=len)
	max_len = (len(longest_word)+1)


	#prints top border of aestrisk
	for x in range(len(longest_word)+3):
		sys.stdout.write('*')
		

	print("")
	for x in words:
		#for words less than the longest word add padding
		if len(x) < max_len:
			new_len = max_len - len(x)
			sys.stdout.write("*")
			sys.stdout.write(x)
			for x in range(0,new_len):
				sys.stdout.write(" ")
			sys.stdout.write("*")
			sys.stdout.write("\n")
		else:
			sys.stdout.write("*")
			sys.stdout.write(x)
			sys.stdout.write("*")
			sys.stdout.write("\n")

	#prints bottom border of aestrisk
	for x in range(len(longest_word)+3):
		sys.stdout.write('*')
	print("\n")


main()