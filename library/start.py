# Request user input the first time
def start():
    print("1: Random")
    print("2: Random + Hill climbing")
    print("3: Random + Simulated annealing")
    print("4: Greedy")
    print("5: Greedy + Hill climbing")
    print("6: Greedy + Simulated annealing")

    chosen_algorithm = input("Algorithm: ")
    while (len(str(chosen_algorithm)) > 1 or
    chosen_algorithm.isdigit() == False or
    int(chosen_algorithm) > 6 or
    int(chosen_algorithm) <= 0):
        print("Invalid input, try again.")
        chosen_algorithm = input("Algorithm: ")

    print("1:            2:\n◼︎ ◼︎ ◼︎ ◼︎ ◻︎ ◻︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎\n◼︎ ◼︎ ◻︎ ◻︎ ◻︎ ◻︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎\n◼︎ ◼︎ ◻︎ ◻︎ ◻︎ ◻︎   ◻︎ ◻︎ ◻︎ ◻︎ ◻︎ ◻︎\n◻︎ ◻︎ ◻︎ ◻︎ ◼︎ ◼︎   ◻︎ ◻︎ ◻︎ ◻︎ ◻︎ ◻︎\n◻︎ ◻︎ ◻︎ ◻︎ ◼︎ ◼︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎\n◻︎ ◻︎ ◼︎ ◼︎ ◼︎ ◼︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎")
    water_layout = input("Water layout: ")
    while (len(str(water_layout)) > 1 or
    water_layout.isdigit() == False or
    int(water_layout) > 2 or
    int(water_layout) <= 0):
        print("Invalid input, try again.")
        water_layout = input("Water layout: ")

    number_of_runs = input("Number of runs: ")
    while (number_of_runs.isdigit() == False or int(number_of_runs) <= 0):
        print("Invalid input, try again.")
        number_of_runs = input("Number of runs: ")

    visualize_data = input("Visualize data (y/n): ")
    while (visualize_data.upper().startswith('Y') == False and
    visualize_data.upper().startswith('N') == False):
        print("Invalid input, try again.")
        visualize_data = input("Visualize data (y/n): ")

    plot_data = input("Plot data (y/n): ")
    while (plot_data.upper().startswith('Y') == False and
    plot_data.upper().startswith('N') == False):
        print("Invalid input, try again.")
        plot_data = input("Plot data (y/n): ")

    return int(chosen_algorithm), int(water_layout), int(number_of_runs), visualize_data.upper()[0], plot_data.upper()[0]
