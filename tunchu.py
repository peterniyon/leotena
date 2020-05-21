while True:
    a = eval(input(print("a = ")))
    try:
        result = 1/a
    except:
        print("Error case")
        exit(0)
    else:
        print("pass case mzee")
        exit(1)