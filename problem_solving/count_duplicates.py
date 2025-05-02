def count_duplicates(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] = count_dict[i]+1
        else:
            count_dict[i] = 1
    filtered = {k: v for k, v in count_dict.items() if v > 1}
    print(filtered)
    

count_duplicates([1,1,1,2,3,4,5,6,8,8])
