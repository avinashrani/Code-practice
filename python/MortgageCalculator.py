#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:37:43 2017

@author: avinashrani
"""

class Mortgage(object):
    
    """Abstract class for building mortgage models"""
    
    def __init__(self, cost, rate, years):
        """Create new mortgage calc using inputs: Loan, Annual Rate of Interest, Years"""
        self.cost = cost
        self.rate = rate/12.0
        self.paid = [0]
        self.n = years*12
        self.remBalance = []
        self.intPayment = []
        self.principal = []
        
    def downPayment(self):
        """ Calculates the initial costs involved"""
        
        closingCostPercentage = 0.025
        downPaymentPercentage = 0.2
        closingCost = closingCostPercentage*self.cost
        downPayment = (self.cost+closingCost)*downPaymentPercentage
        
        return downPayment
        
    def loan(self):
        """Calculates the loan amount, including closing costs"""
        loan = self.cost - self.downPayment()
        
        return loan
        
    def findPayment(self):
        """ Calculates fixed monthly payment to be made"""
        
        Payment = self.loan()*(self.rate*((1+self.rate)**self.n))/((1+self.rate)**self.n - 1)
        
        return Payment
    
    def balance(self):
        """Calculates balance at the end of every month for the term loan"""
        
        uB = self.loan() - self.findPayment()
        self.remBalance.append(uB)
        interest = uB*(self.rate)
        self.intPayment.append(interest)
        
        for period in range(1,self.n):
            nB = uB + self.rate*uB
            uB = nB - self.findPayment()
            interest = uB*self.rate
            self.remBalance.append(uB)
            self.intPayment.append(interest)
            period += 1
            p = self.findPayment() - interest
            self.principal.append(p)
            
        return self.remBalance
    
    def propTax(self , propRate):
        """ Calculates Property Tax per month, given annual rate"""
        self.propRate = propRate
        annualPropTax = self.cost*self.propRate
        
        return annualPropTax
    
    def monthlyPayment(self):
        """ Total monthly payments to be made, including:
            1. Mortgage Payment
            2. Property Tax
            3 HOA
            4. Maintenence
            5. Homeowners Insurance"""
            
        hoa = 50
        maint = 100
        insurance = 150
        
        monthlyPayment = self.findPayment() + self.propTax(0.0125)/12 + hoa + maint + insurance
        
        return monthlyPayment
    
    def equity(self):
        """ Calculates the equity in the house per period
        doubt : when i run this file, and call m1.equity(), it returns an empty list,
        which means that it self.principal is an empty list, which means that it did not compute
        m1.balance(). but when i call m1.balance() first and then call m1.equity(), its returns 
        the correct output. why is m1.balance() not returning a value when i call m1.equity()??
        """
        
        equity = []
        monthlyEquity = self.downPayment()
        for i in self.principal:
            temp1 = i + monthlyEquity
            monthlyEquity = temp1
            equity.append(monthlyEquity)
        
        return equity
    
    def percentEquity(self):
        """Returns percent equity owned on the house at the end of every month"""
        percentEquity = []
        for i in self.equity():
            pE = i / self.cost
            percentEquity.append(pE)
            
        return percentEquity
            
            
            
            
    
        
    
    
m1 = Mortgage(400000,0.04,30)
#import matplotlib.pyplot as plt
#plt.figure(1,)
#plt.plot(m1.balance())
#plt.figure(2)
#plt.plot(m1.intPayment)
#plt.figure(3)
#plt.plot(m1.equity())


      