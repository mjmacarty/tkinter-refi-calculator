# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:02:37 2019

@author: Matt Macarty
"""

from tkinter import Entry, Label
import numpy as np

class LoanCalculator:

    def __init__(self):
        window = Tk()
        window.title("Refinance Evaluator")
        
        Label(window, text="Loan Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Interest rate").grid(row=2, column=1, sticky=W)
        Label(window, text="Term (years)").grid(row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4,column=1) # space between inputs and outputs
		
		
        Label(window, text="Payment:").grid(row=5, column=1, sticky=W)
        Label(window, text="Total Payments:").grid(row=6, column=1, sticky=W)
        
        # variables to store loan inputs
        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()

		# varianbles for loan outputs
        self.pmt = StringVar()
        self.total = StringVar() 
		
		# text boxes to hold inputs and outputs
        Entry(window, textvariable = self.pv,
              justify=RIGHT).grid(row=1,column=2, padx=(0,5))
        Entry(window, textvariable = self.interest_rate, 
              justify=RIGHT).grid(row=2,column=2, padx=(0,5))
        Entry(window, textvariable = self.term, 
              justify=RIGHT).grid(row=3,column=2, padx=(0,5))
        Label(window, textvariable = self.pmt, 
			font="Helvetica 12 bold", 
            justify=RIGHT).grid(row=5,column=2,sticky= E )
        Label(window, textvariable = self.total, 
			font="Helvetica 12 bold", 
            justify=RIGHT).grid(row=6,column=2, sticky= E)
        
        
        Button(window, text="Calculate Payment", command=self.calcPayment).grid(row=7,column=2, padx= (60,5), pady=5)
        
        
        # Refinance variables
        self.old_pmt = StringVar()
        self.time_left = StringVar()
        self.refi_cost = StringVar()
        
        # Refinance widgets
        Label(window, text="Current Payment").grid(row=8,column=1)
        Label(window, text="Time Left").grid(row=9,column=1)
        Label(window, text="Cost of Refi").grid(row=10,column=1)








        
        Entry(window, textvariable=self.old_pmt,
              justify=RIGHT).grid(row=8,column=2, padx=(0,5))
        Entry(window, textvariable=self.time_left,
              justify=RIGHT).grid(row=9,column=2, padx=(0,5))
        Entry(window, textvariable=self.refi_cost,
              justify=RIGHT).grid(row=10,column=2, padx=(0,5))
        
        # output variables for evaluation
        self.monthly_savings 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        