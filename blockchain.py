# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blochain value to the blockchain. """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the in put of the user as a float. """
    return float(input('Your transaction amount: '))


# Get the first transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)

print('Done')
