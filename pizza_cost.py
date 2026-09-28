#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 2008 18
# Calculates cost of producing a pizza 
import constants
def main():
    #gets diameter from user
    Diameter=int(input("Enter the diameter of the pizza (inches):"))
    #calculates Subtotal, Tax, Total.
    Subtotal=constants.LABOUR+constants.RENTAL+Diameter*constants.ING_COST
    Tax=constants.HST*Subtotal
    Total=Tax+Subtotal
    #Displays total cost of pizza
    print("the total cost of a pizza with diameter {} inches is ${:,.2f}" . format(Diameter, Total))
if __name__ == "__main__":

    main()