# 2. Design a Python function that takes a list of elements as input and returns the count of unique elements in the list. The function should not utilize any built-in Python libraries or functions related to counting or sets. 

def count_unique_elements(lst):
    unique_elements = []
    count = 0

    for val in lst:
        if val not in unique_elements:
            unique_elements.append(val)
            count += 1

    return count

input_list = list(map(int, input("Enter the list of elements: ").split()))  
unique_count = count_unique_elements(input_list)
print(unique_count)  