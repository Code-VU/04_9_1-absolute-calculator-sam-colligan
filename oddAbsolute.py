def calculateAbsolute():
    
    # This first line is provided for you
     
     input_num  = input("Enter a number: ")
    
     if int(input_num) > 21:
        diff = abs((int(input_num) - 21) * 2)
     else:
        diff = abs(int(input_num) - 21)

     print("Result:", diff)

if __name__ == "__main__":
    calculateAbsolute()


## If you want to test locally run > python payCalculator.py

