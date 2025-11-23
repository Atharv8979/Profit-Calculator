def product_details():
    print("\nEnter Product Details:")
    while True:
        try:
            
            cp = float(input("Enter Cost Price (CP): "))
            sp = float(input("Enter Selling Price (SP): "))
            break
        except:
            print("Invalid Input... Please enter numbers only...")
            print()

    return cp, sp
