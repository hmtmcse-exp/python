import subprocess


process = subprocess.Popen(args="ping 10.0.40.137", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = process.stdout.readline()
while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.decode('cp949').strip())
