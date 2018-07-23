from pwn import *

p = remote('121.170.91.11', 9999)

for stage in range(1, 21):
    print p.recvuntil('================== '+str(stage).zfill(2)+' STAGE ==================')
    text = p.recvuntil('ANSWER>')

    print text
    equation = text.split('\n')[1][10:].replace(' = ?', '')

    print equation
    p.sendline(str(eval(equation)))


print p.recvall()
