'''
@Author: Sai Tarun
@Date: 2022-04-26 20: 50: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-26 21: 20: 00
@Title: Validate Password Rule 4.
'''
import re

class UserRegistration:

    def validate_firstname(self,first_name):
        """
        Description:
            Takes the first name and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns first name if its valid else returns message. 
        """
        #first_name=input("Enter the first name:")
        #The leading ^(Not) and the trailing $(Dollar) are known as position anchors.
        #Which match the start and end positions of the line, respectively.
        val_firstname="^[A-Z]{1}[a-z]{2,}$" 
        match=re.search(val_firstname,first_name)
        if match:
            return first_name
        else:
            return "Invalid first name."

    def validate_lastname(self,last_name):
        """
        Description:
            Takes the last name and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns last name if its valid else returns message. 
        """
        #last_name=input("Enter the last name:")
        match=re.search("^[A-Z]{1}[a-z]{2,}$",last_name)
        if match:
            return last_name
        else:
            return "Invalid last name."

    def validate_email(self,email_id):
        """
        Description:
            Takes the email id and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns email id if its valid else returns message. 
        """
        #email_id=input("Enter the email id:")
        match=re.search("^\w{3,}(\.\w{3,})*\@[a-z]{2,}\.[a-z]{2,3}(\.[a-z]{2})*$",email_id)
        if match:
            return email_id
        else:
            return "Invalid email id"

    def validate_phnumber(self,phone_number):
        """
        Description:
            Takes the phone number and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns phone number if its valid else returns message. 
        """
        #phone_number=input("Enter the phone number:")
        match=re.search("^(\\+91|91)[ ]{1}[6-9]{1}[0-9]{9}$",phone_number)
        if match:
            return phone_number
        else:
            return "Invalid Phone Number"
    def validate_password1(self,password):
        """
        Description:
            Takes the password and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns password if its valid else returns message. 
        """
        #password=input("Enter the password:")
                        #Minimum length is 8.
                        #^[A-Za-z-0-9_]  {8,}$  we can use \w also for alphanumeric chars.
        print
        match=re.search("^[A-Za-z-0-9]{8,}$",password)
        if match:
            return password
        else:
            return "Invalid Password"

    def validate_password2(self,password):
        """
        Description:
            Takes the password and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns password if its valid else returns message. 
        """
        #password=input("Enter the password:")
                        #Atleast had one Capital Letter.
                        #^(?=.*[A-Z])   .{8,}$
        match=re.search("^(?=.*[A-Z]).{8,}$",password)
        if match:
            return password
        else:
            return "invalid Password"

    def validate_password3(self,password):
        """
        Description:
            Takes the password and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns password if its valid else returns message. 
        """
        #password=input("Enter the password:")
        #Atleast had one Numeric number.
        #(?=.*[A-Z])        (?=.*[0-9])     .{8,}$
        match=re.search("(?=.*[A-Z])(?=.*[0-9]).{8,}$",password)
        if match:
            return password
        else:
            return "invalid Password"

    def validate_password4(self,password):
        """
        Description:
            Takes the password and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns password if its valid else returns message. 
        """
        #password=input("Enter the password:")
        #Atleast had one Special character. 
        #[].^$*+?{}()\| #\W-Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
        #(?=.*[A-Z])        (?=.*\d)        (?=.*\W)        .{8,}$
        match=re.search("(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$",password)
        if match:
            return password
        else:
            return "Invalid Password"

if __name__=="__main__":
    ur=UserRegistration()
    #print(ur.validate_firstname())
    #print(ur.validate_lastname())
    #print(ur.validate_email())
    #print(ur.validate_phnumber())
    print(ur.validate_password())