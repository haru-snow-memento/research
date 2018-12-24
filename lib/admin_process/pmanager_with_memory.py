#!/usr/bin/env/python3

# formal lib
import psutil
import os
import subprocess
from psutil import NoSuchProcess
from subprocess import Popen
# my lib
from pmanager import ProcessManager

class ProcessManagerMofified(ProcessManager):
    def __init__(self):
        pass

    def set_max_physical_memory(self, max_usage=0.25)
        self.max_usage_of_memory = max_usage

    def gene_check_process_usage(self):
        for plnum, proc in enumerate(self.working_process_list):
            util_process = psutil.Process(proc.id)
            util_process.memory_percent()
