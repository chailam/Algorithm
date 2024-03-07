"""
Author: Loi Chai Lam
Date: 7 Mar 2024

0/1 Knapsack for Dynamic Programming

Week 4 FIT 2004

Problem: 
Given a capacity C and a set of items with their weights and values, 
you need to pick items such that their total weight is at most C and their total value is maximized. 
What is the maximum value you can take? 
In 0/1 knapsack, each item can only be picked at most once.


Example:
Imagine information below:
Item            A       B       C           D
Weight(kg)      6       1       5           9
Value($)        230     40     350         550


What is the maximum value for the example given below given capacity is 11 kg?
Answer: $590 (B and D)


Thought:
Assume that we have computed solutions for every capacity<=11 considering the items {A,B,C}.
What is the solution for capacity=11 and set {A,B,C,D} ?

Case 1: the knapsack must NOT contain D
Solution for 0/1 knapsack with set {A,B,C} and capacity 11.

Case 2: the knapsack must contain D
The value of item D + solution for 0/1 knapsack with set {A,B,C} and capacity 11-9=2 

Solution = max(Case1, Case2)

        1   2   3   4   5   6
0   N   0   0   0   0   0   0
1   A   0   0   0   0   0   230
2   B   40  40  40  40  40  230
3   C   40  40  40  40  350 390
4   D   40  40  40  40  350 390


"""


class Bounded_Knapsack:
    def __init__(self, capacity, weight_array, value_array, item_array):
        assert capacity >= 1, "Capacity should be bigger than 1"
        assert len(value_array) == len(weight_array) == len(item_array), "The value array must have same length as the weight array"

        self.capacity = capacity
        self.weight_array = weight_array
        self.value_array = value_array
        self.item_array = item_array

        # initialize the empty 2*2 array
        self.max_value_array = [[0] * (self.capacity + 1) for i in range(len(self.item_array) + 1)]
        self.max_value_content_weight = [[0] * (self.capacity + 1) for i in range(len(self.item_array) + 1)]
        self.max_value_content_item = [[0] * (self.capacity + 1) for i in range(len(self.item_array) + 1)]



    def bounded_knapsack_bottom_up(self):
        """
        Time complexity: O(NC)
        Space Complexit: O(NC)
        """
        for i in range(1, len(self.item_array) + 1):
            for j in range(1, self.capacity + 1):
                excludedValue = self.max_value_array[i - 1][j]
                includedValue = 0
                if self.weight_array[i - 1] <= j:
                    includedValue = self.value_array[i - 1] + self.max_value_array[i - 1][j - self.weight_array[i - 1]]
                self.max_value_array[i][j] = max(excludedValue, includedValue)

        print(self.max_value_array)
        return self.max_value_array[i][j]



if __name__ == "__main__":
    item_array = ["A", "B", "C", "D"]
    weight_array = [6, 1, 5, 9]
    value_array = [230, 40, 350, 550]
    capacity = 11

    test_bottom_up = Bounded_Knapsack(capacity, weight_array, value_array, item_array)
    result_bottom_up = test_bottom_up.bounded_knapsack_bottom_up()
    print(result_bottom_up)
