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

class Book(Author):

  def __init__(self,name_book,author,price,qty):
    self.bookName = name_book
    self.price = price
    self.qty = qty

  def getName(self):
    return f"Book-{self.bookName}"

  def getAuthor(self):
    return f"Author name-{author.name}"

  def getPrice(self):
    return f"Price-{self.price}"

  def setPrice(self,newPrice):
    self.price = newPrice
    return f"New price-{self.price}"

  def getQty(self):
    return f"Qty-{self.qty}"

  def setQty(self,newQty):
    self.setQty = newQty
    return f"New Qty-{self.qty}"

  def toString(self):
    return f"Book[name={self.bookName},Author[name={author.name},email={author.email},gender={author.gender},price={self.price},qty={self.qty}]"

book = Book("Tan",author,2.5,3)
print(book.toString())