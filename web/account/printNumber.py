def pnt():
    f = open("demofile3.csv", "w")
    for index in range(200000):
        f.write(f"{index:06},0,2\n")
    f.close()