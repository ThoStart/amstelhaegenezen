from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.tk_export as tk_export
import library.score as score

def execute(matrix, grid):

	# before hill climbing algorithm
	total_score = score.calculate(grid, matrix)
	#tk_export.create(matrix, grid, (str(total_score) + " (before hill climbing)"))

	hc_data = []

	# swap E and B
	for i in hd.houses_e:
		for j in hd.houses_b:
			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_b[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new < total_score:
				hc_data.append(total_score)
				Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_b[j])
				total_score = score.calculate(grid, matrix)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

	# swap B and M
	for i in hd.houses_b:
		for j in hd.houses_m:
			Matrix.swap(matrix, grid, hd.houses_b[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new < total_score:
				hc_data.append(total_score)
				Matrix.swap(matrix, grid, hd.houses_b[i], hd.houses_m[j])
				total_score = score.calculate(grid, matrix)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

	# swap E and M
	for i in hd.houses_e:
		for j in hd.houses_m:
			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new < total_score:
				hc_data.append(total_score)
				Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_m[j])
				total_score = score.calculate(grid, matrix)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

	# after hill climbing algorithm
	print(hc_data)
	#tk_export.create(matrix, grid, (str(total_score) + " (after hill climbing)"))

	return hc_data
