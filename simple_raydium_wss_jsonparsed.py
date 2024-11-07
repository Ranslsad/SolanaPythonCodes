from solders.pubkey import Pubkey

RAY_AUTHORITY_V4 = Pubkey.from_string("5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1")
Pool_raydium = Pubkey.from_string("675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8")

def get_pool_keys_tx(transaction):
    pool_keys = "NA"
    tmpInstructions = transaction.transaction.transaction.message.instructions

    for instruction_check in tmpInstructions:

        if str(instruction_check.program_id) == str(Pool_raydium):

            if len(instruction_check.accounts) == 17:

                pool_keys = {
                    "amm_id": instruction_check.accounts[1],
                    "authority": RAY_AUTHORITY_V4,
                    "open_orders": instruction_check.accounts[3],
                    "target_orders": "NA",
                    "base_vault": instruction_check.accounts[4],
                    "quote_vault": instruction_check.accounts[5],
                    "market_id": instruction_check.accounts[7],
                    "bids": instruction_check.accounts[8],
                    "asks": instruction_check.accounts[9],
                    "event_queue": instruction_check.accounts[10],
                    "market_base_vault": instruction_check.accounts[11],
                    "market_quote_vault": instruction_check.accounts[12],
                    "market_authority": instruction_check.accounts[13]
                }
                return pool_keys
            elif len(instruction_check.accounts) == 18:

                pool_keys = {
                    "amm_id": instruction_check.accounts[1],
                    "authority": RAY_AUTHORITY_V4,
                    "open_orders": instruction_check.accounts[3],
                    "target_orders": instruction_check.accounts[4],
                    "base_vault": instruction_check.accounts[5],
                    "quote_vault": instruction_check.accounts[6],
                    "market_id": instruction_check.accounts[8],
                    "bids": instruction_check.accounts[9],
                    "asks": instruction_check.accounts[10],
                    "event_queue": instruction_check.accounts[11],
                    "market_base_vault": instruction_check.accounts[12],
                    "market_quote_vault": instruction_check.accounts[13],
                    "market_authority": instruction_check.accounts[14]
                }
                return pool_keys
    return "NA"