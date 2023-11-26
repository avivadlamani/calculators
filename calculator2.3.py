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
                else:
                    print ("Error. Please format x (operator) y.")
                    continue

                cont = input("Ready to continue? ")

                match cont:
                    case ("no"):
                        print ("Restarting application.")
                        break

                    case ("yes"):
                        continue
                        
                    case cont if cont != ("yes", "no"):
                        print ("Please use yes or no.")
                        print ("Continuing...")
                        continue
                    
            except ValueError:
                print ("Error. Please format x (operator) y.")

    else:
        print ("Please use yes or no.")
        continue