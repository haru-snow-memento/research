#!/usr/bin/env python3

import time


class VirtualProcess(object):
    def __init__(self, std_exit=0):
        self.std_exit = std_exit

    def poll(self):
        return self.std_exit


class ProcessManager(object):
    def __init__(self, max_process_num, process_itr):
        self.max_process_num = max_process_num
        self.working_process_list = [VirtualProcess()] * max_process_num
        self.future_process_itr = process_itr

    def gene_cond_of_stdexit(self):
        std_exits_itr = (proc.poll() for proc in self.working_process_list)
        return std_exits_itr

    def confirm_end_of_total_process(self, wait_time=10):
        time.sleep(wait_time)
        while True:
            tmp = [cond for cond in self.gene_cond_of_stdexit()
                   if (cond is not None) and (cond == 0)]
            if len(tmp) == self.max_process_num:
                break
        print("total processes are finished.")

    def run(self, wait_time=10):
        while True:
            time.sleep(wait_time)
            for plinum, exit_cond in enumerate(self.gene_confirm_stdexit()):
                if exit_cond == 0:
                    try:
                        # hook function is written here.
                        working_proc = next(self.process_iter)
                        self.working_process_list[plinum] = working_proc
                    except StopIteration:
                        break
            else:
                continue
            break
        self.confirm_end_of_total_process()
