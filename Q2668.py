# Q2668 number selection


N = int(input())
number_table = []
number_table.append(0)

selected_numberlist = []
total_selected_number = 0

for i in range(0,N):
	number = int(input())
	number_table.append(number)
	

for i in range(1,N+1):
	# dfs()
	next_node = i
	current_node = i
	visited = []
	in_loop = False
	while True:
		next_node = number_table[current_node]
		
		# if this node makes cycle(return to start node) then satisfies
		if next_node == i:
			total_selected_number += 1
			selected_numberlist.append(i)
			break
		
		if i == number_table[current_node]:
			break
		
		
		for idx in range(0,len(visited)):
			if next_node == visited[idx]:
				in_loop = True
				break
				
		if in_loop == True:
			break
			
		current_node = next_node	
		visited.append(current_node)


print(total_selected_number)
for i in range(0,len(selected_numberlist)):
	print(str(selected_numberlist[i]))
	
	
