from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.free_space as free_space

def calculate(grid, matrix):
	total_score = 0

	free_space.calculate_all()
	#free_space.calculate_free_space_eengezinswoning('houses_e')
	for i in hd.houses_e:
		#matrix.free_space(grid, hd.houses_e[i], hd.houses_e[i].id, info.house_e_length, info.house_e_width)
		score = matrix.score(hd.houses_e[i], info.scale, info.house_e_value, info.house_e_free, info.house_e_increment)
		if score == 1:
			return 1
		total_score = total_score + score
		# print("{} score: {}" .format(hd.houses_e[i].id, score))

	for i in hd.houses_b:
		#matrix.free_space(grid, hd.houses_b[i], hd.houses_b[i].id, info.house_b_length, info.house_b_width)
		score = matrix.score(hd.houses_b[i], info.scale, info.house_b_value, info.house_b_free, info.house_b_increment)
		total_score = total_score + score
		if score == 1:
			return 1
		# print("{} score: {}" .format(hd.houses_b[i].id, score))

	for i in hd.houses_m:
		#matrix.free_space(grid, hd.houses_m[i], hd.houses_m[i].id, info.house_m_length, info.house_m_width)
		score = matrix.score(hd.houses_m[i], info.scale, info.house_m_value, info.house_m_free, info.house_m_increment)
		total_score = total_score + score
		if score == 1:
			return 1
		# print("{} score: {}" .format(hd.houses_m[i].id, score))

	# print("Total score: {}" .format(total_score))

	return(total_score)

def calculate_annealing(grid, matrix, dicta, dictb, dictc):
	total_score = 0

	free_space.calculate_all()
	#free_space.calculate_free_space_eengezinswoning('houses_e')
	for i in dicta:
		# matrix.free_space(grid, hd.houses_e[i], hd.houses_e[i].id, info.house_e_length, info.house_e_width)
		score = matrix.score(dicta[i], info.scale, info.house_e_value, info.house_e_free, info.house_e_increment)
		if score == 1:
			return 1
		total_score = total_score + score
		# print("{} score: {}" .format(hd.houses_e[i].id, score))

	for i in dictb:
		#matrix.free_space(grid, hd.houses_b[i], hd.houses_b[i].id, info.house_b_length, info.house_b_width)
		score = matrix.score(dictb[i], info.scale, info.house_b_value, info.house_b_free, info.house_b_increment)
		total_score = total_score + score
		if score == 1:
			return 1
		# print("{} score: {}" .format(hd.houses_b[i].id, score))

	for i in dictc:
		#matrix.free_space(grid, hd.houses_m[i], hd.houses_m[i].id, info.house_m_length, info.house_m_width)
		score = matrix.score(dictc[i], info.scale, info.house_m_value, info.house_m_free, info.house_m_increment)
		total_score = total_score + score
		if score == 1:
			return 1
		# print("{} score: {}" .format(hd.houses_m[i].id, score))

	# print("Total score: {}" .format(total_score))

	return(total_score)
