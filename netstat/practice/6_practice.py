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
    read_file=read_file.split('\n') ## netstat -> list

    print("#### read_file ####")

    for item in read_file:
        print type(item)
        print(item)

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
    
    temp_list=[]
    for read_file_idx in range(len(read_file)):
        if(read_file_idx != 0 and read_file_idx != 1):
            str_read_file=read_file[read_file_idx]

            print("str_read_file : "+str_read_file)
            
            for idx in range(len(except_proc)):
                read_except_proc = (except_proc[idx])

                print("read_except_proc : "+read_except_proc)
                
                if str_read_file.find(read_except_proc) == -1 :
                #if read_except_proc not in str_read_file:
                    temp_list.append(read_file[read_file_idx])

            for idx in range(len(except_ip)):
                read_except_ip = (" "+except_ip[idx]+":")
                if read_except_ip not in str_read_file:
                    temp_list.append(read_file[read_file_idx])
                    
            for idx in range(len(except_port)):
                read_except_port = (":"+except_port[idx]+" ")
                if read_except_port not in str_read_file:
                    temp_list.append(read_file[read_file_idx])
    
    #print temp_list
    result_list = list(set(temp_list))
    
    print("###### result ########")
    print type(result)
    for item in result_list:
        print(item)
