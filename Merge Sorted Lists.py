def merge_list(test_input_list1, test_input_list2):
    new_list = [0] * (len(test_input_list1) + len(test_input_list2))
    for i in range(len(test_input_list1)):
        new_list[2*i] = test_input_list1[i]
        new_list[2*i+1] = test_input_list2[i]
    return new_list
    pass
