
import pickle
import commands
import ConfigParser
import sys

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput

## Make Oring file & Works file
(status_code, origin_netstat) = command("netstat -lntup > origin_netstat")
(status_code, temp_netstat) = command("cp origin_netstat temp_netstat")

## Except IP
config.read('./exception.conf')
except_ip=config.get('EXCEPT', 'except_ip')
except_ip=except_ip.split(',')
print ("Except_ip is :",except_ip)

## Extract line to be deleted
list_except_local_ip=[]
temp_ip=""
for i in range(len(except_ip)):
    (status_code, except_local_ip) = command("awk '{print $4}' temp_netstat |cut -f 1 -d ':' |grep -xn "+except_ip[i]+" |cut -f 1 -d ':'")
    temp_ip += '\n'+except_local_ip
    print temp_ip
    #(status_code, delete_list)=command("sed -i "+list_except_local_ip[i]+"d temp_netstat")
    
    if except_ip[i] == except_ip[-1]:
        list_except_local_ip = temp_ip.split()

list_except_local_ip=list(set(list_except_local_ip))
list_except_local_ip=map(int,list_except_local_ip)
list_except_local_ip.sort()
list_except_local_ip=map(str,list_except_local_ip)
print type(list_except_local_ip)
print ("Delete List Line is :" ,list_except_local_ip)


## Delete Line 
# 
# sed -i '2d' log.log
'''
i=0
for i in range(len(list_except_local_ip)):
    print list_except_local_ip[i]
    print type(list_except_local_ip[i])
    
    (status_code, delete_list)=command("sed -i "+list_except_local_ip[i]+"d temp_netstat")
'''