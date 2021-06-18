import commands
import ConfigParser
import logging as log

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput
logger = log.getLogger()

# logger.setLevel(log.INFO)
# formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler = log.FileHandler('netstat.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)



## Make Oring file & Works file
(status_code, origin_netstat) = command("netstat -lntup > origin_netstat")
(status_code, temp_netstat) = command("cp origin_netstat temp_netstat")
(status_code, make_result_file) = command("cp origin_netstat result_file")

## Extract to  netstat_ip
with open('./temp_netstat','r+') as f:
    read_file=f.read()
    read_file=read_file.split('\n') ## netstat -> list
    del read_file[0]
    print len(read_file)


    print ("\n======================== Exception List ======================== ")
    config.read('./exception.conf')
    except_ip = config.get('EXCEPT', 'except_ip')
    except_ip = except_ip.split(',')
    print ("Except List IP      :",except_ip)

    except_port = config.get('EXCEPT', 'except_port')
    except_port = except_port.split(',')
    print ("Except List PORT    :",except_port)

    except_proc = config.get('EXCEPT', 'except_process')
    except_proc = except_proc.split(',')
    print ("Except List PROCESS :",except_proc)
    print ("=================================================================\n")

    temp_ip_list=''
    for item in read_file:
        temp_ip_list += item+"\n"
    print temp_ip_list
    temp_ip_list=temp_ip_list.split("\n")
    
    #temp_ip_list=[]
    for std_ip_str in read_file:
        for ex_ip_str in except_ip:
            read_ex_ip_str = (" "+ex_ip_str+":")
            
            if read_ex_ip_str not in std_ip_str:
    
    
    print temp_ip_list
    




    '''
    port_temp_list=""
    for item in ip_temp_list:
        port_temp_list += (item +"\n")
    print port_temp_list
    port_temp_list = port_temp_list.split("\n")
    
    # print type(prot_temp_list)
    # print prot_temp_list
    
    for temp_list_port_str in ip_temp_list:
        for ex_port_item in except_port:
            read_port_str = (":"+ex_port_item+" ")
            if read_port_str in temp_list_port_str:
                port_temp_list.remove(temp_list_port_str)
                print ("Lines containing [PROT : "+ex_port_item+"] have been excluded." )
    
    proc_temp_list=""
    for item in ip_temp_list:
        proc_temp_list += (item +"\n")
        
    print proc_temp_list
    proc_temp_list = proc_temp_list.split("\n")

    # print type(proc_temp_list)
    # print proc_temp_list
    
    for read_file_proc_str in ip_temp_list:
        for ex_proc_item in except_proc:
            read_porc_str = ("/"+ex_proc_item+" ")
            if read_porc_str in read_file_proc_str:
                proc_temp_list.remove(read_file_proc_str)
                print ("Lines containing [PROCESS NAME : "+ex_proc_item+"] have been excluded." )

    print ("########## result ##########")
    result_file=""
    for item in proc_temp_list:
        result_file += (item +"\n")
    print result_file

with open('./result_file','w+') as f:
#f.write(item)
    f.write(result_file)
'''