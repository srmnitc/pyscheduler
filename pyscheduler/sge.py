"""
A small scheduler script for submission of jobs.

"""
import os
import subprocess as sub

class sge(object):
    def __init__(self, outfile):
        self.outfile = outfile
        self.initialized = True
        self.header = "#!/bin/bash"
        self.essential = {
            "N" : "pyschedule",
            "S" : "/bin/bash",
            "r" : "n",
            "cwd" : " ",
            "h_rt" : "7:59:00",
            "qname" : "serial.q",
            "h_vmem" : "6G",
            "j" : "y",
            "R" : "y",
            "pe" : "smp",
            "cores" : 1,
            "P" : "ams.p"        
        }

        self.output = "sge.out"
        self.error = "sge.err"
        self.modules = []
        self.commands = []
        self.maincommand = []
        self.argarray = []
    
    def write_script(self):
        """
        Write out the script
        """

        #prep the essentials
        with open(self.outfile,"w") as fout:
            #write out the header
            fout.write(self.header)
            fout.write("\n")

            #write out essentials
            fout.write("#$ -N %s\n" % self.essential["N"])
            fout.write("#$ -S %s\n" % self.essential["S"])
            fout.write("#$ -r %s\n" % self.essential["r"])
            fout.write("#$ -cwd %s\n" % self.essential["cwd"])
            fout.write("#$ -l h_rt=%s\n" % self.essential["h_rt"])
            fout.write("#$ -l qname=%s\n" % self.essential["qname"])
            fout.write("#$ -l h_vmem=%s\n" % self.essential["h_vmem"])
            fout.write("#$ -j %s\n" % self.essential["j"])
            fout.write("#$ -R %s\n" % self.essential["R"])
            fout.write("#$ -pe %s %s \n" % (self.essential["pe"], str(self.essential["cores"])))
            fout.write("#$ -P %s\n" % self.essential["P"])

            #write modules
            for module in self.modules:
                fout.write(" ".join(["module", "load", module]))
                fout.write("\n")

            #write extra commands
            for command in self.commands:
                fout.write(" ".join(command))
                fout.write("\n")

            #write main command with arg array
            argarray = " ".join(self.argarray)
            maincommand = " ".join(self.maincommand) 
            fout.write(" ".join([maincommand, argarray]))


    def submit(self):
        """
        Submit job
        """
        #os.system("qsub %s", self.script)
        cmd = ['qsub', self.script]
        proc = sub.Popen(cmd, stdin=sub.PIPE,stdout=sub.PIPE,stderr=sub.PIPE)
        out,err = proc.communicate(input="")
        proc.wait()
        print(out)
