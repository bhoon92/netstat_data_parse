import commands
import ConfigParser
import logging

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput
#TODO logging => 
#TODO Exception data => std DATA logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


## Make Oring file & Works file
(status_code, origin_netstat) = command("netstat -lntup > origin_netstat")
(status_code, temp_netstat) = command("cp origin_netstat temp_netstat")
(status_code, make_result_file) = command("cp origin_netstat result_file")

## Extract to  netstat_ip
with open('./temp_netstat','r+') as f:
    read_file=f.read()
    read_file=read_file.split('\n') ## netstat -> list
    del read_file[0]

    # print("#### read_file ####")

    # for item in read_file:
        # print type(item)
        # print(item)
    print ("\n======================== Exception List ======================== ")
    config.read('./exception.conf')
    except_ip = config.get('EXCEPT', 'except_ip')
    except_ip = except_ip.split(',')
    print ("Except List IP is :",except_ip)

    except_port = config.get('EXCEPT', 'except_port')
    except_port = except_port.split(',')
    print ("Except List PORT is :",except_port)

    except_proc = config.get('EXCEPT', 'except_process')
    except_proc = except_proc.split(',')
    print ("Except List PROCESS are :",except_proc)
    print ("=================================================================\n")

    temp_list=""
    for item in read_file:
        temp_list += (item +"\n")
    
    temp_list=temp_list.split("\n")

    for read_file_proc_str in read_file:
        for ex_porc_item in except_proc:
            read_porc_str = ("/"+ex_porc_item+" ")
            if read_porc_str in read_file_proc_str:
                print read_porc_str
                temp_list.remove(read_file_proc_str)

    for temp_list_ip_str in temp_list:
        for ex_ip_item in except_ip:
            read_ip_str = (" "+ex_ip_item+":")
            if read_ip_str in temp_list_ip_str:
                print read_ip_str
                temp_list.remove(temp_list_ip_str)

    for temp_list_port_str in temp_list:
        for ex_port_item in except_port:
            read_port_str = (":"+ex_port_item+"  ")
            if read_port_str in temp_list_port_str:
                print read_port_str
                temp_list.remove(temp_list_port_str)

    print ("########## result ##########")
    result_file=""
    for item in temp_list:
        result_file += (item +"\n")
    print result_file

with open('./result_file','w+') as f:
#f.write(item)
    f.write(result_file)