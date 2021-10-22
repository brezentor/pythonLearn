# before using of paramiko - install it - "cmd -> $ pip install paramiko"
import paramiko

host = "172.29.213.242"
port = 22
username = "administrator"
password = "n7calfpaom"
u = open('C:\\Users\\Administrator.GATE1\\Desktop\\sipadd\\temp.txt')
mac = u.readline()
u.close()
maccommand = mac + ".txt"

command1 = "cd ~"
command2 = "touch " + maccommand
command3 = "sudo -s"
command4 = "n7calfpaom"
command5 = "chmod 777 " + maccommand
command6 = 'printf "<flat-profile>\n <HostName ua=\"rw\">SPA8000-68</HostName>\n' \
           ' <User_ID_1_ ua=\"na\"></User_ID_1_>\n <Password_1_ ua=\"na\"></Password_1_>\n' \
           ' <Use_Auth_ID_1_ ua=\"na\">No</Use_Auth_ID_1_>\n <User_ID_2_ ua=\"na\"></User_ID_2_>\n' \
           ' <Password_2_ ua=\"na\"></Password_2_>\n <Use_Auth_ID_2_ ua=\"na\">No</Use_Auth_ID_2_>\n' \
           ' <User_ID_3_ ua=\"na\"></User_ID_3_>\n <Password_3_ ua=\"na\"></Password_3_>\n' \
           ' <Use_Auth_ID_3_ ua=\"na\">No</Use_Auth_ID_3_>\n <User_ID_4_ ua=\"na\"></User_ID_4_>\n' \
           ' <Password_4_ ua=\"na\"></Password_4_>\n <Use_Auth_ID_4_ ua=\"na\">No</Use_Auth_ID_4_>\n' \
           ' <User_ID_5_ ua=\"na\"></User_ID_5_>\n <Password_5_ ua=\"na\"></Password_5_>\n' \
           ' <Use_Auth_ID_5_ ua=\"na\">No</Use_Auth_ID_5_>\n <User_ID_6_ ua=\"na\"></User_ID_6_>\n' \
           ' <Password_6_ ua=\"na\"></Password_6_>\n <Use_Auth_ID_6_ ua=\"na\">No</Use_Auth_ID_6_>\n' \
           ' <User_ID_7_ ua=\"na\"></User_ID_7_>\n <Password_7_ ua=\"na\"></Password_7_>\n' \
           ' <Use_Auth_ID_7_ ua=\"na\">No</Use_Auth_ID_7_>\n <User_ID_8_ ua=\"na\"></User_ID_8_>\n' \
           ' <Password_8_ ua=\"na\"></Password_8_>\n <Auth_ID_8_ ua=\"na\">No</Auth_ID_8_>\n' \
           ' <Use_Auth_ID_8_ ua=\"na\">No</Use_Auth_ID_8_>\n</flat-profile>\n" > ' + maccommand
# command7 = "sed -r 's/@/\"/g'" + maccommand

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

ssh.exec_command(command1)
ssh.exec_command(command2)
ssh.exec_command(command3)
ssh.exec_command(command4)
ssh.exec_command(command5)
ssh.exec_command(command6)

# stdin, stdout, stderr = ssh.exec_command(command6)
# data = stdout.read() + stderr.read(

ssh.close()


