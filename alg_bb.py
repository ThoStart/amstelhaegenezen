'''
Complete Algorithm:

Sort all items in decreasing order of ratio of value per unit weight so that
an upper bound can be computed using Greedy Approach.

Initialize maximum profit, maxProfit = 0
Create an empty queue, Q.
Create a dummy node of decision tree and enqueue it to Q. Profit and weight of dummy node are 0.
Do following while Q is not empty.
Extract an item from Q. Let the extracted item be u.
Compute profit of next level node. If the profit is more than maxProfit, then update maxProfit.
Compute bound of next level node. If bound is more than maxProfit, then add next level node to Q.
Consider the case when next level node is not considered as part of solution and
add a node to queue with level as next, but weight and profit without considering next level nodes.
'''

# sorteer alle house classes in decreasing order of score
# iets met upper bound using greedy Approach

#initialize maxprofit = 0

# create an empty queue

# create a dummy node of decision tree and enqueue it to q
# profit and score of dummy node are 0
