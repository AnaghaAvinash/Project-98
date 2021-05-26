def SwipeFileData():

    file1 = input("Enter first file's name : ")
    file2 = input("Enter second file's name : ")

    with open(file1, 'r') as a:
        dataA = a.read()

    with open(file2, 'r') as b:
        dataB = b.read()
        
    with open(file1, 'w') as a:
        a.write(dataB)

    with open(file2, 'w') as b:
        b.write(dataA)

    print("Data Swapped! Open files to see it!")

SwipeFileData()