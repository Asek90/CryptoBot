from multiprocessing.connection import wait
from threading import Timer
import muuBotConfig
import muuBuy
#import sell
import sys
import time 

if muuBotConfig.w3.isConnected():
        print('')
        print('\|/          (__)     ')
        print('     `\------(oo)     ')
        print('       ||    (__)     ')
        print('       ||w--||     \|/')
        print('   \|/                ')
        print('  __  __ _   _ _   _   ____  _   _ ___ ____  _____   ____   ___ _____ ')
        print(' |  \/  | | | | | | | / ___|| \ | |_ _|  _ \| ____| | __ ) / _ \_   _|')
        print(' | |\/| | | | | | | | \___ \|  \| || || |_) |  _|   |  _ \| | | || |  ')
        print(' | |  | | |_| | |_| |  ___) | |\  || ||  __/| |___  | |_) | |_| || |  ')
        print(' |_|  |_|\___/ \___/  |____/|_| \_|___|_|   |_____| |____/ \___/ |_|  ')

#1)run loop to find pair
def execute():
    print("What would you like to do? [1]Buy [2]Sell")
    selectOption = input("")
    if selectOption == "1":
        muuBuy.address()
    #elif selectOption == "2":
       # print("You're going to sell ur bought tokens")
        #sell.sellMenu()
    else:
        execute()

execute()