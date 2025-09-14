# Match case statements(switch): AN alternative to using many elif statements
#                               Execute some code if a c=vaue matches a case
#                               Benefirs: cleaner code, easier to read, faster execution

#day = int(input("Enter a day number (1-7): "))
#def day_of_week(day):
#    match day:
#        case 1:
#            return "Monday"
#        case 2:
#            return "Tuesday"
#        case 3:
#            return "Wednesday"
#            return "Thursday"
#            return "Friday"
 #       case 6:
#            return "Saturday"
#        case 7:
#            return "Sunday"
#        case _:
#            return "Invalid day"
        
#print(day_of_week(day))  # Output: Wednesday





def is_weekend(day):
    match day:
        case "saturday"|"Sunday":
            return True 
        case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
            return False
        case _:
            return "Invalid day"
print(is_weekend("saturday"))