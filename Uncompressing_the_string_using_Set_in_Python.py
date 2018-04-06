# Implementing the task
# Reading the string from the file
# Uncompressing the line by the rule - a3 = aaa
print()
# Reading the line from the file
with open('dataset_3363_2.txt') as inf:
    line = inf.readline().strip()
print(line)

# Uncompressing the line
set_of_numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
uline = ''
l = ''
n = ''
for i in range(len(line)):
    if line[i] not in set_of_numbers:  # Checking if letter is letter
        l = line[i]
        n = ''
        print(l, end='')  # Checking if program works correctly
    elif line[i] in set_of_numbers:  # Checking if it is a number              
        n += line[i]
        if i == len(line) - 1:  # Checking for the last element - it is always number
            print(n)  # Checking if program works correctly
            for j in range(int(n)):
                uline += l
        if i + 1 < len(line) - 1:  # Checking if the next element is not a number
            if line[i + 1] not in set_of_numbers:
                print(n, end='')  # Checking if program works correctly
                for j in range(int(n)):
                    uline += l

print()
# Showing uncompressed line
print(uline)

# Writing uncompressed line in the file
with open('test3.txt', 'w') as ouf:
    ouf.write(uline)

