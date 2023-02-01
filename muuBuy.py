import time
import muuBotConfig
import sys 
import threading

#2) check if pair has been created
def address():
    print("How much wMuu would you like to spend?")
    global toSpend
    toSpend = input("")
    print("What's Token Address you want to buy?")
    global tokenA
    tokenA = muuBotConfig.w3.toChecksumAddress(input('TokenAddress: '))
    all()
    
def all():
    try:
        threading.Thread(target=buy5).start()
        threading.Thread(target=buy6).start()
        threading.Thread(target=buy7).start()
        threading.Thread(target=buy8).start()
        threading.Thread(target=buy9).start()
        threading.Thread(target=buy10).start()
    except:
        address()

#8)Fifth wallet buy
def buy5():

#Transaction details
    pancakeswap2_txn5 = muuBotConfig.contractBuy.functions.swapExactETHForTokens(
    0,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [muuBotConfig.spend, tokenA],
    muuBotConfig.sender_address5,
    (int(time.time()) + 30000)
    ).buildTransaction({
    'from': muuBotConfig.sender_address5,
    'value': muuBotConfig.w3.toWei(toSpend, 'ether'),  # This is the Token(BNB) amount you want to Swap from
    'gas': 2000000,
    'gasPrice': muuBotConfig.w3.toWei(1, 'gwei'),
    'nonce': muuBotConfig.nonce5,
    })

    #Transaction sign
    signed_transaction5 = muuBotConfig.w3.eth.account.sign_transaction(pancakeswap2_txn5, muuBotConfig.private_key5)
    tx_token5 = muuBotConfig.w3.eth.send_raw_transaction(signed_transaction5.rawTransaction)
    time.sleep(10)
    print("Sniping succesfull, token bought. Txn: " + muuBotConfig.w3.toHex(tx_token5))
    sys.exit()
    
#9)Sixth wallet buy
def buy6():

    #Transaction details
    pancakeswap2_txn6 = muuBotConfig.contractBuy.functions.swapExactETHForTokens(
    0,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [muuBotConfig.spend, tokenA],
    muuBotConfig.sender_address6,
    (int(time.time()) + 30000)
    ).buildTransaction({
    'from': muuBotConfig.sender_address6,
    'value': muuBotConfig.w3.toWei(toSpend, 'ether'),  # This is the Token(BNB) amount you want to Swap from
    'gas': 2000000,
    'gasPrice': muuBotConfig.w3.toWei(1, 'gwei'),
    'nonce': muuBotConfig.nonce6,
    })

    #Transaction sign
    signed_transaction6 = muuBotConfig.w3.eth.account.sign_transaction(pancakeswap2_txn6, muuBotConfig.private_key6)
    tx_token6 = muuBotConfig.w3.eth.send_raw_transaction(signed_transaction6.rawTransaction)
    time.sleep(10)
    print("Sniping succesfull, token bought. Txn: " + muuBotConfig.w3.toHex(tx_token6))
    sys.exit()

#10)Seventh wallet buy
def buy7():

    #Transaction details
    pancakeswap2_txn7 = muuBotConfig.contractBuy.functions.swapExactETHForTokens(
    0,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [muuBotConfig.spend, tokenA],
    muuBotConfig.sender_address7,
    (int(time.time()) + 30000)
    ).buildTransaction({
    'from': muuBotConfig.sender_address7,
    'value': muuBotConfig.w3.toWei(toSpend, 'ether'),  # This is the Token(BNB) amount you want to Swap from
    'gas': 2000000,
    'gasPrice': muuBotConfig.w3.toWei(1, 'gwei'),
    'nonce': muuBotConfig.nonce7,
    })

    #Transaction sign
    signed_transaction7 = muuBotConfig.w3.eth.account.sign_transaction(pancakeswap2_txn7, muuBotConfig.private_key7)
    tx_token7 = muuBotConfig.w3.eth.send_raw_transaction(signed_transaction7.rawTransaction)
    time.sleep(10)
    print("Sniping succesfull, token bought. Txn: " + muuBotConfig.w3.toHex(tx_token7))
    sys.exit()

#11)Eighth wallet buy
def buy8():

    #Transaction details
    pancakeswap2_txn8 = muuBotConfig.contractBuy.functions.swapExactETHForTokens(
    0,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [muuBotConfig.spend, tokenA],
    muuBotConfig.sender_address8,
    (int(time.time()) + 30000)
    ).buildTransaction({
    'from': muuBotConfig.sender_address8,
    'value': muuBotConfig.w3.toWei(toSpend, 'ether'),  # This is the Token(BNB) amount you want to Swap from
    'gas': 2000000,
    'gasPrice': muuBotConfig.w3.toWei(1, 'gwei'),
    'nonce': muuBotConfig.nonce8,
    })

    #Transaction sign
    signed_transaction8 = muuBotConfig.w3.eth.account.sign_transaction(pancakeswap2_txn8, muuBotConfig.private_key8)
    tx_token8 = muuBotConfig.w3.eth.send_raw_transaction(signed_transaction8.rawTransaction)
    time.sleep(10)
    print("Sniping succesfull, token bought. Txn: " + muuBotConfig.w3.toHex(tx_token8))
    sys.exit()

#12)Nineth wallet buy
def buy9():

    #Transaction details
    pancakeswap2_txn9 = muuBotConfig.contractBuy.functions.swapExactETHForTokens(
    0,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [muuBotConfig.spend, tokenA],
    muuBotConfig.sender_address9,
    (int(time.time()) + 30000)
    ).buildTransaction({
    'from': muuBotConfig.sender_address9,
    'value': muuBotConfig.w3.toWei(toSpend, 'ether'),  # This is the Token(BNB) amount you want to Swap from
    'gas': 2000000,
    'gasPrice': muuBotConfig.w3.toWei(1, 'gwei'),
    'nonce': muuBotConfig.nonce9,
    })

    #Transaction sign
    signed_transaction9 = muuBotConfig.w3.eth.account.sign_transaction(pancakeswap2_txn9, muuBotConfig.private_key9)
    tx_token9 = muuBotConfig.w3.eth.send_raw_transaction(signed_transaction9.rawTransaction)
    time.sleep(10)
    print("Sniping succesfull, token bought. Txn: " + muuBotConfig.w3.toHex(tx_token9))
    sys.exit()

# #13)Tenth wallet buy
def buy10():

    #Transaction details
    pancakeswap2_txn10 = muuBotConfig.contractBuy.functions.swapExactETHForTokens(
    0,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [muuBotConfig.spend, tokenA],
    muuBotConfig.sender_address10,
    (int(time.time()) + 30000)
    ).buildTransaction({
    'from': muuBotConfig.sender_address10,
    'value': muuBotConfig.w3.toWei(toSpend, 'ether'),  # This is the Token(BNB) amount you want to Swap from
    'gas': 2000000,
    'gasPrice': muuBotConfig.w3.toWei(1, 'gwei'),
    'nonce': muuBotConfig.nonce10,
    })

    #Transaction sign
    signed_transaction10 = muuBotConfig.w3.eth.account.sign_transaction(pancakeswap2_txn10, muuBotConfig.private_key10)
    tx_token10 = muuBotConfig.w3.eth.send_raw_transaction(signed_transaction10.rawTransaction)
    time.sleep(10)
    print("Sniping succesfull, token bought. Txn: " + muuBotConfig.w3.toHex(tx_token10))
    sys.exit()