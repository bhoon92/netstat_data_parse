import commands
import ConfigParser
import logging as log

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput
logger = log.getLogger()

logger.setLevel(log.INFO)
formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = log.FileHandler('netstat.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

## Make Oring file & Works file
(status_code, origin_netstat) = command("netstat -lntup > origin_netstat")
(status_code, temp_netstat) = command("cp origin_netstat temp_netstat")
(status_code, make_result_file) = command("cp origin_netstat result_file")

## Extract to netstat_ip
with open('./temp_netstat','r+') as f:
    read_file=f.read()
    read_file=read_file.split('\n') 
    
    config.read('./exception.conf')
    except_ip = config.get('EXCEPT', 'except_ip')
    except_ip = except_ip.split(',')
    
    except_port = config.get('EXCEPT', 'except_port')
    except_port = except_port.split(',')
    
    except_proc = config.get('EXCEPT', 'except_process')
    except_proc = except_proc.split(',')

    print ("\n======================== Exception List ======================== ")
    print ("Except List IP      :",except_ip)
    print ("Except List PORT    :",except_port)
    print ("Except List PROCESS :",except_proc)
    print ("=================================================================\n")

    ip_temp_list=""
    for ip_item in read_file:
        ip_temp_list += (ip_item +"\n")
    
    ip_temp_list = ip_temp_list.split("\n")

    for temp_list_ip_str in read_file:
        for ex_ip_item in except_ip:
            if len(ex_ip_item) > 0:
                read_ip_str = (" "+ex_ip_item+":")
                if read_ip_str in temp_list_ip_str:
                    ip_temp_list.remove(temp_list_ip_str)
                    print ("Lines containing [IP : "+ex_ip_item+"] have been excluded." )
            else :
                break

    port_temp_list=""
    for port_item in ip_temp_list:
        port_temp_list += (port_item +"\n")
    port_temp_list = port_temp_list.split("\n")
    
    for temp_list_port_str in ip_temp_list:
        for ex_port_item in except_port:
            read_port_str = (":"+ex_port_item+" ")
            if read_port_str in temp_list_port_str:
                port_temp_list.remove(temp_list_port_str)
                print ("Lines containing [PROT : "+ex_port_item+"] have been excluded." )
    
    proc_temp_list=""
    for proc_item in port_temp_list:
        proc_temp_list += (proc_item +"\n")
    proc_temp_list = proc_temp_list.split("\n")

    for read_file_proc_str in port_temp_list:
        for ex_proc_item in except_proc:
            read_porc_str = ("/"+ex_proc_item+" ")
            if read_porc_str in read_file_proc_str:
                proc_temp_list.remove(read_file_proc_str)
                print ("Lines containing [PROCESS NAME : "+ex_proc_item+"] have been excluded." )

    print ("########## result ##########")
    result_file=""
    for result_item in proc_temp_list:
        result_file += (result_item +"\n")
    print result_file

with open('./result_file','w+') as f:
    f.write(result_file)