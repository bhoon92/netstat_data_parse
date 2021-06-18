import commands
import ConfigParser
import sys

#같은값 찾기
A = [1, 2, 3, 4, 5]
B = [9, 8, 7, 6, 5]

C = set(a) & set(b)
D = [i for i, j in zip(A, B) if i == j]

# C ==> {5}  (object)
# D ==> [5]  (list)

#다른값 찾기
A = [1, 2, 3, 4, 5]
B = [1, 3, 5, 7, 9]

C = list(set(A) - set(B))
D = list(set(B) - set(A))

# C ==> [2, 4]
# D ==> [7, 9]


#sys.argv[1] -> 띄어쓰기를 구분으로 입력 된 문자열의 두 번째인자를 나타냄
# config = ConfigParser.ConfigParser()
# config.read(특정파일) -> 파일이름을 읽음
# test_ip = config.get()

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput
(status, netstat_ip) = command("netstat -nltup > netstat.log")
#(status, save_netstat) = command("touch ")

config.read('exception.conf')
#print(config.sections())

except_ip = config.get('EXCEPT', 'except_ip')
list_except_ip=except_ip.split(',')
print list_except_ip

print type(list_except_ip)

(status, netstat_ip) = command("netstat -nltup | awk '{print $5}' |cut -f 1 -d ':'")
(status, netstat_port) = command("netstat -nltup | awk '{print $5}' |cut -f 2 -d ':'")
(status, netstat_port) = command("netstat -nltup | awk '{print $7}' |cut -f 2 -d ':'")

list_netstat_ip=netstat_ip.split()
del list_netstat_ip[0:2]
print list_netstat_ip

list_netstat_port=netstat_port.split()
del list_netstat_port[0:2]
print list_netstat_port

dif_ip = [i for i, j in zip(list_netstat_ip, list_except_ip) if i == j]

print dif_ip


if len(dif_ip)>0:
    for i in range(len(dif_ip)):
        (status, remove_ip) = command("netstat -nltup |sed '/"+dif_ip[i]+"/d' netstat.log")
else:
    pass
                                            