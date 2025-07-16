def max(data):
    max_number = data[0]
    for index in range (1, len(data)):
        if data[index] > max_number:
            max_number = data[index]
    print('Max number is:',max_number)

numbers=[10, 17, 23, 45, 9, 12]
max(numbers)

ipl_scores = [111, 210, 120, 97, 56, 32]
max(ipl_scores)

