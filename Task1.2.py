for X in range(1):
    for Y in range(1):
        for Z in range(1):
            if not (X or Y or Z) == (not X and not Y and not Z):
                print ('утверждение истинно')
            else:
                print ('утверждение ложно')