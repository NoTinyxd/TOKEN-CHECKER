# Discord Account Checker

A multi-threaded Discord account checker that verifies tokens, checks Nitro status, boost availability, and account verification status.

## Features
- Checks Discord accounts for:
  - Account validity
  - Nitro subscription status
  - Available boosts (0-2)
  - Account age
  - Email verification
  - Phone verification
- Multi-threaded execution (200 threads by default)
- Colored console output
- Automatic file sorting based on results

## Requirements
```
pip install tls-client
pip install colorama
```

## Setup
1. Create a file named `tokens.txt` in the script directory
2. Add your tokens in the format: `email:password:token`
3. Create an `output` folder in the script directory

## Output Files
The script generates several output files in the `output` folder:
- `0boosts.txt` - Valid accounts with no boosts
- `1boosts.txt` - Accounts with 1 available boost
- `2boosts.txt` - Accounts with 2 available boosts
- `nonitro.txt` - Accounts without Nitro
- `locked.txt` - Locked accounts
- `invalid.txt` - Invalid tokens

## Usage
```bash
python checker.py
```

## Output Format
The checker displays information in the following format:
```
[*] email:pass:token**** | Info : [Status : UNLOCKED/LOCKED/INVALID, Nitro : YES/NO, Subscription Date Expire in : X days, Boosts left : X, Account Age : X, Email Verified : YES/NO, Phone Verified : YES/NO]
```

### Note
'''Selling / Reselling this product is not allowed.Its an open source script so dont sell this please!!'''
