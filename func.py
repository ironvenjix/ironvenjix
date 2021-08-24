str = input('Please enter a string : ')
def frequency(string):
    d = {}
    for i in string:
        d[i] = string.count(i)
    return sorted(d.items(), key=lambda x: x[1], reverse = True)     
print(frequency(str))
