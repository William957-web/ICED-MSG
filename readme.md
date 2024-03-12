# ICED PWN2OWN練習網站  
這邊也會記錄每個漏洞的提交者  
## Version  
目前是 v 1.2    
連結：http://23.146.248.20:30003/  
## Rule
本網站是國立竹科實中資研社 Pwn2Own 項目練習網站  
在發現漏洞時請繳交writeup以及證明給社長/教學，經認證後會在Hacker頁面紀錄並附上你的writeup  
同一區域的同一漏洞只能被一人繳交，之後不可去攻擊該區（主辦原則上會盡快上patch去防護）  
會在Github 開源公布最新版本  
最後...開心聊天吧owob  
## 如何證明自己找到漏洞  
首先，私訊我和繳交WRITE UP是必須的  
攻擊分為幾種CASE：  
1.任意讀檔(2pt)：請讀取`/etc/passwd`以及我放在`/home/iced-msg/flag.txt`的檔案(跟網站後端程式碼運作的地方一樣)   
2.水平越權(1pt)：我會創造某個帳號請你登入它並變更它的備忘錄內容  
3.垂直越權(2pt)：登入管理員帳號並變更Announcement內容  
4.未提權RCE(4pt)：讓我的網站主動去`curl`你的webhook，並且彈reverse shell回到的主機上(可以使用iced-student的ssh)並且讀取到我放在`/home/iced-msg/`的某個flag檔案  
5.提權RCE(5pt)：你超電，反正就是提權成`root-iced-msg`的身分 cat flag.txt就好。  
如果是需要前端操作的(簡單來說就是要我點某個連結之類的)攻擊，請你私訊我後傳PoC給我，我會以登入管理員的身分點那個連結。    
## Hackers
