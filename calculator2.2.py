print ("calculator 2.2")

while True:

    conf = input("Would you like to use this calculator? ")

    if conf == ("no"):
            print ("Goodbye!")
            break

    if conf == ("yes"):
        
        while True:

            try:

                x, op, y = input("Calculate: "). split(" ")
                num1 = float(x)
                num2 = float(y)

                if op in ('+', '-', '*', '/'):

                    if op == ("+"):
                        print (num1 + num2)
                    if op == ("-"):
                        print (num1 - num2)
                    if op == ("*"):
                        print (num1 * num2)
                    if op == ("/"):
                        if y == ("0"):
                            print ("Undefined.")
                            continue
                        else: 
                            print (num1 / num2)

                cont = input("Ready to continue? ")

                if cont == ("no"):
                    print ("Then close the program...")
                    break
                if cont == ("yes"):
                    continue                        
                else:
                    print ("Please use yes or no.")
                    
            except ValueError:
                print ("Error. Please format x (operator) y")

    else:
        print ("Please use yes or no.")
        continue