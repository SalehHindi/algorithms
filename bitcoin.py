'''
Alice sends money to Bob
  Alice has private key
  Uses private key to generate public key (SendTo Address) for every transaction
  Pub Key + Message = Sig. Sig authenticates the transaction
    Uses Elliptic Curve Digital Signature Algorithm
    Uses Mathematical Trap Door
  To send money, you must have your private key
  To receive money you must have their public key
All the miners mark this transaction in their ledger
When you first download bitcoin wallet software you must verify all the transactions ever passed
Nodes must check every transaction ever made for every input to make sure it is unspent
  This is made easier with an index of unspent nodes

Your Balance = All the inputs sent to you that have not been spent ie sent out

Send Money = Take unspent transactions until they total near the money you want to send. Any left
over is sent to you

When you
'''

import hashlib
import random

for i in range(100000000):
    m=hashlib.sha256()
    m.update(str(random.random()))
    hash=m.hexdigest()
    numbers=6
    #let numbers=4 for speedy results

    for a in range(numbers):
        if hash[a]=='0':
            numbers-=1
    if not numbers:
        print i, "||", m.hexdigest()
