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
    temp_list=read_file
    for read_file_idx in range(len(read_file)):
        str_read_file=read_file[read_file_idx]

        for idx in range(len(except_ip)):
            read_except_ip = (" "+except_ip[idx]+":")
            if read_except_ip in str_read_file:
                del temp_list [read_file_idx]
                

        for idx in range(len(except_port)):
            read_except_port = (":"+except_port[idx]+" ")
            if read_except_port in str_read_file:
                del temp_list[read_file_idx]
                

        for idx in range(len(except_proc)):
            read_except_proc = ("/"+except_proc[idx]+"\n")
            if read_except_proc in str_read_file:
                del temp_list[read_file_idx]
                
    
        
    

                