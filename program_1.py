# kilometer conversion program
# written by Wesley Greer on 2/17/2026


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
    def miles_to_km():
        print("Give me a number of miles, and I will convert it to kilometers.")
        miles = float(input("What is the number of miles? "))
        km = miles * 0.6214
        print(f'{miles} miles is equal to {km:.4f} kilometers.')

    miles_to_km()
    ######################    


    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    
    # Display the miles
