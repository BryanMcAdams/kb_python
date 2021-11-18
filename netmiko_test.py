from netmiko import ConnectHandler

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": '88newclass',
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": '88newclass',
    "device_type": "cisco_nxos",
}

ios_xe1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": '88newclass',
    "device_type": "cisco_nxos",
}

device_list = [nxos1, nxos2, ios_xe1]

#for device in device_list:
#	net_connect = ConnectHandler(**device)
#	print(net_connect.find_prompt())
#	net_connect.disconnect()

net_connect = ConnectHandler(**ios_xe)
output = net_connect.send_command("show ip interface brief")
print(output)
