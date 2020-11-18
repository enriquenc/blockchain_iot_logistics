from enum import Enum

class ReturnCode(Enum):
	OK = 0
	UNAUTHORIZED_PRIVATE_KEY = 1
	EMPTY_CHAIN = 2
	WRONG_CHAIN_HEIGHT_NUMBER = 3
	INVALID_ARGUMENT = 4
	INVALID_TRANSACTION = 5
	INVALID_SIGNATURE = 6
	CARGO_ID_NOT_FOUND = 7
	BLOCK_ALREADY_ADDED = 8
	WRONG_PREVIOUS_BLOCK_HASH = 9
	INVALID_BLOCK_TRANSACTIONS = 10
	INVALID_BLOCK = 11
	INVALID_BLOCK_HASH = 12
	INVALID_MERKLE_ROOT = 13
	CARGO_INFORMATION_ALREADY_EXISTS = 14