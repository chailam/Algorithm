"""
Author: Loi Chai Lam
Date: 6 Mar 2024

Unbounded Knapsack for Dynamic Programming

Week 4 FIT 2004

Problem: 
Given a capacity C and a set of items with their weights and values, 
you need to pick items such that their total weight is at most C and their total value is maximized. 
What is the maximum value you can take? 
In unbounded knapsack, you can pick an item as many times as you want.


Example:
Imagine information below:
Item            A       B       C           D
Weight(kg)      9       5       6           1
Value($)        550     350     180         40


What is the maximum value for the example given below given capacity is 12 kg?
Answer: $780 (take two Bs and two Ds)

Thought:
Assume we know the optimal solutions for every C < 12kg and results are stored in Memo[ ]
If I tell you that you must use at least one item #1 (weight 9kg), what is the maximum value if  C=12?
If optimal solution contains an item #i (e.g., item 1 with weight 9 and value $550)
	MaxValue = Value[i] + Memo[C- weight[i]] 

1       2       3       4       5       6   
40      80      120     160     350     390
"""

class Unbounded_Knapsack:
    def __init__(self,capacity, weight_array, value_array, item_array):
        assert capacity >= 1, "Capacity should be bigger than 1"
        assert len(value_array) == len(weight_array) == len(item_array), "The value array must have same length as the weight array"

        self.capacity = capacity
        self.weight_array = weight_array
        self.value_array = value_array
        self.item_array = item_array

        #initialize the empty array
        # array to hold the maximum value
        self.max_value_array = [-1] * (self.capacity + 1)
        self.max_value_array[0] = 0

        # array to hold the weight for that maximum value
        self.max_value_content_weight =  [-1] * (self.capacity + 1)
        self.max_value_content_weight[0] = 0

        # array to hold the iteam for the maximum value
        self.max_value_content_item =  [-1] * (self.capacity + 1)
        self.max_value_content_item[0] = 'Z'



    def unbounded_knapsack_bottom_up(self):
        """
        This function is to use Dynamic Programming Bottom Up approach to get the maximum value given a capacity
        """
        # calculate from capacity 1 to self.capacity
        for i in range(1, self.capacity + 1):
            max_value = -1
            max_value_content_weight = ""
            max_value_content_item = ''
            # calculate for each weight
            for j in range(len(self.weight_array)):
                tmp_max_value = -1
                # if the weight does not exceed the capacity
                if i >= self.weight_array[j]:
                    tmp_max_value = self.value_array[j] + self.max_value_array[i - self.weight_array[j]]
                if tmp_max_value > max_value:
                    max_value = tmp_max_value
                    max_value_content_weight = self.weight_array[j]
                    max_value_content_item = self.item_array[j]
            self.max_value_array[i] = max_value  
            self.max_value_content_weight[i] = max_value_content_weight
            self.max_value_content_item[i] = max_value_content_item
        return self.max_value_array[self.capacity]


    def backtrack_get_weight_and_item(self):
        """
        This function is to use Back Tracking to get the weight and items that added up 
        to the maximum value given a capacity
        """
        capacity = self.capacity
        weight_value_array_for_capacity = []
        item_array_for_capacity = []
        while self.max_value_content_weight[capacity] > 0:
            weight_value_array_for_capacity.append(self.max_value_content_weight[capacity])
            item_array_for_capacity.append(self.max_value_content_item[capacity])
            capacity = capacity - self.max_value_content_weight[capacity]
        return (weight_value_array_for_capacity,item_array_for_capacity)



    def unbounded_knapsack_top_down(self,capacity):
        """
        This function is to use Dynamic Programming Top Down approach to get the maximum value given a capacity
        """
        if self.max_value_array[capacity] != -1:
            return self.max_value_array[capacity]
        else:
            max_value = 0
            value = 0
            max_value_content_weight = 0
            for i in range(len(self.weight_array)):
                if capacity >= self.weight_array[i]:
                    value = self.value_array[i] + self.unbounded_knapsack_top_down(capacity - self.weight_array[i])
                if value > max_value:
                    max_value = value
                    max_value_content_weight = self.weight_array[i]
                    max_value_content_item = self.item_array[i]
            self.max_value_array[capacity] = max_value
            self.max_value_content_weight[capacity] = max_value_content_weight
            self.max_value_content_item[capacity] = max_value_content_item
        return self.max_value_array[capacity]




if __name__ == "__main__":
    item_array = ["A","B","C","D"]
    weight_array = [9,5,6,1]
    value_array = [550,350,180,40]
    capacity = 12


# ================Bottom Up======================#
# test_bottom_up = Unbounded_Knapsack(capacity,weight_array,value_array,item_array)
# result_bottom_up = test_bottom_up.unbounded_knapsack_bottom_up()
# #print(result_bottom_up)

# (result_backtrack_weight, result_backtrack_item) = test_bottom_up.backtrack_get_weight_and_item()
# print("For item",item_array,"with weight array (kg)", weight_array, "with its value ($)",value_array,\
#     ",the maximum value that is within capacity", capacity, "kg are $", result_bottom_up,\
#          "with weight",result_backtrack_weight,"and item",result_backtrack_item)


# ================Top Down======================#
test_top_down = Unbounded_Knapsack(capacity,weight_array,value_array,item_array)
result_top_down = test_top_down.unbounded_knapsack_top_down(capacity)
#print(result_top_down)

(result_backtrack_weight, result_backtrack_item) = test_top_down.backtrack_get_weight_and_item()
print("For item",item_array,"with weight array (kg)", weight_array, "with its value ($)",value_array,\
    ",the maximum value that is within capacity", capacity, "kg are $", result_top_down,\
         "with weight",result_backtrack_weight,"and item",result_backtrack_item)