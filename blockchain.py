# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blochain value to the blockchain. """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the in put of the user as a float. """
    return float(input('Your transaction amount: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)


# Get the first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transactino value')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()

print('Done')
