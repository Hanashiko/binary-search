import random

def binary_search(list: list[int], item: int) -> int:
    low: int = 0
    high: int = len(list) - 1
    
    print(f"{item = }", end=";\n")
    
    while low <= high:
        mid: int = (low + high) // 2
        guess: int = list[mid]
        
        print(f"{guess = }; {mid = }")
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

test_list = [random.randint(0, 1000000) for i in range(2**20)]
test_list.sort()
print(binary_search(test_list, random.randint(0,100000)))
