# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:56:55 2022

@author: Aakash
"""
import random   
p=input('Enter select your weapon: rock, scissor or paper: ')
a=["rock","paper","scissor"]
cn= random.choice(a)

if p==cn:
    print(f"Both players selected {p}. It's a tie!")
elif p=="rock":
    if cn=="scissor":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif p=="paper":
    if cn=="rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif p=="scissor":
    if cn=="paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")