from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.free_space as free_space

def calculate(grid, matrix, dicta, dictb, dictc):
	total_score = 0

	free_space.calculate_all()
	for i in dicta:
		score = matrix.score(dicta[i], info.scale, info.house_e_value, info.house_e_free, info.house_e_increment)
		if score == 1:
			return 1
		total_score = total_score + score

	for i in dictb:
		score = matrix.score(dictb[i], info.scale, info.house_b_value, info.house_b_free, info.house_b_increment)
		total_score = total_score + score
		if score == 1:
			return 1

	for i in dictc:
		score = matrix.score(dictc[i], info.scale, info.house_m_value, info.house_m_free, info.house_m_increment)
		total_score = total_score + score
		if score == 1:
			return 1

	return(total_score)
