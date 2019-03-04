"""
A small scheduler script for submission of jobs.

"""
import os
import subprocess as sub

class slurm(object):
    def __init__(self, outfile):
        self.outfile = outfile
        self.initialized = True
        self.header = "#!/bin/bash"
        self.essential = {
            "job-name" : "pyschedule",
            "partition" : "shorttime",
            "time" : "1:59:00",
            "ntasks" : 4,
            "mem-per-cpu" : "3GB",
            "hint" : "no-multithread"        
        }

        self.output = "slurm.out"
        self.error = "slurm.err"
        self.modules = []
        self.commands = []
        self.maincommand = []
        self.argarray = []
    
    def write_script(self):
        """
        Write out the script
        """

        #prep the essentials
        dictcopy = self.essential
        self.statements = []

        #process essentials
        for key, vals in dictcopy.iteritems():
            key = "--".join(["",key])
            key = " ".join(["#SBATCH",key])
            skey = "=".join([key,str(vals)])
            self.statements.append(skey)

        with open(self.outfile,"w") as fout:
            #write out the header
            fout.write(self.header)
            fout.write("\n")

            #write the essentials
            for statement in self.statements:
                fout.write(statement)
                fout.write("\n")

            #write error and output files
            fout.write(("#SBATCH -o %s\n"),self.output)
            fout.write(("#SBATCH -e %s\n"),self.error)

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
        #os.system("sbatch %s", self.script)
        cmd = ['sbatch', self.script]
        proc = sub.Popen(cmd, stdin=sub.PIPE,stdout=sub.PIPE,stderr=sub.PIPE)
        out,err = proc.communicate(input="")
        proc.wait()
        print(out)
        









