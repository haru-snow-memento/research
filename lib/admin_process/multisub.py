#!/usr/bin/env python3


import subprocess
from subprocess import Popen
import os


ENV = os.environ.copy()


def endless_counter(start=0):
    while True:
        yield start
        start += 1


def endless_fobcounter(dir_path, head="tmp_"):
    if not os.path.isdir(dir_path):
        raise OSError("unknown dir path")
    for num in endless_counter():
        fpath = os.path.join(dir_path, head + num)
        yield open(fpath, "r")


def endless_popen_pipe_gene():
    while True:
        yield subprocess.PIPE


def endless_yiled_none():
    while True:
        yield None


class MultiSubP(object):
    def __init__(self, fpath, set_read=True):
        self.read = open(fpath, "r")
        self.input_pipe_gene = None
        self.output_pipe_gene = None
        if set_read:
            self._set_read()

    def remove_output_pipe(self):
        self.trush_outpipe = True

    def _set_read(self):
        self.read = [line.strip() for line in self.read]
        self.total_proc_num = len(self.read)

    def set_output_fpipe(self, out_dir):
        self.output_pipe_gene = endless_fobcounter(out_dir)

    def gene_procs(self):
        if self.input_pipe_gene is None:
            self.input_pipe_gene = endless_popen_pipe_gene()
        if self.output_pipe_gene is None:
            self.output_pipe_gene = endless_popen_pipe_gene()
        if self.trush_outpipe:
            self.output_pipe_gene = endless_yiled_none()
        self.base_gene = zip(self.read,
                             self.input_pipe_gene,
                             self.output_pipe_gene)
        for one_line, input_pipe, out_pipe in self.base_gene:
            cmd = one_line
            proc = Popen(cmd, shell=True, env=ENV,
                         stdin=subprocess.PIPE, stdout=out_pipe)
            yield proc

    def add_input_to_proc_gene(self, add_input=b"a"):
        for proc in self.gene_procs():
            proc.stdin.write(add_input)
            yield proc
