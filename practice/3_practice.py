import pickle
import commands
import ConfigParser
import sys
import pprint

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput

## Make Oring file & Works file
(status_code, origin_netstat) = command("netstat -lntup > origin_netstat")
(status_code, temp_netstat) = command("cp origin_netstat temp_netstat")

## Extract to  netstat_ip
with open('./temp_netstat','r+') as f:
    read_file=f.read()
    list_temp_file=read_file.split('\n') ## netstat -> list
    
    ## Extract except ip & port
    config.read('./exception.conf')
    except_ip=config.get('EXCEPT', 'except_ip')
    except_ip=except_ip.split(',')
    print ("Except List IP is :",except_ip)

    config.read('./exception.conf')
    except_port=config.get('EXCEPT', 'except_port')
    except_port=except_port.split(',')
    print ("Except List PORT is :",except_port)

    split_list=[] ## Total list
    for i in range(len(list_temp_file)):
        split_list += list_temp_file[i].split()

    matching =[s for s in split_list if ":" in s]

    netstat_ip=[]
    for i in range(len(matching)):
        s = matching[i].split(':')
        netstat_ip.append(s)

    result_ip=[]
    # result_port=[]
    for i in range(len(netstat_ip)):
        netstat_ip[i][0]
        for j in range(len(except_ip)):
            except_ip[j]
            if netstat_ip[i][0] == except_ip[j]:
                result_ip.append(netstat_ip[i])
        for j in range(len(except_port)):
            if netstat_ip[i][1] == except_port[j]:
                result_ip.append(netstat_ip[i])
                
    print ("Except Ip is [IP],[Port] : ",result_ip)    

    config.read('./exception.conf')
    except_process=config.get('EXCEPT', 'except_process')
    except_process=except_process.split(',')
    print ("Except List PORT is :",except_process)

    proc_matching =[s for s in split_list if "/" in s]
    
    netstat_proc=[]
    for i in range(len(proc_matching)):
        proc = proc_matching[i].split('/')
        netstat_proc.append(proc)
    
    # print ("matching_PROCESS : ",proc_matching)
    # print ("#######################")
    # print ("NETSTAT_PROCESS : ",netstat_proc)
    
    result_proc=[]
    for i in range(len(netstat_proc)):
        netstat_proc[i][1]
        for j in range(len(except_process)):
            except_process[j]
            if netstat_proc[i][1] == except_process[j]:
                result_proc.append(netstat_proc[i])
    print result_proc

    asd="/".join(result_proc[1])
    print asd

    if asd in list_temp_file[4]:
        print "ASDASDASDASDASD"
    
