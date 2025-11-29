hereimport requests, time, random

def solve_hcaptcha(sitekey, url):
    api_key = "YOUR_2CAPTCHA_KEY_HERE"
    resp = requests.post(f"http://2captcha.com/in.php?key={api_key}&method=hcaptcha&sitekey={sitekey}&pageurl={url}")
    cid = resp.text.split("|")[1]
    for _ in range(30):
        time.sleep(6)
        r = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={cid}")
        if "CAPCHA_NOT_READY" not in r.text:
            return r.text.split("|")[1]
    return None
