# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:55:56 2020
Password Encrypter by Paul
@author: Paul
"""
print ('Dies ist ein Passwort-Verschlüsseler, der ihr Passwort verschlüssen wird,')
print ('und es anschließend verschlüsselt wieder ausgibt.')
print ('Sie können jedes beliebige Passwort und auch andere Phrasen eingeben.')
print ()
print ('Anmerkung: Dies ist keine gute Verschlüsselung, und wurde nur zu Lernzwecken entwickelt.')
VarMulti= 1 #Variabler Multiplikator, mit der die einzelnen Zeichen multipliziert werden
numbers =[]
Hash=0
for x in input('Bitte geben sie ihr Passwort ein: '):
    number= ord (x) #Alle Zeichen des Passworts werden in Zahlenwerte umgewandelt
    number = number * 14 * 567 +25 * VarMulti #Diese Zahlenwerte werden mit Bestimmten Werten multipliziert
    VarMulti= VarMulti +1 #Der Variable Multiplikator wird um 1 ergänzt, um einen gleichen verschlüsselten Wert bei gleichen Zeichen zu vermeiden
    Hash = Hash + number #Die verschlüsselten Werte der einzelnen Zeichen werden zu einem endgültigen Wert addiert 
print(Hash) #Der endgültig verschlüsselte Wert ("Hash") wird ausgegeben. 
print('Es kann vorkommen, dass zwei Passwörter den selben "Hash" haben,')
print('aber dazu bedarf es sehr viel Glück ;)')
wait= input('Drücken sie Enter, um das Programm zu schließen.')