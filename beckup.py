import os
import subprocess

#A name of the dir to take info from 
DIRTOCPFROM = "/var/snap/docker/common/var-lib-docker/volumes/massage/_data/*"

#A name of the dir to put info
DIRTOCPTO = "/backups"

def copyfiles():
    """Copies any files to the named file."""

    pipe = subprocess.Popen(["ls"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, _ = pipe.communicate()
    _, path = DIRTOCPTO.split("/")
    if path in stdout.decode():
        subprocess.run(f"cp {DIRTOCPFROM} {DIRTOCPTO}")
    os.mkdir(DIRTOCPTO)
    subprocess.run(f"cp {DIRTOCPFROM} {DIRTOCPTO}")

if __name__ == "__main__":
    copyfiles()