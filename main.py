import random

def binary_search(list: list[int], item: int) -> int:
    low: int = 0
    high: int = len(list) - 1
    
    print(f"{item = }", end=";\n")
    
    while low <= high:
        half: int = (low + high) // 2
        guess: int = list[half]
        
        print(f"{guess = }; {half = }")
        if guess == item:
            return half
        elif guess > item:
            high = half - 1
        else:
            low = half + 1
            
    return None

test_list = [random.randint(0, 1000000) for i in range(2**20)]
test_list.sort()
print(binary_search(test_list, random.randint(0,100000)))
