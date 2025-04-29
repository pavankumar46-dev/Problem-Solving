def count_duplicates(lst):
  repeated_dict = {}
  for i in range(len(lst)):
      count = 0
      for j in range(0, len(lst)):
          if lst[i] == lst[j]:
              count = count+1
              repeated_dict[lst[i]] = count
  print(repeated_dict)
    
    
    
lst = [1,2,2,4,3,5,6,7,8,1]
count_duplicates(lst)
