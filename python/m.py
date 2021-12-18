def mmprint():
    f = open("mlog", 'r', True)
    while True:
        ch = f.read(1)
        if not ch: break
        print(ord(ch))
    f.close()
def mmprint1(nn):
    nnb = 1024*1024*50
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

#mmwrite()
#mmprint()
