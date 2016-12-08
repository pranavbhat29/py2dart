# Program to create a shell which converts a python code to Dart or vice-versa

import sys

print "===> Py2D.A.R.T --- The Online Python to DART command translator shell <=====\n\n"
print " --- By. Pranav Bhat T ---"
print "\n\n\n"
print " Type 'help', 'developer_details','exit','constraints', for their respective purposes "

def exitproc():
    print "\n\n\t-----------------------------------------\n\n\t\t Thank You for using Py2D.A.R.T \n\n\t---------------------------------------------\n"
    k=raw_input()
def opendoc(cmd):
    fp = open(cmd+".txt","r")
    lines = fp.readlines()
    fp.close()
    for line in lines:
        print line
    print "\n\n"
    out = raw_input(" Do you want to continue using Py2D.A.R.T ? Yes or No : ")
    return out.lower()

def processcmd(cmd):
    block = ['def','for','if','while']
    if cmd in block:
        return False
    return True

def writewithtype(varibl):
    if len(varibl)>1 and varibl[0].islower() and varibl[1].isupper():
        typedet = varibl[0]
        if typedet=='n':
            return "int "+varibl
        elif typedet=='d':
            return "double "+varibl
        elif typedet=='c':
            return "char "+varibl
        elif typedet=='s':
            return "String "+varibl
        else:
            return 0
    else:
        return "var "+varibl

def printnonblock(cmd):
    main = cmd.split()[0]
    output=""
    if main=="print":
        if "'" in cmd:
            val = cmd.split("'")[1]
            val="'"+val+"'"
        elif '"' in cmd:
            val = cmd.split('"')[1] # to print strings
            val = '"'+val+'"'
        else:
            val = cmd.split()[1] # to print variables
        output = 'print('+val+') ;'
    elif main=="return":
        output='return('+cmd.split()[1]+');'
    elif '=' in cmd:
        main = cmd.split("=")
        lhs = main[0]
        rhs = main[1]
        if rhs.replace(" ","")=='':
            print "\n Not Possible to Convert in DART "
            print "\n Did You Mean to write '",lhs,"'?"
            print " This gets translated to "
            print "  ",writewithtype(lhs)
            output = writewithtype(lhs)+" ;"
        else:
            output = "\n\n"+writewithtype(lhs)+" ;\n"+cmd+" ;\n"
    else:
        output=cmd+";"
    return output
def processfor(cmd):
    params=cmd.split("for ")[1]
    vals=params.strip("):").split('in')
    var=vals[0].replace(" ","")
    init=writewithtype(var)
    ranges = vals[1].split("range(")
    ranges = ranges[::-1]
    vvv=ranges[0].replace(" ","").split(",")
    if len(vvv)==1:
        low=0
        high=vvv[0]
    else:
        low=vvv[0]
        high=vvv[1]
    final="for("+init+"="+str(low)+";"+str(var)+" < "+str(high)+";"+str(var)+"++)"
    return final

def processifwhile(cmd,flg):
    if flg:
        params=cmd.split("if")[1]
        start='if'
    else:
        params=cmd.split("while")[1]
        start='while'
   # print params.index("and")
    params=params.replace("and","&&").replace("or","||")
    params=params.replace(":","")
    fin=start+" ( "+params+" ) "
    return fin
def processdef(cmd):
    name=cmd.split('(')[0].split()[1].replace(" ","")
    argmnts=cmd.strip("):").split("(")[1].split(",")
    alist=[]
    for arg in argmnts:
        alist.append(writewithtype(arg))
    aliststr=' , '.join(alist)
    return writewithtype(name)+"("+aliststr+")"
def printblock(cmd,i):
    line=''
    fincmd=' '*i+'{\n'
    while True:
        cur=raw_input().strip()
        line+=(cur+'\n')
        if cur=='$':
            break
        check=processcmd(cur.split()[0])
        if check:
            fincmd+=("  "*(i+1)+printnonblock(cur)+"\n")
        else:
            fincmd+=("  "*(i+1)+printblock(cur,i+1)+"\n")
    fincmd+=(' '*i+'}')
    commd=cmd.split()[0]
    if commd=='for':
        stline=processfor(cmd)
    elif commd=='if':
        stline=processifwhile(cmd,1)
    elif commd=='while':
        stline=processifwhile(cmd,0)
    else:
        stline=processdef(cmd)
    finval=stline+"\n"+fincmd 
    return finval
checkin=int(raw_input(" Do you want to read a code file and write to another ? "))
if checkin:
    sin=sys.stdin
    infile=open(raw_input("Input File Name:").strip(),"r")
    ofname=raw_input("Output File Name:").strip()
    outfile=open(ofname,"w")
    sys.stdin=infile
    sout=sys.stdout
    sys.stdout=outfile
if checkin:
    prompt=''
else:
    prompt="\n>>> "
while True:
    cmd = raw_input(prompt).strip()
    if cmd.lower()=="exit":
        if not checkin:
            exitproc()
        break
    elif cmd.lower()=="help" or cmd.lower()=="developer_details" or cmd.lower()=='constraints':
        out=opendoc(cmd)
        if out=="yes":
            continue
        else:
            exitproc()
            break
    out = processcmd(cmd.split()[0])
    if out:
        output=printnonblock(cmd)
        if not checkin:
            print "\n Python Input : ",cmd
            print "\n  DART Output : ",output,"\n"
        else:
            print output
    else:
        output=printblock(cmd,0)
        if not checkin:
            print "\n\n\n  DART Output : \n---------------------\n",output,"\n"
        else:
            print output
if checkin:
    sys.stdin=sin
    sys.stdout=sout
    infile.close()
    outfile.close()
    print " Here is the Output File : Name ---> "+ofname+"\n-----------------------------------------------\n"
    fp = open(ofname,"r")
    lines=fp.readlines()
    for lin in lines:
        print lin
    x=raw_input()
