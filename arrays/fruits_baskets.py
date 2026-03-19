from collections import defaultdict
def fruit_baskets(fruits):
    l = 0
    basket = defaultdict(int)
    maxFruits = 0
    for r in range(len(fruits)):
        basket[fruits[r]] = basket.get(fruits[r],0) + 1
        while len(basket) > 2:
            fruit_count = basket.get(fruits[l])
            if fruit_count == 1:
                del basket[fruits[l]]
            else:
                basket[fruits[l]]-=1
            l+=1
        maxFruits = max(maxFruits,r-l+1)
    return maxFruits

fruits = [0,1,2,2]
print(fruit_baskets(fruits))