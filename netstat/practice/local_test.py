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

# # stream_handler = logging.StreamHandler()
# # stream_handler.setFormatter(formatter)
# # logger.addHandler(stream_handler)



# ## Make Oring file & Works file
# (status_code, origin_netstat) = command("netstat -lntup > origin_netstat")
# (status_code, temp_netstat) = command("cp origin_netstat temp_netstat")
# (status_code, make_result_file) = command("cp origin_netstat result_file")

## Extract to  netstat_ip
#with open('./temp_netstat','r+') as f:
with open('C:/Users/user/Desktop/Norma/TEST/temp_netstat.txt',mode='r') as f:
    read_file=f.read()
    read_file=read_file.split('\n') ## netstat -> list
    del read_file[0]
    print len(read_file)

    # print("#### read_file ####")

    # for item in read_file:
        # print type(item)
        # print(item)
    print ("\n======================== Exception List ======================== ")
    config.read('C:\\Users\\user\\Desktop\\Norma\\TEST\\exception.conf.txt')
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

    temp_list=""
    for item in read_file:
        temp_list += (item +"\n")
    
    temp_list=temp_list.split("\n")

    for read_file_proc_str in read_file:
        for ex_proc_item in except_proc:
            read_porc_str = ("/"+ex_proc_item+" ")
            if read_porc_str in read_file_proc_str:
                print ("Lines containing [PROCESS NAME : "+ex_proc_item+"] have been excluded." )
                temp_list.remove(read_file_proc_str)

    read_file = temp_list

    proc=""
    for item in read_file:
        proc += (item +"\n")
    print proc


    for temp_list_ip_str in read_file:
        for ex_ip_item in except_ip:
            read_ip_str = (ex_ip_item+":*")
            print temp_list_ip_str
            print read_ip_str
            #read_ip_str = (" "+ex_ip_item+":")
            if read_ip_str in temp_list_ip_str:
                print ("Lines containing [IP : "+ex_ip_item+"] have been excluded." )
                temp_list.remove(temp_list_ip_str)

    
    
    read_file = temp_list
    
    ip=""
    for item in read_file:
        ip += (item +"\n")
    print ip
    
    #print ("################################",read_file)

    for temp_list_port_str in read_file:
        #print temp_list_port_str
        for ex_port_item in except_port:
        #    print ex_port_item
            read_port_str = (":"+ex_port_item+" ")
            if read_port_str in temp_list_port_str:
                print ("Lines containing [PROT : "+ex_port_item+"] have been excluded." )
                temp_list.remove(temp_list_port_str)

    read_file = temp_list
    
    port=""   
    for item in read_file:
        port += (item +"\n")
    print port

    print ("########## result ##########")
    result_file=""
    for item in read_file:
        result_file += (item +"\n")
    print result_file
with open('C:/Users/user/Desktop/Norma/TEST/result_file.txt','r+') as f:
#with open('./result_file','w+') as f:
#f.write(item)
    f.write(result_file)