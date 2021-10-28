# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:55:56 2020
Password Encrypter by Paul
@author: Paul
"""
print ('This is a basic Password-Encrypter,which takes your password,')
print ('and shows it encrypted.')
print ('You can type in every password and also other phrases.')
print ()
print ('Note: This is not a good encryption, its for educational purposes only and a proof of concept.')
VarMulti= 1 #variable multiplier
numbers =[]
Hash=0
for x in input('Please type in your password: '):
    number= ord (x) #All charakters of the entered Phrase are converted to Numbers
    number = number * 14 * 567 +25 * VarMulti #These Numbers are multiplied with some fixed Values
    VarMulti= VarMulti +1 #1 is added to the variable multiplier ,to prevent the "hash" being the same with same charakters
    Hash = Hash + number #The encrypted charakters are added to a cumulative value
print(Hash) #The final encrypted value ("Hash") is being displayed
print('It can be possible that to passwords have the same "Hash"')
wait= input('Press Enter to close the Program')