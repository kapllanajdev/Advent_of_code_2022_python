
maxN1 = 0    # Variable that stores max number found
maxN2 = 0    # Variable that stores second max number found
maxN3 = 0    # Variable that stores third max number found
current = 0     # Variable that will store the calories for each elf

while True:     # Loop that never stops
    try:
        N = int(input())    # Stores user input in N
        current += N   # Adds N to current elf
        if current > maxN1:     # If current has passed maxN
            maxN3 = maxN2
            maxN2 = maxN1
            maxN1 = current  # Checks if current elf has passed maxN
        elif current > maxN2:   # Elif current has passed maxN2 
            maxN3 = maxN2
            maxN2 = current
        elif current > maxN3:   # Elif current has passed maxN3
            maxN3 = current
    except ValueError:      # If input is not an int (empty line in this case)
        current=0   # Sets current to 0
    print(maxN1 + maxN2 + maxN3)     # Print max number