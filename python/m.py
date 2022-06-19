def mmprint():
    f = open("mlog", 'r', True)
    while True:
        ch = f.read(1)
        if not ch: break
        print(ord(ch))
    f.close()
def mmprint1(nn):
    import time
    nnb = 1024*1024*200
    #nnb = 10
    nni = 0
    print('aaa '+str(nn)+' '+str(nnb))
    f = open("mlog", 'r', True)
    while True:
        ch = f.read(1)
        nni = nni +1
        if not ch: break
        if nni<=nn*nnb or nni>(nn+1)*nnb: continue
        print(ord(ch))
        if nni==100:
            print(ord(ch))
        if nni%(1024*10)==0:
            time.sleep(1) 
    f.close()
def mmprint1_1(nn):
    import time
    nnb = 1024*1024*200
    #nnb = 10
    nni = 0
    print('aaa '+str(nn)+' '+str(nnb))
    f = open("mlog", 'r', True)
    aa=f.read()
    f.close()
    #while True:
    for ch in aa:
        #ch = f.read(1)
        nni = nni +1
        if not ch: break
        if nni<=nn*nnb or nni>(nn+1)*nnb: continue
        print(ord(ch))
        if nni==100:
            print(ord(ch))
        if nni%(1024*10)==0:
            time.sleep(1) 
def mmprint1_2(nn, mskip):
    import time
    nnb = 1024*1024*200
    #nnb = 10
    nni = 0
    print('aaa '+str(nn)+' '+str(nnb))
    f = open("mlog", 'r', True)
    aa=f.read()
    f.close()
    #while True:
    for ch in aa:
        #ch = f.read(1)
        nni = nni +1
        if not ch: break
        if nni<=mskip : continue
        if nni<=nn*nnb or nni>(nn+1)*nnb: continue
        print(ord(ch))
        if nni==100:
            print(ord(ch))
        if nni%(1024*10)==0:
            time.sleep(1) 
def mmprint2():
    import random
    for ii in range(100):
        print(random.randint(0,255))
    f = open("mlog", 'r', True)
    nni = 0
    nni1 = 0
    while True:
        ch = f.read(1)
        nni = nni +1
        if nni>=1024*1024*1024:
            nni1 = nni1 +1
            nni = 0
        if not ch: break
        print(ord(ch))
        if nni==100 and nni1==0:
            print(ord(ch))
    f.close()

def mmwrite():
    import struct
    fw = open("mw.txt", 'wb', True)

    f = open("mlog", 'r', True)
    line = f.readline()             
    linenon=line.strip('\n')
    linenum=0
    if len(linenon):
        linenum=int(linenon)
        a=struct.pack('B', linenum)
        fw.write(a)
    #print(linenum,end='')
    while line:
        line = f.readline()
        linenon=line.strip('\n')
        linenum=0
        if len(linenon):
            linenum=int(linenon)
            a=struct.pack('B', linenum)
            fw.write(a)
        #print(linenum,end='')
    
    f.close()
    fw.close()
def mmprint1_1b(nn):
    import time
    import base64
    nnb = 1024*1024*2
    btyper = 108
    #nnb = 10
    nni = 0
    print('aaa '+str(nn)+' '+str(nnb))
    f = open("mlog", 'r', True)
    aa = []
    while True:
        bb=f.read(btyper)
        if len(bb) <= 0:
            break
        aa.append(base64.b64encode(bb))
    f.close()
    #while True:
    for ch in aa:
        #ch = f.read(1)
        nni = nni +1
        if not ch: break
        if nni<=nn*nnb or nni>(nn+1)*nnb: continue
        print(ch)
        if nni==100:
            print(ch)
        if nni%(1024)==0:
            time.sleep(1) 
    print('bbb '+str(nn)+' '+str(nnb))
def mmwrite_b():
    import base64
    import struct
    fw = open("mw.txt", 'wb', True)

    f = open("mlog", 'r', True)
    lines = f.readlines()             
    for line in lines:
        linenon=line.strip('\n')
        bb=base64.b64decode(linenon)
        fw.write(bb)
    f.close()
    fw.close()

#mmwrite()
#mmprint()
#print(__name__)
#mmdd=[1,1,2]
#mmprint1(0)
#mmprint2()
#mmprint1_1(2)
#mmprint1_1b(0)
#mmwrite_b()
