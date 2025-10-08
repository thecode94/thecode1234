#max value using brtue force
def find_max_value(data):
    max_val = data[0]
    for val in data:
        if val > max_val:
            max_val = val
        
    return max_val
data = [12, 5, 23, 7, 34, 9, 30]
print("Max value found using Brute Force:", find_max_value(data))