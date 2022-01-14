# Element search: Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Method 1: Using a regular loop
def element_search(list, element):
    is_present = False
    if element in list:
        is_present = True
    return is_present

list = [2, 4, 6, 8, 10]
print(element_search(list, 8))

# Method 2: Using binary search method, search by repeatedly dividing the search interval by half
def find(ordered_list, element):
    # Creating the boundary
    start_index = 0
    end_index = len(ordered_list) - 1

    while True:
        middle_index = int((end_index + start_index) / 2)

        # Checking if middle element is the element to find, using it later as the new boundary if otherwise
        middle_element = ordered_list[middle_index]
       
        # Condition where element does not exist: when there is no more middle_index within that boundary
        if middle_index == start_index or middle_index == end_index or middle_index == 0:
            return False
        
        if middle_element == element or ordered_list[start_index] == element or ordered_list[end_index] == element:
            return True
            
        elif middle_element < element:
            start_index = middle_index
        else:
            end_index = middle_index

print(find(list, 4))