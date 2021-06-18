import commands
import ConfigParser

config=ConfigParser.ConfigParser()
command = commands.getstatusoutput

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
    print ("\n"+"############### Exception List ############### ")
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
    print ("###############################################"+"\n\n")
    temp_list=[]
    ## read_file = origin file list
    ## ex_xxx = except list
    for read_file_idx in read_file:
        
        for proc_idx in except_proc:
            # read_except_proc=("/"+proc_idx)
            read_except_proc=(proc_idx)
            
            # if read_except_proc in read_file_idx:
                # print ("read_file_idx####################"+read_file_idx)
                # print ("read_except_proc####################"+read_except_proc)
            if read_except_proc not in read_file_idx : #compare str and str
                # print "########## read_file_idx ##########"
                # print type (read_file_idx)
                # print (read_file_idx)
                
                # print (read_except_proc)
                
                for ip_idx in except_ip:
                    read_except_ip = (" "+ip_idx+":")
                    #print read_except_ip

                    if read_except_ip not in read_file_idx :
                        
                        for port_idx in except_port:
                            read_except_port = (":"+port_idx+" ")

                            if read_except_port not in read_file_idx:
                                temp_list.append(read_file_idx)

                            #elif read_except_port in read_file_idx:
                            else :
                                #print ("It was Excluded from the list because of " + port_idx)
                                break
                    elif read_except_ip in read_file_idx:
                        
                        #print ("It was Excluded from the list because of " + ip_idx)
                        break
            elif read_except_proc in read_file_idx:
                print ("IIIIIIIIIIIIIIIIIIIII")
                print read_except_proc
                # print ("It was Excluded from the list because of " + proc_idx)
                # break

    #print temp_list
    temp_list.sort()
    result_list = list(set(temp_list))
    #print result_list
    print("###### result ########")
    #print ("result_list",type(result_list))
    result_file=""

    for item in result_list:
        result_file += (item +"\n")
        
print result_file

with open('./result_file','w+') as f:
    #f.write(item)
    f.write(result_file)