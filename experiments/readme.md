This map contains results of performed experiments.

State space experiment
	- state space calculation:
			To approach the state space of the Amstelhaege problem, the size of the grid was used as to estimate the number of different spots where a house can
			be placed. The number of different spots is incremented by a factor of the scale^2 (for both length and width). This amount of possibilities is for
			only one house so the amount is multiplied by the number of houses and placed as the power of 2, because bungalows and maisons can be rotated.

			State-space = size of grid * scale^2 * number of eengezinswoningen + 2^(size grid * scale^2 * number of bungalows) + 2^(size grid * scale^2 *
			number of maisons) = 115200 * 12 + 2^(115200 * 5) + 2^(115200 * 3) = 1,89 * 10^173393 = 10^10^5,24

	- upper bound calculation:
			Use most free space for each house.


			upper bound = ((shortest side of grid) - (longest side of eengezinswoning + minimal free space eengezinswoning * 2)) / 2 * increment factor + 1) * number of eengezinswoningen * worth eengezinswoning + ((shortest side of grid) - (longest side of bungalow + minimal free space bungalow * 2)) / 2 * increment factor + 1) * number of bungalows * worth bungalow + ((shortest side of grid) - (longest side of maison + minimal free space maison * 2)) / 2 * increment factor + 1) * number of maisons * worth maison

	- lower bound calculation:
			Use only obligated free space for each house.

			lower bound = number of eengezinswoningen * worth eengezinswoning + number of bungalows * worth bungalow + number of maisons * worth maison = 12 * 285000 + 5 * 399000 + 3 * 610000 = 7245000

Different water layout experiments:
		Introduction
			Two different water layouts are compared with each other using the random algorithm to determine the best layout.
		Experiment
			The random algorithm was performed 10000 times for each of the layouts (n=10000). Averages were compared with an paired t test.
		Results (shown in water layout 1 vs water layout 2 map)
			Water layout 1 has a mean score of
			9.016.502,52 (SD: 381.700,10), water layout 2 has a mean score of 8.985.892,99 (SD: 379.747,33).
		Conclusion
			Paired t-test shows layout 1 has a significant higher score than water layout 2 (p<0.0001). Water layout 1 has thus a higher chance of a good score than water layout 2.

Random algorithm vs. Greedy algorithm experiments:
		Introduction
				The random algorithm is an algorithm that places 20 houses on random places in the grid.
				The greedy algorithm is a deterministic algorithm that puts all 20 houses in such a way that all houses have the highest possible average free
				space. Expected is that the deterministic score of the greedy algorithm will be higher than the average score of the random algorithm. The
				difference between the score of the greedy algorithm with the average score of the random algorithm will tell of what quality the greedy algorithm
				is.
		Experiment
				As the greedy algorithm is deterministic it was performed once. The random algorithm was performed 10000 times (n=10000).  
				Average scores were compared with an unpaired t-test.
		Results (shown in map random vs greedy)
				Greedy algorithm had a score of €10.067.460,00 with a standard deviation of €0,00.
				Random algorithm had an average score of €9.007.194,04 with a standard deviation of €384.892,01.
				Unpaired t-test showed the greedy algorithm has a score significant (p<0.0001) higher than the average score random algorithm.
		Discussion
				The greedy algorithm has a higher score than

Random algorithm with hill climber vs. greedy algorithm with hill climber:
		Introduction
				The random algorithm is an algorithm that places 20 houses on random places in the grid. The greedy algorithm is a deterministic algorithm that
				puts all 20 houses in such a way that all houses have the highest possible average free space. The hill climber algorithm first tries to swap the
				houses, if a swap beneficial for the score the swap becomes permanent. After a house is swapped, 1000 different spots will be tried for the house,
				again if the new spot is beneficial for the score it becomes permanent. After all possible house swaps will be checked again. To determine where
				the hill climber algorithm used has more effect, the random algorithm compared with the hill climber algorithm were compared with the greedy
				algorithm compared with the hill climber algorithm.
		Experiments
				Water layout 1 was used. The average score of the solution of the random algorithm combined with the hill climber algorithm (n=100) was compared
				with the solution of the greedy algorithm combined with the hill climber algorithm. The scores were compared with an unpaired t-test.
		Results (shown in map random hc vs greedy hc)
				Greedy algorithm combined with the hill climber algorithm had a score of €11.924.776,17 (Standard Deviation: €268.162,39)
				Random algorithm combined with the hill climber algorithm had an average score of €12.027.168,27 (Standard Deviation: €165.888,26)
		Discussion
				The unpaired t-test showed solutions generated with the greedy algorithm combined with the hill climber algorithm is significant higher than the  
				average score of 100 runs of the random algorithms combined with the hill climber algorithm (p<0.01). The maximum score of the random algorithm combined with the hill climber algorithm is higher than the score of the greedy algorithm.
