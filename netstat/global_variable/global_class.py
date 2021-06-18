# import netstat_module

class global_variable(object):

    # Linux Command
    MAKE_NETSTAT    = "netstat -lntup > origin_netstat"
    COPY_NETSTAT    = "cp origin_netstat result_file"
    
    # Linux File
    ORIGIN_FILE     = './origin_netstat'
    EXCEPT_CONF     = './exception.conf'
    
    # Str
    flag     = ""
    temp_str = ""

    # List
    origin_file_list = []
    
    except_ip_list   = []
    except_port_list = []
    except_proc_list = []
    dif_temp_list    = []

    netstat_ip_list    = []
    netstat_port_list  = []
    netstat_proc_list  = []
    