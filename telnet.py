import getpass
import telnetlib

HOST = "192.168.6.253"

ls = b"Level13 toggle mute 1\n"
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Welcome to the Tesira Text Protocol Server...")
tn.write(ls)


print("哈哈哈")
