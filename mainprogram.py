print("Welcome to the Leafy Vegetable Hydration Level Detector\n")
print("Enter the following number to proceed \n 1 - start program \n 2 - exit program\n")
num = int(input("Input Num: "))

if num == 1:
    print("Choose from one of the ten plants available\n")
    print("[1] Kangkong")
    plant = int(input("Plant Num: "))
    if plant == 1:
        print("Do you want to use the leaf or the stem?\n")
        print("[1] Leaf")
        print("[2] Stem")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extracttest()
        elif detect == 2: 
            print("Please Input Stem Directory")
            import colorextract as ce
            ce.ave_color_extract()            
elif num == 2:
    print("Thank You for using the program!")