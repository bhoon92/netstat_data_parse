import commands
import ConfigParser
import sys

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput

############# netstat IP 
(status_code, ip_v6) = command("netstat -nltup | awk '{print $1}'")
if "6" in ip_v6:
    (status_code, ip_v6) = command("netstat -nltup | awk '{print $4}' | cut -f 4 -d ':'")
    local_ip_v6=ip_v6.split()
    del local_ip_v6[0:2]
(status_code, netstat_ip)=command("netstat -nltup | awk ' {print $4}' | cut -f 1 -d ':'")
netstat_ip=netstat_ip.split()
del netstat_ip[0:2]

(s, a) = command("netstat -nltup |awk '{print $4}' |  grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'")

############# except IP
config.read('./exception.conf')
except_ip=config.get('EXCEPT', 'except_ip')
except_ip=except_ip.split(',')

result_ip=[]
for i in range(len(netstat_ip)):
    netstat_ip[i]
    for j in range(len(except_ip)):
        except_ip[j]
        if netstat_ip[i] == except_ip[j]:
            result_ip.append(netstat_ip[i])

result_ip=list(set(result_ip))

with open ('save_result', 'w+') as save_result:
    save_result.write('Local Address        Foreign Address        Program name\n')
    save_result.write('\n'.join(result_ip))
            
############# netstat port 
(status_code, ip_v6) = command("netstat -nltup | awk '{print $1}'")
if "6" in ip_v6:
    (status_code, port_v6) = command("netstat -nltup | awk '{print $4}' | cut -f 4 -d ':'")
    port_v6=port_v6.split()
    del port_v6[0:2]

(status_code, port_v4)=command("netstat -nltup | awk ' {print $4}' | cut -f 2 -d ':'")
port_v4=port_v4.split()
del port_v4[0:2]
local_netstat_port=list(set(port_v4 + port_v6))

############# except port
config.read('./exception.conf')
except_port=config.get('EXCEPT', 'except_port')
except_port=except_port.split(',')

############# local_netstat_port - except_port
local_netstat_port=[x for x in local_netstat_port if x not in except_port]

############# Foreign IP Address
(status_code, foreign_ip_v6) = command("netstat -nltup | awk '{print $1}'")
if "6" in ip_v6:
    (status_code, port_v6) = command("netstat -nltup | awk '{print $5}' | cut -f 4 -d ':'")
    ip_v6=port_v6.split()
    del port_v6[0:2]





#dif_process=[a for a, b in zip(netstat_process_list(), except_process_list()) if a==b]
""" ## Make list  local_ip 
(s, local_ip) = command("netstat -nltup | awk '{print $4}' |cut -f 1 -d ':'")
list_local_ip = local_ip.split()
del list_local_ip[0:2]
print type(list_local_ip)
print list_local_ip

## Get ip list of except
config.read('./exception.conf')
except_ip=config.get('EXCEPT', 'except_ip')
list_except_ip=except_ip.split(',')
print type(list_except_ip)
print list_except_ip

list_dif_ip=[]
for i in range(len(list_local_ip)):
    temp_local_ip = list_local_ip[i]
        
        for j in range(len(list_except_ip)):
            temp_except_ip=list_except_ip[j]
            
            if temp_local_ip==temp_except_ip:
                list_dif_ip = list_dif_ip+list_dif_ip
 """

#awk '{print $4}' temp.log |cut -f 1 -d ":" |grep -xn "127.0.0.1" |cut -f 1 -d ":"
#1. 위 코드 실행시 정확하게 일치하는 행을 구할 수 있음

# netstat -nltup |awk '{print $4}'|cut -f 1 -d ':' |grep -x "192.168.10.10"

# grep -n 문자열 파일
# grep -n 2610/dnsmasq log.log |awk '{print $1}' |cut -f 1 -d ":"

# sed -i '2d' log.log
#awk '{print $4}' temp.log

