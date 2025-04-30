# Approach One
def extract_int_from_str(string):
    integer_from_string = []
    for i in (string):
        try:
            if int(i):
                integer_from_string.append(i)
        except ValueError:
            continue
    
    print(integer_from_string)

# Approach Two
def extract_int_from_str2(string):
    integer_from_string = []
    for i in (string):
        if i.isdigit():
            integer_from_string.append(i)
            
    print(integer_from_string)

extract_int_from_str("123qwerty9891")
extract_int_from_str2("123qwerty9891")

# Sample output
#['1', '2', '3', '9', '8', '9', '1']
#['1', '2', '3', '9', '8', '9', '1']
