## Correctly placed (green) letters ##
first_letter = ''
second_letter = 'a'
third_letter = ''
fourth_letter = 's'
fifth_letter = 'e'

## Incorrectly placed (gold) letters ##
required_letters = ['']

## Incorrect (gray) letters ##
excluded_letters = ['r','o','l']


## Don't change things below here!
########################################################

freq_dict = {'s': 3033/28785, 'e': 3009/28785,'a': 2348/28785, 'o': 1915/28785, 'r': 1910/28785, 'i': 1592/28785, 'l': 1586/28785, 't': 1585/28785, 'n': 1285/28785, 'd': 1181/28785, 'u': 1089/28785, 'c': 964/28785, 'p': 955/28785, 'y': 886/28785, 'm': 843/28785,'h': 814/28785, 'b': 715/28785, 'g': 679/28785, 'k': 596/28785, 'f': 561/28785, 'w': 505/28785, 'v': 318/28785, 'x': 139/28785, 'z': 135/28785, 'j': 89/28785, 'q': 53/28785}

ordered_letters = [first_letter, second_letter, third_letter, fourth_letter, fifth_letter]
placed_letters_index = [i for i, j in enumerate(ordered_letters) if j != '']

word_dict = {}

def position_checker(j,k):			
	if ordered_letters[k] == j[k]:
		return True
	else:
		return False

with open('word-list.txt') as f:
	text = f.readlines()
	text = [ele for ele in text if all(ch not in ele for ch in excluded_letters)]	
	text = [ele for ele in text if all(ch in ele for ch in required_letters)]
			
	for i in text:
		word_sum = 0
		true_false_list = []
		
		i = i.strip()
		j = list(i)
		
		for k in placed_letters_index:
			boolean = position_checker(j,k)
			true_false_list.append(boolean)

		if sum(true_false_list) == len(true_false_list):
			for letter in j:
				word_sum += freq_dict[letter]

			word_dict[i] = word_sum
					
for w in sorted(word_dict, key=word_dict.get, reverse=True):
    print(w, word_dict[w])