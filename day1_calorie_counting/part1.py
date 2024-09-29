
maxN = 0    # Variable that stores max number found
current = 0     # Variable that will store the calories for each elf

while True:     # Loop that never stops
    try:
        N = int(input())    # Stores user input in N
        current += N   # Adds N to current elf
        maxN = max(maxN,current)    # Checks if current elf has passed maxN
    except ValueError:      # If input is not an int (empty line in this case)
        current=0   # Sets current to 0
    print(maxN)     # Print max number