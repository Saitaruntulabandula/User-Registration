import unittest

from UserRegistration import UserRegistration

ur=UserRegistration()

class TestFirstName(unittest.TestCase):
    #Starts with capital letter and minimum 3 chars.
    def test_validate_firstname(self):
        self.assertEqual(ur.validate_firstname("Tarun"),"Tarun")
        self.assertNotEqual(ur.validate_firstname("Arjun"),"Ram")
        self.assertEqual(ur.validate_firstname("Rajkumar"),"Rajkumar")
        self.assertNotEqual(ur.validate_firstname("Prem"),"Prakash")
        self.assertEqual(ur.validate_firstname("Nanda"),"Nanda")
        self.assertNotEqual(ur.validate_firstname("Sravan"),"Naveen")
        self.assertEqual(ur.validate_firstname("Swetha"),"Swetha")
        self.assertNotEqual(ur.validate_firstname("Sowmya"),"Sruthi")

    #Starts with capital letter and minimum 3 chars.
    def test_validate_lastname(self):
        self.assertEqual(len(ur.validate_lastname("Sunny")),5)
        self.assertNotEqual(len(ur.validate_lastname("Sai Kiran")),5)
        self.assertEqual(len(ur.validate_lastname("Ravali")),6)
        self.assertNotEqual(len(ur.validate_lastname("Ram")),2)
        self.assertEqual(len(ur.validate_lastname("Yeswitha")),8)
        self.assertNotEqual(len(ur.validate_lastname("Anil")),3)
        self.assertEqual(len(ur.validate_lastname("Prasanna")),8)
        self.assertNotEqual(len(ur.validate_lastname("Ashok")),4)

    def test_validate_email(self):
        if ur.validate_email("sai@bl.co")!="Invalid email id":
            self.assertTrue(True,True)
        value=ur.validate_email("s@bl.co")
        if ur.validate_email("sai@bl.co")=="Invalid email id":
            self.assertFalse(False,True)

        if ur.validate_email("raj.100@google.com")!="Invalid email id":
            self.assertTrue(True,True)
        value=ur.validate_email("s@bl.co")
        if ur.validate_email("abc123@.com.com")=="Invalid email id":
            self.assertFalse(False,True)

    #Country code followed by 10 digit-phone number.
    def test_validate_phnumber(self):
        valid_phn_num="+91 8686545392"
        invalid_phn_num="91 756547856"
        self.assertEqual(len(ur.validate_phnumber(valid_phn_num)),14)
        self.assertNotEqual(len(ur.validate_phnumber(invalid_phn_num)),14)
        valid_phn_num="91 8686545392"
        invalid_phn_num="91 75654785671"
        self.assertEqual(len(ur.validate_phnumber(valid_phn_num)),13)
        self.assertNotEqual(len(ur.validate_phnumber(invalid_phn_num)),14)
        valid_phn_num="+91 9247320014"
        invalid_phn_num="-91 756547856"
        self.assertEqual(len(ur.validate_phnumber(valid_phn_num)),14)
        self.assertNotEqual(len(ur.validate_phnumber(invalid_phn_num)),14)
        valid_phn_num="+91 9234567890"
        invalid_phn_num="911275654785"
        self.assertEqual(len(ur.validate_phnumber(valid_phn_num)),14)
        self.assertNotEqual(len(ur.validate_phnumber(invalid_phn_num)),14)
    
    #Minimum 8 characters.
    def test_validate_password1(self):
        self.assertEqual(len(ur.validate_password1("Saitarun")),8)
        self.assertNotEqual(len(ur.validate_password1("saita")),8)
        self.assertEqual(len(ur.validate_password1("Rajkumar")),8)
        self.assertNotEqual(len(ur.validate_password1("ramu")),8)
        self.assertEqual(len(ur.validate_password1("Yeswitha")),8)
        self.assertNotEqual(len(ur.validate_password1("ravali")),8)
        self.assertEqual(len(ur.validate_password1("Prasanth")),8)
        self.assertNotEqual(len(ur.validate_password1("prem")),8)

    #Should have atleast one upper case
    def test_validate_password2(self):
        input=ur.validate_password2("Rajkumar")
        if input[0].isupper() and len(input)>=8:
            valid_input=True
        else:
            valid_input=False
        self.assertTrue(valid_input,True)

        input1=ur.validate_password2("ramu")
        if input1[0].isupper() and len(input1)>=8:
            valid_input=True
        else:
            valid_input=False
        self.assertFalse(valid_input,True)

        self.assertEqual(len(ur.validate_password2("Arjunrao")),8)
        self.assertNotEqual(len(ur.validate_password2("ramu")),8)
        self.assertEqual(len(ur.validate_password2("Aravinda")),8)
        self.assertNotEqual(len(ur.validate_password2("ravali")),8)
        self.assertEqual(len(ur.validate_password2("Shelarao")),8)
        self.assertNotEqual(len(ur.validate_password2("prem")),8)
        self.assertEqual(len(ur.validate_password2("Chaithra")),8)
        self.assertNotEqual(len(ur.validate_password2("ashok")),8)
        
    #Sholud had atleast one numeric character.
    def test_validate_password3(self):
        input=ur.validate_password3("Aravinda4")
        for i in range(len(input)):
            if input[0].isupper() and len(input)>=8 and input[i].isdigit():
                valid_input=True
            else:
                valid_input=False

        self.assertTrue(valid_input,True)

        input1=ur.validate_password3("ramu")
        for i in range(len(input)):
            if input1[0].isupper() and len(input1)>=8 and input1[i].isdigit():
                valid_input=True
            else:
                valid_input=False
        self.assertFalse(valid_input,True)
    
    #Should contain atleast one special charcter.
    def test_validate_password4(self):
        self.assertEqual(len(ur.validate_password4("Taruns]4")),8)
        self.assertNotEqual(len(ur.validate_password4("ramu")),8)
        self.assertEqual(len(ur.validate_password4("Aravi3d[")),8)
        self.assertNotEqual(len(ur.validate_password4("ravali")),8)
        self.assertEqual(len(ur.validate_password4("Shela5a|")),8)
        self.assertNotEqual(len(ur.validate_password4("prem")),8)
        self.assertEqual(len(ur.validate_password4("Chai6hr?")),8)
        self.assertNotEqual(len(ur.validate_password4("ashok")),8)
        

if __name__=="__main__":
    unittest.main()