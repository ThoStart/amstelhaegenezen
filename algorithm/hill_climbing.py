from class_objects import House, Water, Matrix
import setup as info
import house_dictionary as hd
import tk_export
import score

def execute(matrix, grid):

	# before hill climbing algorithm
	total_score = score.calculate(grid, matrix)
	tk_export.create(matrix, grid, (str(total_score) + " (before hill climbing)"))

	hc_data = []

	# swap E and B
	for i in hd.houses_e:
		for j in hd.houses_b:
			swap(matrix, grid, hd.houses_e[i], hd.houses_b[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new < total_score:
				hc_data.append(total_score)
				swap(matrix, grid, hd.houses_e[i], hd.houses_b[j])
				total_score = score.calculate(grid, matrix)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

	# swap B and M
	for i in hd.houses_b:
		for j in hd.houses_m:
			swap(matrix, grid, hd.houses_b[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new < total_score:
				hc_data.append(total_score)
				swap(matrix, grid, hd.houses_b[i], hd.houses_m[j])
				total_score = score.calculate(grid, matrix)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

	# swap E and M
	for i in hd.houses_e:
		for j in hd.houses_m:
			swap(matrix, grid, hd.houses_e[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new < total_score:
				hc_data.append(total_score)
				swap(matrix, grid, hd.houses_e[i], hd.houses_m[j])
				total_score = score.calculate(grid, matrix)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

	# after hill climbing algorithm
	print(hc_data)
	tk_export.create(matrix, grid, (str(total_score) + " (after hill climbing)"))

	return hc_data


def swap(matrix, grid, house_a, house_b):
	# clear houses
	matrix.place(house_a.length, house_a.width, house_a.xcor, house_a.ycor, 'v')
	matrix.place(house_b.length, house_b.width, house_b.xcor, house_b.ycor, 'v')

	house_a_xcor_new = int(house_b.xcor + int(1/2 * house_b.length) - int(1/2 * house_a.length))
	house_a_ycor_new = int(house_b.ycor + int(1/2 * house_b.width) - int(1/2 * house_a.width))
	house_b_xcor_new = int(house_a.xcor + int(1/2 * house_a.length) - int(1/2 * house_b.length))
	house_b_ycor_new = int(house_a.ycor + int(1/2 * house_a.width) - int(1/2 * house_b.width))

	# check if houses can be swapped
	check_a = matrix.check(house_a.length, house_a.width, eval("info.house_" + str.lower(house_a.id[:1]) + "_free"), house_a_xcor_new, house_a_ycor_new)
	check_b = matrix.check(house_b.length, house_b.width, eval("info.house_" + str.lower(house_b.id[:1]) + "_free"), house_b_xcor_new, house_b_ycor_new)
	print("checks: {}, {}" .format(check_a, check_b))

	# if houses can be swapped, place houses on new location
	if (check_a == 0 and check_b == 0):
		print("old: house_a.xcor, ycor: {}, {}" .format(house_a.xcor, house_a.ycor))
		matrix.place(house_a.length, house_a.width, house_a_xcor_new, house_a_ycor_new, house_a.id)
		matrix.place(house_b.length, house_b.width, house_b_xcor_new, house_b_ycor_new, house_b.id)

		# update dictionary
		house_a.xcor, house_a.ycor = house_a_xcor_new, house_a_ycor_new
		house_b.xcor, house_b.ycor = house_b_xcor_new, house_b_ycor_new
		print("new: house_a.xcor, ycor: {}, {}" .format(house_a.xcor, house_a.ycor))

	# if houses cannot be swapped, place houses on original location
	else:
		matrix.place(house_a.length, house_a.width, house_a.xcor, house_a.ycor, house_a.id)
		matrix.place(house_b.length, house_b.width, house_b.xcor, house_b.ycor, house_b.id)
