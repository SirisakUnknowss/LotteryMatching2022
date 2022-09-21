def pnt():
    fix =  1000
    for round in range(10):
        startNumber = fix * round
        endNumber = fix * (round + 1)
        f = open(f"number{startNumber}-{endNumber}.csv", "w")
        for index in range(startNumber, endNumber):
            f.write(f"{index:06},0,2\n")
        f.close()