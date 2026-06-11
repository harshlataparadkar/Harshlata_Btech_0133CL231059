class UnderAgeError(Exception):
      pass
class InvalidAgeError(Exception):
      pass
class AgeVerification:
    def set_age(self,age):
            try:
                if age<0:
                      raise ValueError("age cannot be -ve")
                elif age < 18:
                      raise UnderAgeError("Under age")
                elif age > 100:
                      raise InvalidAgeError ("invalid age")
                else:
                      print("Valid age")
            except ValueError as e:
                  print(e)
                
obj = AgeVerification()
obj.set_age(int(input("Enter age:")))
        
