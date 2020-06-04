class Author():

  def __init__(self,name,email,gender):
    self.name = name
    self.email = email
    self.gender = gender
  
  def getName(self):
    return f"Name-{self.name}"

  def getEmail(self):
    return f"Email-{self.email}"

  def setEmail(newEmail):
    self.email = newEmail
    return f"New email-{self.email}"
  
  def getGender(self):
    return self.gender
  
  def toString(self):
    return f"Author[name={self.name},email={self.email},gender={self.gender}]"
  
author = Author("Tan Ah Teck","ahTeck@somewhere.com","m")
print(author.toString())