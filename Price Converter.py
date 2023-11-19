def fuel_converter(price_per_100l):
    while True:
        
        if int(price_per_100l)<0:
            print("Error: Please enter a positve numeric value. ")
            continue
        elif price_per_100l.isalpha():
            print("Error: Please enter a positve numeric value. ")
            continue
        elif price_per_100l.isnumeric():
            price=int(price_per_100l)
            break
    price_per_litre= price/100
    round(price_per_litre,2)
    
    return price_per_litre

if __name__ == "__main__":
    p= input("Please enter the price per 100 L of fuel: ")
    litre=fuel_converter(p)
    print("The price per litre of fuel is","$", litre)
    
            
    