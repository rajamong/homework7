# creates a program to check whether a year is a leap year
def leapyear(year):
                # if the year is evenly divisible by 4
        if (year % 4) == 0:
                # if the year is evenly divisible by 100
                if (year % 100) == 0:
                        # if the year is evenly divisible by 400
                        if (year % 400) == 0:
                                return "True"
                        else:
                                return "False"
                else:
                        return "True"
        else:
                return "False"

