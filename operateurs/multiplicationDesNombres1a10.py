def multiplication():
    m = 0
    for i in range(1, 11):
        for j in range(1, 11):
            m = i * j
            print(i, " * ", j, " = ", m)
            print()
multiplication()