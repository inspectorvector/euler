def powersum():
    bigstring = str(2**1000)
    running_total = 0

    for i in range(len(bigstring)):
        num_in_string = int(bigstring[i])
        running_total += num_in_string
    return running_total

print(powersum())