"""
Author: Loi Chai Lam
Date: 6 Mar 2024
Coin Change Problem in Dynamic Programming

Week 4 FIT 2004

Problem:
A country uses N coins with denominations {a1, a2, …, aN}. 
Given a value V, find the minimum number of coins that add up to V.

Example: 
Suppose the coins are {1, 5, 10, 50} and the value V is 110. 
The minimum number of coins required to make 110 is 3 (two 50 coins, and one 10 coin).

Thought:
You need to make the value V=12. 
Assume coins we have are [9,5,6,1] 
Assume we know the optimal solutions for every V < 12 and results are stored in Memo[ ]
If I tell you that you must use at least one coin of value 9, what is the minimum number of coins to make V=12?
If optimal solution contains a coin with value x (e.g., coin 9 in the example):
	MinCoins(V) = 1 + Memo[V- x]

"""


class Coin_Change:
    def __init__(self, v, coins_array):
        assert v > 0, "the value V should be larger than 0"
        self.V = v
        self.coins_array = coins_array

        # initialize the array
        self.min_coins_array = [-1] * (self.V + 1)
        self.min_coins_value_array = [-1] * (self.V + 1)

        self.min_coins_array[0] = 0
        self.min_coins_value_array[0] = 0



    def coin_change_bottom_up(self):
        """
        This function is to use Dynamic Programming Bottom Up approach to get the minimum 
        number of coins required to add up to V
        """
        for i in range(1, self.V + 1):
            # set the initial min coins to infinity
            minCoins = float('inf')
            coin_value = -1
            for j in range(len(self.coins_array)):
                # if the coin value is less than or equal to the value V,
                # then the coin required is the remaining array value + 1 self coin
                if self.coins_array[j] <= i:
                    coin_required = 1 + self.min_coins_array[i - self.coins_array[j]]
                # compare and set the min coins
                if coin_required < minCoins:
                    minCoins = coin_required
                    coin_value = self.coins_array[j]
            # save the minimum coins requried and its value
            self.min_coins_array[i] = minCoins
            self.min_coins_value_array[i] = coin_value
        return self.min_coins_array[self.V]



    def backtrack_get_coin_value(self):
        """
        This function is to use Back Tracking to get the minimum coins values that add up to V
        """
        value = self.V
        coins_value_array_for_V = []
        while self.min_coins_value_array[value] > 0:
            coins_value_array_for_V.append(self.min_coins_value_array[value])
            value = value - self.min_coins_value_array[value]
        return coins_value_array_for_V


    def coin_change_top_down(self, value):
        """
        This function is to use Dynamic Programming Top Down approach to get the minimum 
        number of coins required to add up to V
        """
        if self.min_coins_array[value] != -1:
            return self.min_coins_array[value]
        else:
            minCoins = float('inf')
            for j in range(len(self.coins_array)):
                coin_required = float('inf')
                # if the coin value is less than or equal to the value V,
                # then the coin required is the remaining array value + 1 self coin
                if self.coins_array[j] <= value:
                    coin_required = 1 + self.coin_change_top_down(value - self.coins_array[j])
                # compare and set the min coins
                if coin_required < minCoins:
                    minCoins = coin_required
                    coin_value = self.coins_array[j]
            # save the minimum coins requried and its value
            self.min_coins_array[value] = minCoins
            self.min_coins_value_array[value] = coin_value
        return self.min_coins_array[value]




if __name__ == "__main__":
    V = 12
    coins = [9, 5, 6, 1]

    # # ================Bottom Up======================#
    # coin_change_bottom_down = Coin_Change(V, coins)
    # min_no_coins = coin_change_bottom_down.coin_change_bottom_up()
    # print(min_no_coins)

    # min_coin_value = coin_change_bottom_down.backtrack_get_coin_value()
    # print(min_coin_value)

    # print("In coins array", coins, ",the minimum number of coins that adds up to", V, "are", min_no_coins, "coins with values", min_coin_value)


# ================Top Down======================#
    coin_change_top_down = Coin_Change(V, coins)
    min_no_coins = coin_change_top_down.coin_change_top_down(V)
    print(min_no_coins)

    min_coin_value = coin_change_top_down.backtrack_get_coin_value()
    print(min_coin_value)
    print("In coins array", coins, ",the minimum number of coins that adds up to", V, "are", min_no_coins, "coins with values", min_coin_value)
