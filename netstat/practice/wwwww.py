import commands
import ConfigParser
import sys

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput

#===netstat port configuration
(status, netstat_port) = command("netstat -nltup | awk '{print $5}' |cut -f 2 -d ':'")
list_netstat_port = netstat_port.split()
del list_netstat_port[0:2]
print ("list_netstat_port : ", list_netstat_port)

'''
#===netstat process configuration
(status, protocol) = command("netstat -nltup | awk '{print $1}'")

if "tcp" in protocol:
    (status, tcp)=command("netstat -nltp | awk '{print $7}' |cut -f 2 -d '/'")
    list_tcp=tcp.split()
    del list_tcp [0:2]
    print ("list process of tcp : ",list_tcp)

if "udp" in protocol:
    (status, udp)=command("netstat -nlup | awk '{print $6}' |cut -f 2 -d '/'")
    list_udp = udp.split()
    del list_udp [0:2]
    print ("list process of udp : ",list_udp)
'''
list_tcp.extend(list_udp)
print ("Sum of two process list : ",list_tcp)

#=== exception port in conf
config.read('./exception.conf')
except_port = config.get('EXCEPT', 'except_port')
list_except_port=except_port.split(',')
print ("Except port list : ",list_except_port)

#===exception process in conf
config.read('./exception.conf')
except_process = config.get('EXCEPT', 'except_process')
list_except_process=except_process.split(',')
print ("Except process list : ",list_except_process)

#=== compare netstat process to exception process
#dif_process = [a for a, b in zip(list_tcp, list_except_process) if a==b]

#=== compare netstat port to exception port
#dif_port=[i for i, j in zip(list_netstat_port, list_except_port) if i==j]

print ("Dif_prot : ",dif_port)
print ("Dif_process : ",dif_process)
#dif_port.extend(dif_process)

#=== 
(status, save_netstat_origin)=command("netstat -nltup > netstat.log")

if len(list_except_port)>0:
    for i in range(len(list_except_port)):
        (s, except_port) = command("sed -i '/"+list_except_port[i]+"/d' netstat.log")


if len(list_except_process)>0:
    for i in range(len(list_except_process)):
        #(status, except_process)=command("sed -i '/"+dif_process[i]+"/d' netstat.log")
        (status, except_process)=command("sed -i '/"+list_except_process[i]+"/d' netstat.log")
