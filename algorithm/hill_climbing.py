from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.score as score

def start(matrix, grid):
    hc_data = []

    execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b)
    execute_swap(grid, matrix, hc_data, hd.houses_b, hd.houses_m)
    execute_swap(grid, matrix, hc_data, hd.houses_m, hd.houses_e)
    execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b)

    print(hc_data)

    number_of_iterations = 1000 - len(hc_data)

    return hc_data

def execute_swap(grid, matrix, hc_data, houses_a, houses_b):
    total_score = score.calculate(grid, matrix)

    for i in houses_a:
        for j in houses_b:
            Matrix.swap(matrix, grid, houses_a[i], houses_b[j])
            total_score_new = score.calculate(grid, matrix)

            if total_score_new < total_score:
                hc_data.append(total_score)
                Matrix.swap(matrix, grid, houses_a[i], houses_b[j])
                total_score = score.calculate(grid, matrix)
            else:
                total_score = total_score_new
                hc_data.append(total_score)
