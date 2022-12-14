print("Welcome to the Leafy Vegetable Hydration Level Detector\n")
print("Enter the following number to proceed \n 1 - start program \n 2 - exit program\n")
num = int(input("Input Num: "))

if num == 1:
    print("Choose from one of the ten plants available\n")
    print("[1] Broccoli") #done leaf
    print("[2] Cabbage") #done leaf
    print("[3] Celery") #done leaf and stem
    print("[4] Kangkong") #done leaf and stem
    print("[5] Mint") #done leaf
    print("[6] Parsley") #done
    print("[7] Spinach") #done leaf and stem
    print("[8] Spring Onion") #done leaf
    print("[9] Monstera Plant") #done leaf
    print("[10] Rubber Tree Plant") #done leaf
    plant = int(input("Plant Num: "))
    
    if plant == 1: #Broccoli code
        print("Proceed to the Leaf??\n")
        print("[1] Yes")
        print("[2] No")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractbroccoli()
        elif detect == 2: 
            print("Ending Program")   
            
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
    
    if plant == 3: #Celery code
        print("Do you want to use the leaf or the stem?\n")
        print("[1] Leaf")
        print("[2] Stem")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractceleryleaf()
        if detect == 2:
            print("Please Input Stem Directory")
            import colorextract as ce
            ce.ave_color_extractcelerystem()
            
    if plant == 4: #Kangkong code
        print("Do you want to use the leaf or the stem?\n")
        print("[1] Leaf")
        print("[2] Stem")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractkangkongleaf()
        if detect == 2:
            print("Please Input Stem Directory")
            import colorextract as ce
            ce.ave_color_extractkangkongstem()
            
    if plant == 5: #Mint code
        print("Proceed to the Leaf??\n")
        print("[1] Yes")
        print("[2] No")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractmint()
        elif detect == 2: 
            print("Ending Program")  
    
    
    if plant == 6: #Parsley code
        print("Proceed to the Leaf??\n")
        print("[1] Yes")
        print("[2] No")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractparsley()
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
            
    if plant == 8: #Spring Onion code
        print("Proceed to the Leaf??\n")
        print("[1] Yes")
        print("[2] No")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractspronion()
        elif detect == 2: 
            print("Ending Program") 
    
    if plant == 9: #Monstera code
        print("Proceed to the Leaf??\n")
        print("[1] Yes")
        print("[2] No")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractmonstera()
        elif detect == 2: 
            print("Ending Program")
     
    if plant == 10: #Rubber Tree code
        print("Proceed to the Leaf??\n")
        print("[1] Yes")
        print("[2] No")
        detect = int(input("Choice: "))
        if detect == 1:
            print("Please Input Leaf Directory")
            import colorextract as ce
            ce.ave_color_extractrubbertree()
        elif detect == 2: 
            print("Ending Program")  
            
elif num == 2:
    print("Thank You for using the program!")