# creates a function called fizzbuzz
def fizzbuzz(number):
    # if the number is evenly divisible by 5 and 3
    if number % 5 == 0 and number % 3 == 0:
        # print FizzBuzz
        return "FizzBuzz"

    # if the number if evenly divisible by 5
    if number % 5 == 0:
        #print Buzz
        return "Buzz"

    # if the number is evenly divisible by 3
    if number % 3 == 0:
        # print Fizz
        return "Fizz"

    # if the number is neither evenly divisible by 5 or 3  
    if number % 3 != 0 and number % 5 != 0:
        # print out the number
        return number


