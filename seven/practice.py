# 1.从url中截取端口号
server_name = '127.0.0.1:'
if server_name and ':' in server_name:
    port = int(server_name.rsplit(':',1)[1])
else:
    port = 5000
print(port)