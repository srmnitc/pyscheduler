"""
A small scheduler script for submission of jobs.

"""
import os

class slurm(object):
    def __init__(self, outfile):
        self.outfile = outfile
        self.initialized = True
        self.header = "#!/bin/bash"
        self.essential = {
            "job-name" : "pyschedule",
            "time" : "1:59:00",
            "ntasks" : 4,
            "mem-per-cpu" : "3GB",
            "hint" : "no-multithread"        
        }

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

    def submit(self):
        """
        Submit job
        """
        a = 1









