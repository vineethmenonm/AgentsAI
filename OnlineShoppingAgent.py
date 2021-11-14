"""
Created By: Vineeth Menon M
"""

import pandas as pd

class Environment(object):
    def __init__(self):
        # Reading the product Catalogue
        self.productData = pd.read_csv("ProductDetail.csv", header=0, 
                                       names=["Website","Item", "Company", "Price"])
        # Reading User Base
        self.users = ['vineeth', 'gokul']
        self.users = pd.DataFrame(self.users)

        # Retailers or companies
        self.uniqueRetailers = pd.DataFrame(self.productData.Company.unique())

class OnlineShoppingAgent(Environment):
    def __init__(self, environment):
        #Login Control
        self.loginSuccess = 0

        #Search Selection
        self.searchSelection = 0

        print("Online Shopping Agent Initiated...")
        self.username = input("Enter your Username: ")

        # Username Check
        self.UserCheckReturn = environment.users.eq(self.username).all(1)
        if True in self.UserCheckReturn.values:
            print("\nLogin Successful!  Welcome, ", self.username)
            self.loginSuccess = 1
        else:
            print("\nUser Not Found")

        # Upon Login Success:
        if(self.loginSuccess == 1):
            self.searchSelection = int(input("\nSelect Operations:\n1. Search per Brand\n2. Search by Item and Price\n"))

            # Use case for Brand Search (searchSelection == 1)
            if(self.searchSelection == 1):
                self.brandInput = input("\nEnter your Dezired Brand:\n")
                #Search for Brand in the preloaded data
                if(self.brandInput in environment.uniqueRetailers.values):
                    print("Brand Found!\nItem Catalog\n")
                    # Return the Items regarding the searched items
                    print(environment.productData.loc[environment.productData.Company == self.brandInput])
                # No Available Brands in the catalogue
                else:
                    print("Brand Not Found!, Available Brands are:\n")
                    # Return the Retailers available
                    print(environment.uniqueRetailers, "\n")
                    #print(environment.productData)

            # Use Case for Price search (searchSelection == 2)
            if(self.searchSelection ==2):
                print(environment.productData.Item.unique())
                self.itemInput = input("\nEnter an item from the above list: ")
                self.inputPrice = input("\nEnter the dezired price: ")
                # Get list of items that are input by the customer and also equal to the price given
                self.equalDF = environment.productData[(environment.productData['Price'] == int(self.inputPrice)) &
                                                         (environment.productData['Item'] == self.itemInput)]
                # Get list of items that are input by the customer and also greater than price given
                self.greaterDF = environment.productData[(environment.productData['Price'] > int(self.inputPrice)) &
                                                         (environment.productData['Item'] == self.itemInput)]
                # Get list of items that are input by the customer and also lesser than price given
                self.lesserDF = environment.productData[(environment.productData['Price'] < int(self.inputPrice)) &
                                                       (environment.productData['Item'] == self.itemInput)]

                # If Exact Search doesnt match
                if (self.equalDF.empty == True):
                    print("\n Products are not available with the exact amount that you are looking for\n Suggesting other options.....")

                # If exact search Matches
                if(self.equalDF.empty == False):
                    print("\n Products are available with the exact amount that you are looking for\n")
                    print(self.equalDF)

                # If the item and Price range does not match, show the rest of the catalogue:
                else:
                    if(self.lesserDF.empty == False):
                        print("\n The items that are less than your dezired price range found:\n")
                        print(self.lesserDF)
                    if(self.greaterDF.empty == False):
                        print("\n The items that are greated than your dezired price range found:\n")
                        print(self.greaterDF)
                    else:
                        print("\nSorry, We cannot satisfy your criteria now!")

environ = Environment()
OSA = OnlineShoppingAgent(environ)
