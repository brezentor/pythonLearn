# before using of paramiko - install it - "cmd -> $ pip install paramiko"
import paramiko

host = "10.30.0.6"
port = 22
username = "iptel"
password = "48qtnRXt"


number = 438

command_koza = """mysql -u asterisk -pyw7s72ad1d2esd3qd3 asterisk -e 'select name from users where extension="{p}"'"""
command = command_koza.format(p = number)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
dataraw = stdout.read() + stderr.read()
location = str(dataraw).lstrip("b'name\\n").rstrip("n'").rstrip("\\")
print(location)
ssh.close()
