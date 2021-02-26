# Q1467 delete number

number = input()
to_delete = input()

def delete_number(number,to_delete):
	if not to_delete:
		return number
		
	target_number = to_delete[0]
	to_delete = to_delete[1:]
	max_result = 0
	
	for i in range(0,len(number)):
		if target_number == number[i]:
			temp_number = number[:i] + number[i+1:]
			
			result = int(delete_number(temp_number,to_delete))
			if result > max_result:
				max_result = result
			
	return max_result	


print(delete_number(number,to_delete))
