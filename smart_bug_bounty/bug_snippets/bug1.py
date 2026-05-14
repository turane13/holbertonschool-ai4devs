def calculate_average(numbers):
    if numbers is None:
        return None
    
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
        
    result = total / count
    return result
