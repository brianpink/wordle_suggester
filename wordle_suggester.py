#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
#
#	wordle_suggester.py
#
#	brianpink@mac.com 
#
#	made: 5/8/22
#
#	my script to search for words when I can't find the answer
#	the backup puzzle for the main puzzle, is to take the available
#	clues, and make this script give me hints
#
#

print('\n-- - - SOF -- - -\n')

# INSERT CODE HERE

import time
import sys

### FUNCTIONS

def good_bye(start):
	end = time.time()
	ticktock = round(end - start, 4)
	print(f'---   --  -\n{ticktock} seconds to process.\n---   --  -\n')

### THE GUTS

def main():

	#filename = 'english-words-master/words.txt'
	filename = 'five_letter_words.txt'
	#filename = 'sample_words.txt'
	
	# TIMER INFO
	
	start = time.time()

	''' open the file and cycle through '''
	with open(filename) as f:
		word_list = f.readlines()
		word_list = [word.rstrip() for word in word_list]
	f.close()

	
	#clues = input('tell me what you got: ')
	#bad_clues = input('any you no have: ')

	while True:
		'''
			take our clue input and come back with a list.
		'''
		print('ok start with positives. needs to look like ..x.x')
		clue_str = input('tell me what you got: ')
		if clue_str == 'q':
			good_bye(start)
			sys.exit('QUITTING. HAVE A GREAT DAY AND GOD BLESS AMERICA.')
			
		bad_clue_str = input('list all that are no matchie: ')
		if bad_clue_str == 'q':
			good_bye(start)
			sys.exit('QUITTING. HAVE A GREAT DAY AND GOD BLESS AMERICA.')
		
		#clue_str = 'oce..'
		clues = list(clue_str)
		if len(clues) < 5:
			sys.exit('NOT ENOUGH CLUES. STOPPING.')
		
		#bad_clue_str = 'wltkz'
		bad_clues = list(bad_clue_str)

		for c in clues:
			if c in bad_clues:
				sys.exit('BAD CLUE IN GOOD CLUE. COME ON NOW.')
	
		print('\nlooking...\n')
	
		# CLEAN THE LIST
			
		clean_list = word_list.copy()
	
		total = len(clean_list)
		print(f'started with {total} words.')
	
		for clue in clues:
			if clue != '.':
				this_list = [x for x in clean_list if clue in x]	
				clean_list = this_list.copy()
	
		total = len(clean_list)
		print(f'next at {total} words.')
		
		for clue in bad_clues:
			this_list = [x for x in clean_list if clue not in x]	
			clean_list = this_list.copy()
		
		# LIST SEEMS CLEANED, BUT NOT ACCOUNTING FOR CLUE POSITION.
	
		even_cleaner_list = []
	
		for word in clean_list:
	
			tmp_word = list(word)
			word_spot = clean_list.index(word)
		
			x = 0
			y = len(word)
		
			while x < y:
				if clue != '.':
					if tmp_word[x] == clues[x]:
						tmp_word[x] = clues[x].upper()
				x += 1
			
			even_cleaner_list.append(''.join(tmp_word))
			#clean_list[word_spot] = ''.join(tmp_word)
		#
		#	RESULTS
		#
		
		total = len(even_cleaner_list)
		print(f'returned {total} words.')
		
		if total < 25:		
			for x in even_cleaner_list:
				print(x)
		else:
			print('more than 25 results. try again with more clues.')
	
		print(f'with clues: {"".join(clues)}')
		print(f'and bad_clues: {"".join(bad_clues)}')
	
		good_bye(start)
	

if __name__ == '__main__': main()
	
# END EXERCISE

print( "\n- -- EOF. -- -\n" )


#     
# EOF