from netmiko import ConnectHandler

ocnos_device = {
    'device_type':'cisco_ios',
    'ip':'10.12.94.161',
    'username':'ocnos',
    'password':'ocnos',
    'port':22
}

connection = ConnectHandler(**ocnos_device)

print(connection.send_command('show ip int br'))
print(connection.send_command('show run'))
connection.enable()


connection.disconnect()