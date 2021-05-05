import pyrebase
import urllib

class Database_Firebase:
    def __init__(self):
        firebaseConfig = {'apiKey': "AIzaSyDu-oQIpSK_DvSX4iIn32pK5E1NpZJh8bM",
                        'authDomain': "test-tetris-d3c6c.firebaseapp.com",
                        'projectId': "test-tetris-d3c6c",
                        'storageBucket': "test-tetris-d3c6c.appspot.com",
                        'messagingSenderId': "740057139345",
                        'appId': "1:740057139345:web:4baceed71fd43d07d81730",
                        'measurementId': "G-7028VEFBW4",
                        'databaseURL':'https://test-tetris-d3c6c-default-rtdb.firebaseio.com/'}

        firebase = pyrebase.initialize_app(firebaseConfig)
        self.person_db = firebase.database()
        self.person_auth = firebase.auth()

    def sing_up(self):
        email = input("Enter your email")
        password = input("Enter your password")
        confirmpass = input("Confirm password")
        if password == confirmpass:
            try:
                self.person_auth.create_user_with_email_and_password(email, password)
                print("Success")
            except:
                print("Email already exists")

    def log_in(self):
        email = input("Enter your email")
        password = input("Enter your password")
        try:
            self.person_auth.sign_in_with_email_and_password(email, password)
            print("Successfully signed in!")
        except:
            print("Invalid User or Password. Try again.")

    def create_data_in_firebase(self,email,character,level,exp):
        data = {'email':email,'character':character,'level':level,'exp':exp}
        self.person_db.child("User").child("user2").set(data)

    def update_data_in_firebase(self,email,level,exp):
        users = self.person_db.child("User").get()
        for user in users.each():
            if user.val()['email'] == email:
                self.person_db.child("User").child(user.key()).update({'level': level,'exp':exp})








