import os
import time
import random
import inspect
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
from web3 import Web3, Account
from dotenv import load_dotenv
import getpass

# Network constants
RPC_URL = "https://dream-rpc.somnia.network/"  # RPC URL for Somnia Testnet
CHAIN_ID = 50312  # Chain ID for the network
GAS_LIMIT = 21000  # Gas limit for transfer transactions

def print_header():
    """
    Print the colored header
    """
    header = """
\033[1;36m===============================================
       Somnia Testnet Wallet Sender Bot       
       coded By P4R4D0X , powered by HexQuant       
===============================================\033[0m
    """
    print(header)

def save_private_key_to_env(private_key):
    """
    Saves the private key to the .env file.
    """
    env_file = ".env"
    with open(env_file, "w") as f:
        f.write(f"PRIVATE_KEY={private_key}\n")

def load_private_key_from_env():
    """
    Loads the private key from the .env file.
    """
    load_dotenv()
    return os.getenv("PRIVATE_KEY")

def generate_wallets(num):
    """
    Generates the specified number of wallets (only addresses) using web3.Account.create().
    """
    wallets = []
    for _ in range(num):
        acct = Account.create()
        wallets.append(acct.address)
    return wallets

def save_wallets(wallets, filename):
    """
    Saves generated wallet addresses to a file with the specified name.
    """
    with open(filename, "w") as f:
        for addr in wallets:
            f.write(addr + "\n")

def main():
    print_header()
    try:
        # Get the number of private keys to use
        num_keys = int(input("Enter the number of private keys to use: "))
        private_keys = []
        for i in range(num_keys):
            pk = getpass.getpass(f"Enter private key #{i+1}: ").strip()
            private_keys.append(pk)
        
        # Get the number of wallets to generate for each private key
        wallets_per_key = int(input("Enter the number of wallets to generate for each private key: "))
        
        # Get the token amount range for sending (in STT, assumed like Ether)
        min_amount = float(input("Enter minimum token amount to send (in STT): "))
        max_amount = float(input("Enter maximum token amount to send (in STT): "))
        
        # Get the random delay range between transactions (in seconds)
        min_delay = float(input("Enter minimum delay between transactions (in seconds): "))
        max_delay = float(input("Enter maximum delay between transactions (in seconds): "))
        
        # Connect to the test network
        web3 = Web3(Web3.HTTPProvider(RPC_URL))
        if not web3.isConnected():
            print("Error: Unable to connect to the network.")
            return
        
        # Process each private key
        for idx, private_key in enumerate(private_keys, start=1):
            print(f"\nProcessing Private Key #{idx}:")
            sender_account = Account.from_key(private_key)
            print(f"Sender Address: {sender_account.address}")
            
            # Save the private key to .env file (for usage in this section)
            save_private_key_to_env(private_key)
            
            # Generate wallets for the current private key
            wallets = generate_wallets(wallets_per_key)
            wallet_filename = f"wallet_{idx}.txt"
            save_wallets(wallets, wallet_filename)
            print(f"Generated {wallets_per_key} wallets and saved to file '{wallet_filename}'")
            
            # Retrieve the initial nonce from the network
            nonce = web3.eth.getTransactionCount(sender_account.address)
            
            # Send a transaction to each generated wallet
            for wallet in wallets:
                amount = random.uniform(min_amount, max_amount)
                value = web3.toWei(amount, 'ether')
                gas_price = web3.eth.gasPrice
                
                tx = {
                    'nonce': nonce,
                    'to': wallet,
                    'value': value,
                    'gas': GAS_LIMIT,
                    'gasPrice': gas_price,
                    'chainId': CHAIN_ID
                }
                
                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                print(f"Sent {amount:.6f} STT to {wallet}. Transaction hash: {tx_hash.hex()}")
                
                nonce += 1
                delay = random.uniform(min_delay, max_delay)
                time.sleep(delay)
        
        print("\nAll transactions have been sent for all private keys.")
        input("Press Enter to exit...")
    
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
    finally:
        # Delete the .env file after program completion
        if os.path.exists(".env"):
            os.remove(".env")

if __name__ == "__main__":
    main()
