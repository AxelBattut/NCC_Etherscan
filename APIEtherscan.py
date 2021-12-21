# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:59:35 2021

@author: SESSIONSOUFIANE
"""

import requests

address = "0xbccf9f2b76c7e2460d0acb9763ae8b779675e568"
"""
put the adress that you are looking for here 
"""

url = "http://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=YourApiKeyToken"

response = requests.get(url)
address_content =response.json()
result = address_content.get("result")

for n, transaction in enumerate(result):
    hash = transaction.get("hash")
    tx_from = transaction.get("from")
    tx_to = transaction.get("to")
    value = transaction.get("value")
    confirmations = transaction.get("confirmations")
    
    
    print("Transaction ID : ", n)
    print("hash : ", hash)
    print("from : ", tx_from)
    print("to : ", tx_to)
    print("value : ", value)
    print("confirmations : ", confirmations)