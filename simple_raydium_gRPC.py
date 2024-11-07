from solders.pubkey import Pubkey

RAY_AUTHORITY_V4 = Pubkey.from_string("5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1")
Pool_raydium = Pubkey.from_string("675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8")

def get_pool_keys_tx(response):
    pool_keys = "NA"

    account_keys = [Pubkey.from_bytes(bytes(key)) for key in response.transaction.transaction.transaction.message.account_keys]

    instructions = response.transaction.transaction.transaction.message.instructions

    for i, instruction_proto in enumerate(instructions):
        program_id_index = instruction_proto.program_id_index
        program_id = account_keys[program_id_index]
        accounts = instruction_proto.accounts
        data = instruction_proto.data

        account_keys_involved = []
        
        for idx in accounts:
            if idx >= len(account_keys):
                continue
            account_keys_involved.append(account_keys[idx])

        if str(program_id) == Pool_raydium:
            if len(account_keys_involved) == 17:
                pool_keys = {
                    "amm_id": account_keys_involved[1],
                    "authority": RAY_AUTHORITY_V4,
                    "open_orders": account_keys_involved[3],
                    "target_orders": "NA",
                    "base_vault": account_keys_involved[4],
                    "quote_vault": account_keys_involved[5],
                    "market_id": account_keys_involved[7],
                    "bids": account_keys_involved[8],
                    "asks": account_keys_involved[9],
                    "event_queue": account_keys_involved[10],
                    "market_base_vault": account_keys_involved[11],
                    "market_quote_vault": account_keys_involved[12],
                    "market_authority": account_keys_involved[13]
                }
                return pool_keys
            elif len(account_keys_involved) == 18:
                pool_keys = {
                    "amm_id": account_keys_involved[1],
                    "authority": RAY_AUTHORITY_V4,
                    "open_orders": account_keys_involved[3],
                    "target_orders": account_keys_involved[4],
                    "base_vault": account_keys_involved[5],
                    "quote_vault": account_keys_involved[6],
                    "market_id": account_keys_involved[8],
                    "bids": account_keys_involved[9],
                    "asks": account_keys_involved[10],
                    "event_queue": account_keys_involved[11],
                    "market_base_vault": account_keys_involved[12],
                    "market_quote_vault": account_keys_involved[13],
                    "market_authority": account_keys_involved[14]
                }
                return pool_keys
    return "NA"