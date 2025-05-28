#Program to slice the list and reverse it

orig_list=[1,2,3,4,5,6,7,8,9]
slice_list =orig_list[:5]
print('Original List:',orig_list)
print('Extracted first five elements:',slice_list)
slice_list.reverse()
print('Reversed extracted elements:',slice_list)