In this Chapter, The technical aspects of blockchain and how it works.
Let me give you a brief explanation of the clever solutions employed by blockchain technology.

This is what a blockchain looks like.
Each block holds a list of public transactions and every block is linked to the previous one by these hash values, as you can see.

Block number two holds the proof of work code from block number one and so on.
Now, remember the transaction John wanted to make with Sarah.

Here's how it would work.
John opens a new transaction with some details like their wallet addresses and the amount to be transferred.
The wallet address, which is also called the Public Key, is linked to a private key that only the
owner has access to, but it is done in a way that any node in the network can verify if the link is
valid.  

This is a type of digital signature. Once the transaction is created, it is then broadcast to the network.
It is eventually added to a block containing multiple other transactions.
Then the people that work to maintain the blockchain,   which are called miners. We work to validate the transactions.
Since everything in the blockchain is public, the miners can easily verify if John and the other senders are actually the owners of the wallets and that they have sufficient funds for the transactions.

Once the transactions have been validated, the miners will compete to solve a complex mathematical puzzle that demands a huge amount of computational power.

The first miner who solves it adds the solution to the block in the Bitcoin network.
This solution is called the proof of work. The miner then adds the new block to the blockchain and is rewarded with Bitcoin for his work.
This is how miners make money or bitcoins. The other miners can easily validate the solution and all transactions in the new block in order to
confirm the update in the chain.

So this was a brief explanation of how a blockchain system works. Now Three common questions people often ask about blockchain security.

Number one, what prevents a malicious node from adding fake transactions to a block?
All nodes can easily validate all transactions in a block, so any invalid transaction would make the new block automatically rejected by the other nodes.

Number two, Why can anyone alter or delete retroactive data on the blockchain?
That's because the link between the blocks makes it impossible to alter data, as all puzzles would have to be solved again, requiring an impossible amount of computational power.

Number three What prevents someone from spamming the network with millions of fake blocks?
Remember that to send the new block to the chain, the miner must spend computational power to solve the complex mathematical puzzle.

So this makes it economically unfeasible to create and validate a large number of fake blocks.
We can then conclude that the utilization of mathematical and cryptographic functions in these solutions
enables the establishment of a secure and decentralized network, which is the backbone of Web3.  

 creating decentralized apps (dApps) that run on the blockchain

