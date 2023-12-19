from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_info = {}
        self.SortedCuisines = defaultdict(SortedList)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            self.SortedCuisines[cuisine].add((-rating, food))


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.food_info[food]

        self.food_info[food] = (cuisine, newRating)
        self.SortedCuisines[cuisine].discard((-oldRating, food))
        self.SortedCuisines[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.SortedCuisines[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)