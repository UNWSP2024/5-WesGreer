# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


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
