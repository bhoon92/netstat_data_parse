import gl_class
import global_class
import copy
gl=global_class.global_variable
# class Global(object):
#     a="AAAAAAAAAAAAAAAAAA"
#     b="BBBBBBBBBBBBBBBBBB"
#     c="CCCCCCCCCCCCCCCCCC"

# class varTest(GL):

def p():
    # GL=gl_class.Global

    GL.c = GL.a + GL.b

    # asd=varTest()
    print (GL.a)
    print (GL.c)
    # asd.p()
    print (GL.c)
def main():
    
    p()

if __name__== '__main__':
    GL = gl_class.Global
    main()


y="aaaa"
y="nnnnnnnnnn"
y="[[[[[[[["
print y

def test ():
    
    gl.netstat_ip_list=[1,23,4,5,6]
    gl.netstat_port_list = gl.netstat_ip_list[:]

    print gl.netstat_ip_list

def test1 ():
    
    
    gl.netstat_ip_list.remove(1)
    gl.netstat_ip_list.remove(23)

    print gl.netstat_ip_list

    print gl.netstat_port_list

def test2():

    gl.netstat_ip_list.remove(4)
    print gl.netstat_ip_list

print 'DDDDDDDDDDDDD"'
test()
print 'test1'
test1()
test2()
#print gl.netstat_ip_list
#print gl.netstat_port_list


def compare_list(TYPE, except_list):  ##
    
    except_ip_list=[1,23,4,5,6]
    if "IP" in TYPE:
        gl.flag="IP"
        except_list = except_ip_list[:]
        print 'IP'
        print except_list
    elif "PORT" in TYPE:
        gl.flag="PORT"
        except_list = gl.except_prot_list[:]
        print 'PROT'
    elif "PROC" in TYPE:
        gl.flag="PROC"
        except_list = gl.except_proc_list[:]
        print 'PRoc'
    print except_list

# netstat_ip_list=[1,23,4,5,6]
print '###########'
# compare_list(IP ,test )



def var_test():
    gl.origin_file_list = [1,2,3,4,56,6,7,0]
    
    return gl.origin_file_list
def var_test2():
    print var_test()
    print gl.origin_file_list

var_test2()

