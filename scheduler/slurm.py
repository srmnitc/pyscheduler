"""
A small scheduler script for submission of jobs.

"""
import os

class slurm(object):
    def __init__(outfile):
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

    def submit():
        """
        Submit job
        """



def write_script(scheduler):
    """
    Write out the script
    """

    #prep the essentials
    dictcopy = scheduler.essentials
    statements = []

    for key, vals in dictcopy.iteritems():
        key = "--".join(,key)
        key = " ".join("#SBATCH",key)
        skey = "=".join(key,vals)
        statements.append(skey)



    with open(scheduler.outfile,"w") as fout:
        #write out the header
        fout.write(self.header)
        fout.write("\n")
        
        #write the essentials
        





