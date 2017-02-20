import subprocess

import sys


class MSBuild:

    def build(self):
        print('Build Start ************************')
        process = subprocess.Popen(args="ping 10.0.40.137", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            nextline = process.stdout.readline()
            if nextline == b'' and process.poll() != None:
                break
            sys.stdout.write(nextline.decode('cp949'))  # adjust the codepage for your console
            sys.stdout.flush()

        output = process.communicate()[0]
        exitCode = process.returncode

        if (exitCode == 0):
            build_result = True
            pass  # return output
        else:
            build_result = False
            
        print('************************')
        print('build finished %d ' % process.returncode)












msbuild = MSBuild()
msbuild.build()