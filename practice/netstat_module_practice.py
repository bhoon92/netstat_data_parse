import netstat_log_write
import netstat_VO

bring_VO = netstat_VO.netstat ## Variable class
write_log = netstat_log_write.write_log

def file_read():

    (status_code, origin_netstat) = bring_VO.command("netstat -lntup > origin_netstat")
    (status_code, make_result_file) = bring_VO.command("cp origin_netstat result_file")

    with open ('./origin_netstat','r+') as f:
        read_file = f.read()
        list_file = read_file.split('\n')
    
    return list_file

def exception_list():

    bring_VO.config.read('./exception.conf')

    except_ip_list = bring_VO.config.get('EXCEPT', 'except_ip')
    except_ip_list = except_ip_list.split(',')

    except_port_list = bring_VO.config.get('EXCEPT', 'except_port')
    except_port_list = except_port_list.split(',')

    except_proc_list = bring_VO.config.get('EXCEPT', 'except_process')
    except_proc_list = except_proc_list.split(',')

    return except_ip_list, except_port_list, except_proc_list

def exception_list_print():
    print ("############################"+bring_VO.flag)
    bring_VO.flag="EX"
    print ("############################"+bring_VO.flag)
    
    except_ip_list, except_port_list, except_proc_list = exception_list()

    print ("\n======================== Exception List ======================== ")
    print ("Except List IP      :",except_ip_list)
    print ("Except List PORT    :",except_port_list)
    print ("Except List PROCESS :",except_proc_list)
    print ("=================================================================\n")

    write_log(bring_VO.flag)

def make_working_list(obj_list):
    
    working_list=""
    
    for item in obj_list:
        working_list += (item +"\n")
    dif_working_list = working_list.split("\n")

    return dif_working_list

## IP comparison function
def ip_dif_list():
    
    global except_ip_idx
    bring_VO.flag="IP"

    list_origin_list = file_read()
    working_ip_list  = make_working_list(list_origin_list)
    except_ip_list   = exception_list()

    for std_ip_idx in list_origin_list:
        for except_ip_idx in except_ip_list[0]:
            if len(except_ip_idx) > 0:
                read_except_ip_idx = (" "+except_ip_idx+":")
                if read_except_ip_idx in std_ip_idx:
                    working_ip_list.remove(std_ip_idx)
                    print ("Lines containing [IP : "+except_ip_idx+"] have been excluded." )
                    write_log(bring_VO.flag)
            else :
                break
    
    working_ip_list = make_working_list(working_ip_list)
    
    return working_ip_list

## Port comparison function
def port_dif_list():

    global except_port_idx
    bring_VO.flag="PORT"
    
    working_ip_list  = ip_dif_list()
    except_port_list = exception_list()
    working_port_list = make_working_list(working_ip_list)
    
    for std_port_idx in working_ip_list:
        
        for except_port_idx in except_port_list[1]:
            
            if len(except_port_idx) > 0:
                read_except_port_idx = (":"+except_port_idx+" ")
                
                if read_except_port_idx in std_port_idx:
                    working_port_list.remove(std_port_idx)
                    print ("Lines containing [PROT : "+except_port_idx+"] have been excluded." )
                    write_log(bring_VO.flag)
            else :
                break
    
    working_port_list = make_working_list(working_port_list)
    
    return working_port_list

## Process comparison function
def proc_dif_list():

    global except_proc_idx
    bring_VO.flag="PROC"
    
    working_port_list = port_dif_list()
    except_proc_list  = exception_list()
    working_proc_list = make_working_list(working_port_list)

    for std_proc_idx in working_port_list:

        for except_proc_idx in except_proc_list[2]:

            if len(except_proc_idx) > 0:
                read_except_proc_idx = ("/"+except_proc_idx+" ")

                if read_except_proc_idx in std_proc_idx:
                    working_proc_list.remove(std_proc_idx)
                    print ("Lines containing [PROC : "+except_proc_idx+"] have been excluded." )
                    write_log(bring_VO.flag)
            else:
                break

    working_proc_list = make_working_list(working_proc_list)

    return working_proc_list

def result_save_file():

    result_list=""
    
    working_proc_list=proc_dif_list()

    for result_list_idx in working_proc_list:
        result_list += (result_list_idx +"\n")

    print ("\n########## result ##########\n")
    print result_list

    with open ('./result_file','w+') as f:
        f.write(result_list)


def main():
    exception_list_print()
    result_save_file ()
    
if __name__== '__main__':
    main()

    