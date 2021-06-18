import commands
import ConfigParser

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput

## Make Oring file & Works file
(status_code, origin_netstat) = command("netstat -lntup > origin_netstat")
(status_code, temp_netstat) = command("cp origin_netstat temp_netstat")

## Extract to  netstat_ip
with open('./temp_netstat','r+') as f:
    read_file=f.read()
    list_temp_file=read_file.split('\n') ## netstat -> list
    print "######################################################"
    print list_temp_file

    split_list=[] ## Temp File Total list
    for i in range(len(list_temp_file)):
        split_list += list_temp_file[i].split()
    print split_list

    ip_port_matching =[s for s in split_list if ":" in s]
    proc_matching = [s for s in split_list if "/" in s]
    # print "######################################################"
    # print ip_port_matching
    # print proc_matching
    # print "######################################################"

    ## split ip & port to colon
    netstat_ip_port=[]
    for i in range(len(ip_port_matching)):
        s = ip_port_matching[i].split(':')
        netstat_ip_port.append(s)
    
    ## combinate ip to port 
    for i in range(len(netstat_ip_port)):
        com_ip_port=":".join(netstat_ip_port[i])

    netstat_proc=[]
    for i in range(len(proc_matching)):
        proc = proc_matching[i].split('/')
        netstat_proc.append(proc)
    # print "######################################################"
    # print netstat_proc
    # print netstat_ip_port
    # print "######################################################"
    ## Extract except ip & port
    config.read('./exception.conf')
    except_ip = config.get('EXCEPT', 'except_ip')
    except_ip = except_ip.split(',')
    print ("Except List IP is :",except_ip)

    except_port = config.get('EXCEPT', 'except_port')
    except_port = except_port.split(',')
    print ("Except List PORT is :",except_port)

    except_proc = config.get('EXCEPT', 'except_process')
    except_proc = except_proc.split(',')
    print ("Except List PORT is :",except_process)

    result_list=[]
    for i in range(len(list_temp_file)):
        read_temp_file=list_temp_file[i]
        
        for j in range(len(except_proc)):
            read_except_proc = except_proc[j]
            
            if read_except_proc not in read_temp_file:

                 
        for j in range(len(except_ip)):
            read_except_ip = (except_ip[j]+":")
            
            if read_except_ip not in read_temp_file: 
                
            elif 



                