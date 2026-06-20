'''                                 ATM Managment System                                      '''



class ATM :


    def __init__ (self) :
        self.pin = ''
        self.balance = 0



    def Create_PIN (Self) :
        user_Create_PIN = int(input("Enter the PIN : "))
        user_Create_Balance = int(input("Enter the Balance : "))
        print("Your PIN added successfully !...")
        print("Your Balance added successfully !...")

        Self.pin = user_Create_PIN
        Self.balance = user_Create_Balance



    def Change_PIN (self) :
        old_PIN = int(input("Enter the old PIN : "))
        
        if ( self.pin == old_PIN ) :
            user_Change_Pin = int(input("Enter the new PIN : "))
        else :
            print("Please enter the Correct PIN !...")

        self.pin = user_Change_Pin


    
    def Check_Balance (self) :
        old_PIN = int(input("Enter the old PIN : "))
        
        if ( self.pin == old_PIN ) :
            print("Currently your Balance is " , self.balance , ".rs")
        else :
            print("Please enter the Correct PIN !...")




class Cash_recyclers (ATM) :


    def Withdraw (self) :
        old_PIN = int(input("Enter the old PIN : "))
        
        if ( self.pin == old_PIN ) :
            if ( user_Withdraw < self.balance ) :
                user_Withdraw = int(input("Enter the Rupees how many do you want to Withdraw : "))
            else :
                print("You have enter more than your Balance !...")
        else :
            print("Please enter the Correct PIN !...")

        self.balance = self.balance - user_Withdraw



    def Deposite (self) :
        old_PIN = int(input("Enter the old PIN : "))
        
        if ( self.pin == old_PIN ) :
            user_Deposite = int(input("Enter the Rupees how many do you want to Deposite : "))
        else :
            print("Please enter the Correct PIN !...")

        self.balance = self.balance + user_Deposite




class Transction (Cash_recyclers) :


    def Transfer (self) :
        old_PIN = int(input("Enter the old PIN : "))
        
        if ( self.pin == old_PIN ) :
            user_Transfer = int(input("Enter the Rupees how many do you want to Transfer : "))
        else :
            print("Please enter the Correct PIN !...")

        self.balance = self.balance - user_Transfer



    def Mobile_recharge (self) :
        old_PIN = int(input("Enter the old PIN : "))
        
        if ( self.pin == old_PIN ) :
            user_Mobile_recharge = int(input("Enter the Rupees how many do you want to Transfer : "))
        else :
            print("Please enter the Correct PIN !...")

        self.balance = self.balance - user_Mobile_recharge



    def Light_bill (self) :
        old_PIN = int(input("Enter the old PIN : "))
        
        if ( self.pin == old_PIN ) :
            user_Light_bill = int(input("Enter the Rupees how many do you want to Transfer : "))
        else :
            print("Please enter the Correct PIN !...")

        self.balance = self.balance - user_Light_bill




class Main_Menu (Transction) :

    def Main_menu (self) :

        while True :

            user_input = input("""
        hii , How can i help you ?  \n
        1. Create PIN 
        2. Change PIN 
        3. Check Balance                    
        4. withdraw 
        5. Deposite
        6. Transfer
        7. Light Bill
        8. Mobile Recharge         \n
        Enter your choice : """)

            if ( user_input == '1' ) :
                self.Create_PIN()
            elif ( user_input == '2' ) :
                self.Change_PIN()
            elif ( user_input == '3' ) :
                self.Check_Balance()
            elif ( user_input == '4' ) :
                self.Withdraw()
            elif ( user_input == '5' ) :
                self.Deposite()
            elif ( user_input == '6' ) :
                self.Transfer()
            elif ( user_input == '7' ) :
                self.Light_bill()
            elif ( user_input == '8' ) :
                self.Mobile_recharge()
            elif ( user_input == '9' ) :
                print("\n\n Thank you to using the ATM System !...")
                break
            else :
                print("\n\n Please enter the valid input !...")




a = Main_Menu()
a.Main_menu()