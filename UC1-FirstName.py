'''
@Author: Sai Tarun
@Date: 2022-04-26 12: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-26 13: 45: 00
@Title: Validate First Name.
'''

import re

class UserRegistration:

    def validate_firstname(self):
        """
        Description:
            Takes the first name and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns first name if its valid else returns message. 
        """
        first_name=input("Enter the first name:")
        #The leading ^(Not) and the trailing $(Dollar) are known as position anchors.
        #Which match the start and end positions of the line, respectively. 
        #First occurence of the patter at the entire string not only at beginning.
        #^[A-Z]{1}       [a-z]{2,}$
        match=re.search("^[A-Z]{1}[a-z]{2,}$",first_name)
        if match:
            return first_name
        else:
            return "Invalid first name."

if __name__=="__main__":
    ur=UserRegistration()
    print(ur.validate_firstname())