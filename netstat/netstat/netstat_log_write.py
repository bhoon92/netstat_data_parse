import netstat_VO
import logging
import logging.handlers

# logger      = logging.getLogger()
# formatter   = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logger.setLevel(level = logging.DEBUG)

# fileHandler = logging.FileHandler('practice.log')
# fileHandler.setFormatter(formatter)
# bring_VO = netstat_VO.netstat

# logger.addHandler(fileHandler)

# streamHandler   = logging.StreamHandler()
# streamHandler.setFormatter(formatter)
# logger.addHandler(streamHandler)


def write_logging(flag, log_value):
    import netstat_module_practice
        
    logger      = logging.getLogger()
    formatter   = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger.setLevel(level = logging.DEBUG)

    fileHandler = logging.FileHandler('practice.log')
    fileHandler.setFormatter(formatter)
    bring_VO = netstat_VO.netstat

    logger.addHandler(fileHandler)
    bring_VO.flag   =""
    ns_module       = netstat_module_practice

    except_ip_list, except_port_list, except_proc_list = ns_module.exception_list()

    try:
            
        if flag == "EX":
            logging.info ("======================== Exception List =========================")
            logging.info ("Except List IP      : ")
            logging.info (except_ip_list)
            logging.info ("Except List PORT    :")
            logging.info (except_port_list)
            logging.info ("Except List PROCESS :")
            logging.info (except_proc_list)
            logging.info ("=================================================================")
            
        elif flag == "IP":
            logging.debug ("Lines containing [IP : "+log_value+"] have been excluded." )
        elif flag == "PORT":
            logging.debug ("Lines containing [PROT : "+log_value+"] have been excluded." )
        elif flag == "PROC":
            logging.debug ("Lines containing [PROCESS : "+log_value+ "] have been excluded.")

    except Exception as e:
        
        logging.error ("ERROR============================")
        logging.error (e)
        logging.error ("END==============================")
        


    finally:
        # logger.removeHandler(streamHandler)
        # logger.removeHandler(fileHandler)
        print ("END")