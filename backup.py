import os
import subprocess


DIRTOCPFROM = "/var/snap/docker/common/var-lib-docker/volumes/massage/_data/*"
DIRTOCPTO = "/backups"

def copyfiles():
    pipe = subprocess.Popen(["ls"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, _ = pipe.communicate()
    _, path = DIRTOCPTO.split("/")
    os.mkdir(DIRTOCPTO) if path not in stdout.decode() else None
    _, dirs, files = [elems for elems in os.walk(DIRTOCPTO)][0]
    subprocess.call([f"rm -r {DIRTOCPTO}/*"], shell=True) if dirs or files else None
    subprocess.call([f"cp -r {DIRTOCPFROM} {DIRTOCPTO}"], shell=True)

if __name__ == "__main__":
    copyfiles()
