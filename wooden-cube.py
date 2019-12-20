
#IF the direction is "" 
		#IF dimemsions of the new coordinates are 1<= d <= 3
			#IF new spaces are not in the old key values.  
				#The immediate next step CANNOT go the opposite direction
				#Add keyvalue ("Direction", co,or,dinates) 
				#add the new spaces occupied by new direction 
sol = {(("start", 1,1,1,),):{(1,1,1),}}
link_list = [2,2,2,2,1,1,1,2,2,1,1,2,1,2,1,1,2]
#link_list=[2,2,2,2,1]
position_dir = {"+x", "-x", "+y", "-y", "+z", "-z"}		
for link_length in link_list:
	sol_copy = sol.copy()

	for current_pose in sol_copy: 
		temp_dir = position_dir.copy()
		current_dir = current_pose[-1][0] 
		if  current_dir == "+x":
			temp_dir.remove("+x")
			temp_dir.remove("-x")
		elif current_dir == "-x":
			temp_dir.remove("+x")
			temp_dir.remove("-x")
		elif current_dir == "+y":
			temp_dir.remove("+y")
			temp_dir.remove("-y")
		elif current_dir == "-y":
			temp_dir.remove("+y")
			temp_dir.remove("-y")
		elif current_dir == "+z":
			temp_dir.remove("+z")
			temp_dir.remove("-z")
		elif current_dir == "-z":
			temp_dir.remove("+z")
			temp_dir.remove("-z")

		for position in temp_dir:
			key_value = sol_copy[current_pose].copy()
			temp_x = current_pose[-1][1]
			temp_y = current_pose[-1][2]
			temp_z = current_pose[-1][3]
			
			if position == "+x":
				for i in range(1, link_length + 1):
					temp_x += 1
					coordinate = (temp_x, temp_y, temp_z)
					if 1 <= temp_x <= 3 and coordinate not in key_value:
						key_value.add(coordinate)
						successful = True
					else:
						successful = False 
				if successful: 
					new_start = (("+x", temp_x, temp_y, temp_z),)
					new_key = current_pose + new_start
					sol[new_key] = key_value

	

			elif position == "-x":
				for i in range(1, link_length + 1):
					temp_x -= 1
					coordinate = (temp_x, temp_y, temp_z)

					if 1 <= temp_x <= 3 and coordinate not in key_value:
						key_value.add(coordinate)
						successful = True
					else: 
						successful = False 
			
				if successful: 
					new_start = (("-x", temp_x, temp_y, temp_z),)
					new_key = current_pose + new_start
					sol[new_key] = key_value
			

			elif position == "+y":
				for i in range(1, link_length + 1):
					temp_y += 1
					coordinate = (temp_x, temp_y, temp_z)
					if 1 <= temp_y <= 3 and coordinate not in key_value:
						key_value.add(coordinate)
						successful = True
					else:
						successful = False
						break 
				if successful: 
					new_start = (("+y", temp_x, temp_y, temp_z),)
					new_key = current_pose + new_start
					sol[new_key] = key_value

			
			elif position == "-y":
				#raw_input()
				#print("this is the key value before", key_value)
				for i in range(1, link_length + 1):
					temp_y -= 1
					coordinate = (temp_x, temp_y, temp_z)
		
					if 1 <= temp_y <= 3 and coordinate not in key_value:
						key_value.add(coordinate)
						successful = True
					else: 
						successful = False 
						break
	
				if successful:
					new_start = (("-y", temp_x, temp_y, temp_z),)
					new_key = current_pose + new_start
					sol[new_key] = key_value


			elif position == "+z":
				for i in range(1, link_length + 1):
					temp_z += 1
					coordinate = (temp_x, temp_y, temp_z)

					if 1 <= temp_z <= 3 and coordinate not in key_value:
						key_value.add(coordinate)
						successful = True
					else: 
						successful = False 
						break
				if successful: 
					new_start = (("+z", temp_x, temp_y, temp_z),)
					new_key = current_pose + new_start
					sol[new_key] = key_value


			elif position == "-z":
				for i in range(1, link_length + 1):

					temp_z -= 1
					coordinate = (temp_x, temp_y, temp_z)
					if 1 <= temp_z <= 3 and coordinate not in key_value:
						key_value.add(coordinate)
						successful = True
					else: 
						successful = False 
						break
				if successful: 
					new_start = (("-z", temp_x, temp_y, temp_z),)
					new_key = current_pose + new_start
					sol[new_key] = key_value
				
		sol.pop(current_pose)


for key in sol:
	for k in key:
		print(k[0])
	raw_input()

#print (len(sol))

