# Somnia Testnet Wallet Sender Bot

A Python bot designed to interact with the Somnia Testnet network. This script leverages [web3.py](https://github.com/ethereum/web3.py) (v5.31.1) and [python-dotenv](https://github.com/theskumar/python-dotenv) to generate wallet addresses, send random token amounts (STT) to those wallets, and manage multiple private keys.

## Features

- **Multi-Key Support:** Input multiple private keys and generate a specified number of wallet addresses for each.
- **Wallet Generation:** Creates unique wallet addresses using web3's account creation.
- **Randomized Transactions:** Sends random token amounts (in a specified range) from your account to each generated wallet.
- **Nonce Management:** Automatically retrieves and manages nonces for sequential transactions.
- **Random Delays:** Implements random delays between transactions to mimic real-world timing.
- **Colorful Terminal Output:** Displays a visually appealing header and real-time transaction feedback.
- **Cleanup:** Automatically deletes temporary environment files after execution.

## Requirements

- Python 3.7 or later
- [web3.py==5.31.1](https://pypi.org/project/web3/5.31.1/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HexQuant-hub/Somnia-Testnet.git
   cd Somnia-Testnet
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
   *Alternatively, install them manually:*
   ```bash
   pip install web3==5.31.1 python-dotenv
   ```

## Usage

Run the bot using:
```bash
python3 main.py
```
Follow the on-screen prompts:
- Enter the number of private keys you wish to use.
- For each private key, input the key (the input will be hidden for security).
- Specify the number of wallets to generate per private key.
- Provide the minimum and maximum token amounts (in STT) to send.
- Define the minimum and maximum delay (in seconds) between transactions.

After all transactions are completed, a summary report is displayed. Press Enter to exit the program.

## Notes

- This bot is intended for use with the Somnia Testnet. Ensure you have sufficient test tokens in your account.
- The script temporarily stores your private key in a `.env` file, which is automatically deleted upon program completion.
- **Use at your own risk:** Always test thoroughly on the testnet before using with any live assets.

## License

This project is licensed under the MIT License.

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request for any improvements.

## Author

Coded by P4R4D0X, powered by HexQuant.

---

You can modify this template to better suit your project's specifics if needed.
