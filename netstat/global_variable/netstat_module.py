import netstat_logger
import global_class
import commands
import ConfigParser

#=======================================================#
def get_origin_file():

    convert_str_to_list(glVar.ORIGIN_FILE)
    #, glVar.origin_file_list) # delimter '\n'
    return False

#=======================================================#

#=======================================================#
def convert_str_to_list(origin_file):
#, list_name):
    
    with open (origin_file,'r+') as f:
        read_file = f.read()
        glVar.origin_file_list = read_file.split('\n')
    return glVar.origin_file_list
#=======================================================#

#=======================================================#
def get_except_list(section,key):
    
    config.read(glVar.EXCEPT_CONF)
    
    tmp         = config.get(section, key)
    except_list = tmp.split(',')

    return except_list
#=======================================================#

#=======================================================#
def exception_list_print():
    
    glVar.flag="EX"
    
    glVar.except_ip_list   = get_except_list('EXCEPT', 'except_ip')
    glVar.except_port_list = get_except_list('EXCEPT', 'except_port')
    glVar.except_proc_list = get_except_list('EXCEPT', 'except_process')

    print ("\n======================== Exception List ======================== ")
    print ("Except List IP      :", glVar.except_ip_list)
    print ("Except List PORT    :", glVar.except_port_list)
    print ("Except List PROCESS :", glVar.except_proc_list)
    print ("=================================================================\n")
    
    write_log(glVar.flag, glVar.flag)

#=======================================================#

#=======================================================#
def make_working_list(obj_list):
    
    temp_str=""
    for item in obj_list:
        temp_str += (item +"\n")
    working_list  = temp_str.split("\n")

    return working_list
#=======================================================#

#=================== Except Function ===================#
def compare_list(TYPE, std_dif_list, except_list): 
    
    get_origin_file()
    glVar.flag          = TYPE

    if len(glVar.dif_temp_list) <= 0:
        glVar.dif_temp_list = std_dif_list[:]

    for std_idx in glVar.dif_temp_list:

        for except_idx in except_list:

            if len(except_idx) > 0 and TYPE == "IP":
                read_except_idx = (" "+except_idx+":")
            elif len(except_idx) > 0 and TYPE == "PORT":
                read_except_idx = (":"+except_idx+" ")
            elif len(except_idx) > 0 and TYPE == "PROC":    
                read_except_idx = ("/"+except_idx+" ")
            else : 
                break

            if read_except_idx in std_idx:
                glVar.dif_temp_list.remove(std_idx)
                print ("[Lines : "+std_idx+" containing [INDEX : "+except_idx+"] have been excluded." )
                write_log(glVar.flag, except_idx)

            else :
                break
    
    return glVar.dif_temp_list
    
#=======================================================#

#=======================================================#
def result_save_file():

    result_list=""
    
    # working_proc_list = proc_dif_list()

    for result_list_idx in glVar.dif_temp_list:
        result_list += (result_list_idx +"\n")

    print ("\n########## result ##########\n")
    print result_list
    
    with open ('./result_file','w+') as f:
        f.write(result_list)

#=======================================================#

#=======================================================#
def main():
    code, make_netstat = command(glVar.MAKE_NETSTAT)
    code, copy_netstat = command(glVar.COPY_NETSTAT)
    
    exception_list_print()
    get_origin_file()
    
    glVar.except_ip_list = get_except_list('EXCEPT', 'except_ip')
    glVar.except_port_list = get_except_list('EXCEPT', 'except_port')
    glVar.except_proc_list = get_except_list('EXCEPT', 'except_process')
    
    compare_list("IP", glVar.origin_file_list, glVar.except_ip_list)
    compare_list("PORT", glVar.dif_temp_list, glVar.except_port_list)
    compare_list("PROC", glVar.dif_temp_list, glVar.except_proc_list)

    result_save_file ()


#=======================================================#
if __name__== '__main__':
    
    write_log   = netstat_logger.write_logging
    command     = commands.getstatusoutput
    config      = ConfigParser.ConfigParser()
    glVar       = global_class.global_variable

    main()


#=======================================================#
# def exception_list():

#     config.read(glVar.EXCEPT_CONF)

#     except_ip_list = config.get('EXCEPT', 'except_ip')
#     except_ip_list = except_ip_list.split(',')

#     except_port_list = bring_VO.config.get('EXCEPT', 'except_port')
#     except_port_list = except_port_list.split(',')

#     except_proc_list = bring_VO.config.get('EXCEPT', 'except_process')
#     except_proc_list = except_proc_list.split(',')

#     return except_ip_list, except_port_list, except_proc_list
#=======================================================#
'''
#==================IP comparison function===============#
def ip_dif_list():
    
    glVar.flag="IP"
    glVar.netstat_ip_list =  glVar.origin_file_list[:]

    # working_ip_list  = make_working_list(list_origin_list)

    for std_ip_idx in glVar.origin_file_list:

        for except_ip_idx in glVar.except_ip_list:

            if len(except_ip_idx) > 0:
                read_except_ip_idx = (" "+except_ip_idx+":")

                if read_except_ip_idx in std_ip_idx:
                    glVar.netstat_ip_list.remove(std_ip_idx)
                    print ("Lines containing [IP : "+except_ip_idx+"] have been excluded." )
                    write_log(glVar.flag, except_ip_idx)

            else :
                break
    
    working_ip_list = make_working_list(working_ip_list)
    
    return working_ip_list
#=======================================================#

#================Port comparison function===============#
def port_dif_list():

    glVar.flag="PORT"
    
    working_ip_list  = ip_dif_list()
    working_port_list = make_working_list(working_ip_list)
    
    for std_port_idx in working_ip_list:
        
        for except_port_idx in glVar.except_port_list:
            
            if len(except_port_idx) > 0:
                read_except_port_idx = (":"+except_port_idx+" ")
                
                if read_except_port_idx in std_port_idx:
                    working_port_list.remove(std_port_idx)
                    print ("Lines containing [PROT : "+except_port_idx+"] have been excluded." )
                    write_log(glvar.flag,except_port_idx)
            else :
                break
    
    working_port_list = make_working_list(working_port_list)
    
    return working_port_list
#=======================================================#

#===========Process comparison function=================#
def proc_dif_list():

    bring_VO.flag = "PROC"

    working_port_list = port_dif_list()
    except_proc_list  = exception_list()
    working_proc_list = make_working_list(working_port_list)

    for std_proc_idx in working_port_list:
      
        for except_proc_idx in except_proc_list[2]:
      
            if len(except_proc_idx) > 0:
                read_except_proc_idx = ("/"+except_proc_idx+" ")
      
                if read_except_proc_idx in std_proc_idx:
                    working_proc_list.remove(std_proc_idx)
                    print ("Lines containing [PROC : "+ except_proc_idx +"] have been excluded." )
                    write_log(bring_VO.flag, except_proc_idx)
      
            else:
                break

    working_proc_list = make_working_list(working_proc_list)

    return working_proc_list
#=======================================================#
'''