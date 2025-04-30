def find_prime(num):
    if num == 1:
        print("Given number is prime")
        return True
    elif num > 0:
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count == 2:
            print("Given number is prime")
            return True
        print("Given number is not a prime")
        return False
    else:
        print("Number should be possitive")
        return False

lst = [2, 3, 5, 11, 17, 23, 31, 47, 61, 73, 89, 101, 113, 149, 167, 191, 223, 257, 281, 307, 310]

for i in lst:
    find_prime(i)
