servers = {'HP':120930, 'Dell':9012341, 'IBM':673408} # returning the value of a key and deleting the pair

code1 = servers.pop('HP')
print(code1)

code2 = servers.pop("Lenovo", "Unknown") # returning value "unknown" if the key is not in the servers dict
print(code2)
print(servers)