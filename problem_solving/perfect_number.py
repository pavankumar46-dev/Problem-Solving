# Sum of proper divisors is called perfect number
def perfect_number(num):
    divisor_list = []
    for i in range(1, num):
        if num%i == 0:
            divisor_list.append(i)
            
    print(divisor_list)
    print(sum(divisor_list))
    if sum(divisor_list) == num:
        print(f"Given number {num} is a perfect number")
    else:
        print(f"Given number {num} is not a perfect number")
    
perfect_number(28)
