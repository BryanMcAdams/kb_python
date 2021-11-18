from netmiko import ConnectHandler

device1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": '88newclass',
    "device_type": "cisco_nxos",
}

device2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": '88newclass',
    "device_type": "cisco_nxos",
}

device_list = ['device1', 'device2']

for device in device_list:
	net_connect = ConnectHandler(**device)
	print(net_connect.find_prompt())
	net_connect.disconnect()
