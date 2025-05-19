import json
from web3 import Web3, HTTPProvider



# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\Antique Integrity System\\node_modules\\.bin\\build\\contracts\\Antique.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xf3D138c8b53Feb20a2af3B58Dcc88648171bD69E'
syspath=r"C:\Users\DELL\OneDrive\Desktop\Antique Integrity System\static\\"




