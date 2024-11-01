# Discord Account Checker

A multi-threaded Discord account checker that verifies tokens, checks Nitro status, boost availability, and account verification status.

## ⚠️ Legal Disclaimer

**IMPORTANT: READ BEFORE USING**

- This tool is for EDUCATIONAL PURPOSES ONLY
- The developer(s) and contributor(s) are NOT responsible for:
  - Any misuse of this tool
  - Any violation of Discord's Terms of Service
  - Any damages or legal consequences that may arise from using this tool
  - Any illegal activities performed with this tool
- By using this tool, you agree that you take FULL RESPONSIBILITY for your actions
- Commercial use, selling, or distributing this tool is STRICTLY PROHIBITED
- The user bears ALL responsibility for compliance with applicable laws and regulations

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

## Terms of Use
- NO commercial use
- NO selling or redistributing this tool
- NO malicious use
- NO token stealing or account hijacking
- NO automated abuse of Discord's services
- NO violation of Discord's Terms of Service
- NO using this tool to harm others

## Notice
This is a proof-of-concept tool intended for educational purposes to understand API interactions and account verification processes. Any use of this tool for malicious purposes, including but not limited to account theft, token stealing, or service disruption is strictly prohibited and may be illegal. Users must comply with Discord's Terms of Service and all applicable laws.

## Contributing
If you want to contribute to this project, please ensure your modifications adhere to the educational purpose of this tool and do not promote or facilitate malicious use.
