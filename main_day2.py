with open('input_file_day2.txt') as my_file:
	my_input_list = list(map(int, my_file.read().split(',')))

my_first_list = my_input_list.copy()

def intcode(sequence):
 	counter = 0
 	while sequence[counter] != 99:
 		if sequence[counter] == 1: 
 			sequence[sequence[counter + 3]] = sequence[sequence[counter + 1]] + sequence[sequence[counter + 2]]
 		elif sequence[counter] == 2:
 	 		sequence[sequence[counter + 3]] = sequence[sequence[counter + 1]] * sequence[sequence[counter + 2]]
 		counter += 4
 	return sequence[0]

my_first_list[1] = 12
my_first_list[2] = 2

print(intcode(my_first_list)) 

#part two

for i in range(100):
	for j in range(100):
		my_second_list = my_input_list.copy()
		my_second_list[1] = i
		my_second_list[2] = j
		if intcode(my_second_list) == 19690720:
		 	print(100*i+j)
			
 			


