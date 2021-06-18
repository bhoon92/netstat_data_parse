import commands
import ConfigParser
import logging
import os



class netstat:
    config  = ConfigParser.ConfigParser()
    command = commands.getstatusoutput
    except_proc_idx=""
    flag    =   ""
    working_list=""

    # except_ip_list=""
    # except_port_list=""
    # except_proc_list="" 

    