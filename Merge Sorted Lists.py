# my solution

def merge_list(test_input_list1, test_input_list2):
    new_list = [0] * (len(test_input_list1) + len(test_input_list2))
    for i in range(len(test_input_list1)):
        new_list[2*i] = test_input_list1[i]
        new_list[2*i+1] = test_input_list2[i]
    return new_list

# favorite solution:
def merge_list(test_input_list1, test_input_list2):
    test_input_list1.extend(test_input_list2)
    return sorted(test_input_list1)

# official solution

def merge_list(list1, list2): 
    list3 = []
    i = 0
    j = 0
  
    # Traverse both lists
    # If the current element of first list
    # is smaller than the current element
    # of the second list, then store the
    # first list's value and increment the index 

    while i < len(list1) and j < len(list2): 
      
        if list1[i] < list2[j]: 
            list3.append(list1[i])
            i = i + 1
        else: 
            list3.append(list2[j])
            j = j + 1
      
  
    # Store remaining elements of the first list
    while i < len(list1): 
        list3.append(list1[i])
        i = i + 1
  
    # Store remaining elements of the second list
    while j < len(list2): 
        list3.append(list2[j])
        j = j + 1

    return list3
