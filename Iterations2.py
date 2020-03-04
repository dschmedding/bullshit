while True:
        try:
            gross = input("How much are you making?")
            gross = int(gross)
            if gross < 1000:
                    tax = 0.1
            elif gross < 2000:
                tax = 0.2
            elif gross < 4000:
                tax = 0.4
            else:
                tax = 0.14
            break

        except:
                print ("that was not a good gross")