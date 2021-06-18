import global_class
import logging
import logging.handlers


def write_logging(flag, log_value):
    glVar = global_class.global_variable
        
    logger      = logging.getLogger()
    formatter   = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler = logging.FileHandler('practice.log')
    
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(level = logging.DEBUG)

    try:
            
        if flag == "EX":
            logging.info ("======================== Exception List =========================")
            logging.info ("Except List IP      : ")
            logging.info (glVar.except_ip_list)
            logging.info ("Except List PORT    :")
            logging.info (glVar.except_port_list)
            logging.info ("Except List PROCESS :")
            logging.info (glVar.except_proc_list)
            logging.info ("=================================================================")
            
        elif flag == "IP":
            logging.info ("Lines containing [IP : "+log_value+"] have been excluded." )
        elif flag == "PORT":
            logging.info ("Lines containing [PROT : "+log_value+"] have been excluded." )
        elif flag == "PROC":
            logging.info ("Lines containing [PROCESS : "+log_value+ "] have been excluded.")

    except Exception as e:
        
        logging.error ("============== ERROR ===================")
        logging.error (e)
        logging.error ("==============  END  ===================")
        


    finally:
        # logger.removeHandler(streamHandler)
        logger.removeHandler(fileHandler)