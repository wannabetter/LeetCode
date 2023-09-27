from typing import List


def filterRestaurants(restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    restaurants = sorted(restaurants, key=lambda item: (-item[1],-item[0]))
    ans = []
    for restaurant in restaurants:
        if veganFriendly == 1 and restaurant[2] == 0:
            continue
        if maxPrice < restaurant[3]:
            continue
        if maxDistance < restaurant[-1]:
            continue
        ans.append(restaurant[0])
    return ans
