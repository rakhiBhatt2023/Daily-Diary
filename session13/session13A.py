# Sort Function
def sort(data, low_to_high=0):
    if low_to_high == 0:
        for outer in range(0, len(data) - 1):
            for inner in range(0, len(data) - outer - 1):
                if data[inner] > data[inner + 1]:
                    temp = data[inner]
                    data[inner] = data[inner + 1]
                    data[inner + 1] = temp
        print('Sorted numbers are:', data)
    else:
        for outer in range(0, len(data) - 1):
            for inner in range(0, len(data) - outer - 1):
                if data[inner] < data[inner + 1]:
                    temp = data[inner]
                    data[inner] = data[inner + 1]
                    data[inner + 1] = temp
        print('Sorted numbers are:', data)


numbers = [10,80,20,40,50,30,20]
sort(numbers)                          # prints ascending order
sort(numbers,low_to_high=4)            # any value other than 0 will give descending order