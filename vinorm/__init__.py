
import subprocess,os
import imp
def TTSnorm(text, punc = False, unknown = True, lower = True, rule = False ):
    A=imp.find_module('vinorm')[1]

    #print(A)
    I=A+"/input.txt"
    with open(I,"w+") as fw:
        fw.write(text)

    myenv = os.environ.copy()
    myenv['LD_LIBRARY_PATH'] = A+'/lib'

    E=A+"/main"
    Command = [E]
    if punc:
        Command.append("-punc")
    if unknown:
        Command.append("-unknown")
    if lower:
        Command.append("-lower")
    if rule:
        Command.append("-rule")
    subprocess.check_call(Command, env=myenv, cwd=A)
    
    O=A+"/output.txt"
    with open(O,"r") as fr:
        text=fr.read()
    TEXT=""
    S=text.split("#line#")
    for s in S:
        if s=="":
            continue
        TEXT+=s+". "


    return TEXT