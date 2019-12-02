with open('input_file_day2.txt') as my_file:
	my_input_list = list(map(int, my_file.read().split(',')))

def opcode(sequence):
 	counter = 0
 	while sequence[counter] != 99:
 		if sequence[counter] == 1: 
 			sequence[sequence[counter + 3]] = sequence[sequence[counter + 1]] + sequence[sequence[counter + 2]]
 		elif sequence[counter] == 2:
 	 		sequence[sequence[counter + 3]] = sequence[sequence[counter + 1]] * sequence[sequence[counter + 2]]
 		counter += 4
 	return sequence

my_input_list[1] = 12
my_input_list[2] = 2

print((opcode(my_input_list))[0]) 