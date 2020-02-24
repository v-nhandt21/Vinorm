import subprocess,os
def TTSnorm1(text):
    with open("input.txt","w+") as fw:
        fw.write(text)
    myenv = os.environ.copy()
    myenv['LD_LIBRARY_PATH'] = 'lib'
    subprocess.check_call(['./main'], env=myenv)
    with open("output.txt","r") as fr:
        text=fr.read()
    return text
def testnorm(text):
    return text