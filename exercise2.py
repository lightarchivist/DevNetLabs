
#validate isdn
def islISBN():

    #enter string for check
    pattern = input("Enter a string: ")
    
    # separate by '-' 
    pattern = pattern.split('-')
    
    #check if eac element is a number
    for p in pattern:
        if not p.isdigit():
            print("False")
            return False
        
    
    if len(str(pattern[0]))==3 and len(str(pattern[1]))==1 and len(str(pattern[2]))==2 and len(str(pattern[3]))==6 and len(str(pattern[4]))==1:
        print("TRUE")
        return True
    
    print("False")
    return False
 
    
islISBN()
    