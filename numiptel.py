
# before using of paramiko - install it - "cmd -> $ pip install paramiko"
# before using of webdriver from selenium - install it - "cmd -> $ pip install selenium"
import paramiko

host = "10.30.0.6"
port = 22
username = "iptel"
password = "48qtnRXt"
u = open('C:\\scripts\\iptel\\temp.txt')
mac = u.readline()
u.close()
maccommand = mac + ".xml" # мас-адрес телефона
n = '165' # номер телефона
i = '10.30.0.197' # ip теелефона

command_koza = 'printf "<flat-profile>\n <HostName ua=\\"rw\\"></HostName>\n' \
               ' <User_ID_1_ ua=\\"na\\">{n}</User_ID_1_>\n <Password_1_ ua=\\"na\\">{n}</Password_1_>\n' \
               ' <Use_Auth_ID_1_ ua=\\"na\\">No</Use_Auth_ID_1_>\n' \
               ' <Auth_ID_1_ ua=\\"na\\"></Auth_ID_1_>\n</flat-profile>\n" > /tftproot/Cisco/spa502g/{m}'
command = command_koza.format(m = maccommand)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
data = stdout.read() + stderr.read()

ssh.close()

# before using of webdriver from selenium - install it - "cmd -> $ pip install selenium"
from selenium import webdriver

webpage = r"http://{ip}/admin/basic"
webpage = webpage.format(ip = i)
searchterm = '{num}'
searchterm = searchterm.format(num = n)

driver = webdriver.Chrome()
driver.get(webpage)

numberip = driver.find_element_by_xpath("/html/body[onload='onLoad()']/form[@action='bcisco.csc']/table/tbody/tr/td[@valign='top']/div[@id='tableData']/div[@id='Ext 1']/table/tbody/tr[23]/td[4]/input")
numberip.send_keys(searchterm)
passip = driver.find_element_by_name("P64815")
passip.send_keys(searchterm)

submit = driver.find_element_by_class_name("sbtSearch")
submit.click()