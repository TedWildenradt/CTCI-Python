import hashlib
def sha1(text):
  s = hashlib.sha1()
  s.update(text.encode('utf-8'))
  return s.hexdigest()

x = sha1("0000000000000000000000000000000000000000, 28427, [[0, 1, 5], [1, 2, 5]]")
sha1('1')
y = len(x)
'''
Given arrays representing startBalances and pendingTransactions and the integer blockSize, create a blockchain[1] that includes all valid pending transactions in the order in which they are given and return the last block.

Blocks
Blocks are encoded as strings of the form:
"blockHash, prevBlockHash, nonce, blockTransactions"

blockHash: The value returned by sha1(“prevBlockHash, nonce, transactions”)[2], e.g. sha1("0000000000000000000000000000000000000000, 28427, [[0, 1, 5], [1, 2, 5]]").
prevBlockHash: The blockHash of the previous block. Should be 0000000000000000000000000000000000000000 for the first block.
nonce: The lowest integer for which the first four characters of blockHash are equal to 0000
blockTransactions: A string encoded representation of the transactions included in this block. Each individual transaction takes the form [fromAddress, toAddress, value], where fromAddress, toAddress, and value are each integers, e.g. [0, 1, 5].
Each block should have blockSize transactions if there are >= blockSize transactions that have yet to be included in a block. If there are fewer than blockSize transactions remaining, all remaining transactions should be included in the final block.

Transactions
A transaction ti is valid if the address at from has a balance >= value after processing all transactions tj for which j < i. Some transactions in pendingTransactions may be invalid. These transactions should be omitted from all blocks. You can assume that from and to will have entries in startBalances.

Example
getLastBlock([5, 0, 0], [[0, 1, 5], [1, 2, 5]], 2) = "00000d03a1ce56a06bfdbceb0249bbb2204a6f22, 0000000000000000000000000000000000000000, 28427, [[0, 1, 5], [1, 2, 5]]"

Notes
[1] A blockchain is an immutable linked list of ‘blocks’, each containing up to 5 valid transactions. Each block is linked to the previous block via a cryptographic hash rather than a pointer. The global state of each account can be derived by examining the entire chain. More information about the structure and content of a block can be found in the 'Blocks' section.
[2] Below are some examples of how to run sha1 in popular languages, we recommend that you copy paste this code into your solution.
'''