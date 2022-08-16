print("Welcome to the Leafy Vegetable Hydration Level Detector\n")
print("Enter the following number to proceed \n 1 - start program \n 2 - exit program\n")
num = int(input("Input Num: "))

if num == 1: #broccoli code
    print("Choose from one of the ten plants available\n")
    print("[1] Broccoli")
    print("[2] Cabbage") #done leaf
    print("[3] Celery")
    print("[4] Kangkong")
    print("[5] Mint")
    print("[6] Parsley")
    print("[7] Spinach") #done leaf and stem
    print("[8] Spring Onion")
    print("[9] NA")
    print("[10] BA")
    plant = int(input("Plant Num: "))
    
    if plant == 1: #broccoli code
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
    
    if plant == 7: #Spinach code
        print("Do you want to use the leaf or the stem?\n")
        print("[1] Leaf")
        print("[2] Stem")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractspinachleaf()
        if detect == 2:
            print("Please Input Stem Directory")
            import colorextract as ce
            ce.ave_color_extractspinachstem()
     
elif num == 2:
    print("Thank You for using the program!")