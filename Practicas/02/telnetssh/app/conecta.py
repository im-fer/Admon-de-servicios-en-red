import telnetlib

host = '192.168.0.1'
user = 'admin'
password = 'admin01'
cmd = ["ena","1234","sh ip route","sh ip int br","exit"]

tn=telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii')+b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
for i in cmd_list:
    tn.write(i.encode("ascii")+b"\n")
print(tn.read_all().decode("ascii"))
tn.close()
