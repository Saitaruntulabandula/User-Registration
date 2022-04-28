'''
@Author: Sai Tarun
@Date: 2022-04-26 14: 20: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-26 15: 15: 00
@Title: Validate Email.
'''
import re

class UserRegistration:
    def validate_email(self,email_id):
        """
        Description:
            Takes the email id and validates it.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns email id if its valid else returns message. 
        """
        #email_id=input("Enter the email id:")     # 2 or 3 char len  #* zero or more occurences.
                        #abc         #.xyz          #@bl           #.co            #.in
                        #^\w{3,}     (\.\w{3,})*    \@[a-z]{2,}    \.[a-z]{2,3}    (\.[a-z]{2})* $
        match=re.search("^\w{3,}(\.\w{3,})*\@[a-z]{2,}\.[a-z]{2,3}(\.[a-z]{2})*$",email_id)
                        #abc.xyz@bl.co.in #abc@bl.co
        if match:
            return email_id
        else:
            return "Invalid email id"

if __name__=="__main__":
    ur=UserRegistration()
    valid_emails=["ram@yahoo.com", "raj.100@google.com","ravi.sai@hotmail.com",
                  "siva.111@abc.com","abc.bin@abc.net", "abc.100@abc.com.au"]
    invalid_emails=["abc","abc@.com.my", "abc123@gmail.a", "abc123@.com",
                    "abc123@.com.com", ".abc@abc.com", "abc()*@gmail.com",
                    "abc@%*.com", "abc..2002@gmail.com", "abc@1.com", "abc.@gmail.com",
                    "abc@abc@gmail.com", "abc@gmail.com.1a", "abc@gmail.com.aa.au"]
    print("********List of valid email id's********")
    for email in valid_emails:
        print(ur.validate_email(email))
    print("********List of invalid email id's********")
    for email in invalid_emails:
        print(ur.validate_email(email))
    