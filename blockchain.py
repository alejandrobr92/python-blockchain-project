blockchain = [[1]]


def get_lasat_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount):
    blockchain.append([get_lasat_blockchain_value(), transaction_amount])


add_value(2)
add_value(4)
add_value(8)

print(blockchain)
