from abc import ABC, abstractmethod
from users import *
from products import *
#Write your code here

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    cashiers = []
    for _, row in dataFrame.iterrows():
      cashiers.append(Cashier(str(row["dni"]), row["name"], int(row["age"]), row["timetable"], float(row["salary"])))
      return cashiers

class CustomerConverter(Converter):
  def convert(self,dataFrame):    
    customers = []
    for _, row in dataFrame.iterrows():
      customers.append(Customer(str(row["dni"]), row["name"], int(row["age"]), row["email"], row["postalcode"]))
      return customers

class ProductConverter(Converter):
    def convert(self, dataFrame, *args):
        productClass = args[0]
        products = []
        for _, row in dataFrame.iterrows():
            products.append(productClass(str(row["id"]), row["name"], float(row["price"])))
        return products
