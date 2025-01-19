#Initializations
lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_case_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
under_score = '_'

digit = '0123456789'

# Function valid_First_Char(string) returns True if first char in identifier is a letter else returns False
def valid_First_Char(string):
    return (string[0] in lower_case_alphabet) or (string[0] in upper_case_alphabet) or (string[0]=='_')

#Function valid_Non_First_Char(kar) returns True if a character from the 2nd position onwards is an upper or lower case
#letter or an underscore character or a character representing a single digit
def valid_Non_First_Char(kar):
    
    return (kar in lower_case_alphabet) or (kar in upper_case_alphabet) or (kar in digit) or (kar == under_score)


#The function iS_It_A_Valid_Identifier(string) returns True if string is a valid identifier;
#else returns False
#The function assumes that string is a valid identifier initially (invalid_Identifier=False)
#if any of the rules for string to be a valid identifier is found to be violated, the function
#returns False
def iS_It_A_Valid_Python_Identifier(string):
    
    #invalid_Identifier=False
    
    if valid_First_Char(string):
        
        i=1
        while  (i<len(string)):
            if valid_Non_First_Char(string[i]):
                i=i+1
            else:
                break;
        return (i==len(string))          
    else:
        return False
    
    return (i==len(string))
  #  if (not invalid_Identifier):
  #      return True
  #  else:
  #      return False
  #
