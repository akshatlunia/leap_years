print("Type only the integer year that you wish to check for leap year")
year = input()
yearInt = int(year)
if(yearInt%400 == 0):
    print("The year",yearInt,"is a 400-year leap year")
else:
    if(yearInt%100 == 0):
        print("The year",yearInt,"is not a leap year")
        import sys
        sys.exit()
    else:
        if(yearInt%4 == 0):
            print("The year",yearInt,"is a leap year")
            import sys
            sys.exit()
        else:
            print("The year",yearInt,"is not a leap year")
