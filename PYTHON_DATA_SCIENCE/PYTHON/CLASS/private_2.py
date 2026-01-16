class Person : 
    __name = "aayush"

    def __hello(self):
        print("Hello my name is aayush pateriya and" \
        " I am a passionate freelancer in the field of data analyst")
    
    def welcome(self):
        self.__hello()
        print("Welcome to welcome method")

person = Person()
person.welcome()

# The private method will directly accessed by the another methods but it cannot be 
# accessed via object ....
