print("Welcome to the Leafy Vegetable Hydration Level Detector\n")
print("Enter the following number to proceed \n 1 - start program \n 2 - exit program\n")
num = int(input("Input Num: "))

if num == 1: #broccoli code
    print("Choose from one of the ten plants available\n")
    print("[1] Broccoli")
    print("[2] Cabbage")
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
            
    if plant == 2: #cabbage code
        print("Proceed to the leaf?\n")
        print("[1] Yes")
        print("[2] No")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractcabbage()
        elif detect == 2: 
            print("Ending Program")     
     
elif num == 2:
    print("Thank You for using the program!")