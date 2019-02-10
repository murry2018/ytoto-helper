def read_mileages():
    lines = list()
    while True:
        try: row = input().split()
        except EOFError: break
        if row[-1] == 'O':
            lines.append(row)
        elif row[-1] != 'X': # error case
            print(row[-1])
    return lines

def median(numbers):
    # declaration : size, mid
    size = len(numbers)
    mid = size//2
    return (
        (numbers[mid] + numbers[mid-1]) / 2 if size % 2 == 0
        else numbers[mid]
    )

def average(numbers):
    _sum = 0
    for item in numbers:
        _sum += item
    return _sum / len(numbers)    
        
lines = read_mileages()
mileages = list(map( lambda row: int(row[1]), lines ))
print("Minimum: {}, Maximum: {}, Median: {}, Average: {:.2f}"
      .format(mileages[-1], mileages[0] , median(mileages), average(mileages)))
