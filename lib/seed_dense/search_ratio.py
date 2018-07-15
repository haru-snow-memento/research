#!/usr/bin/env python3


import numpy as np
from itertools import zip_longest


def confirm_ranks_data(max_id, total_ars):
    cond_right = (total_ars[max_id:-1] - total_ars[(max_id + 1):]) >= 0
    if not np.min(cond_right):
        raise AssertionError("function is not decreasing monotoniously.")
    cond_left = (total_ars[0:(max_id + 1)] - total_ars[1:(max_id)]) <= 0
    if not np.min(cond_left):
        raise AssertionError("function is not increasing "
                             "monotoniously")


def get_ranks_ids(max_id, total_ars, ranks_num, ratio=1.0/2.0):
    """
    max_id is the id of a extreme value.
    """
    confirm_ranks_data(max_id, total_ars)
    threshold = total_ars[max_id] * ratio
    r_threshold = threshold
    r_ranks_ids = []
    l_threshold = threshold
    l_ranks_ids = []
    for counter, va in enumerate(total_ars[max_id:], max_id):
        if va < r_threshold:
            r_ranks_ids.append(counter)
            r_threshold = r_threshold * ratio
        else:
            continue
    reverse_counter = np.arange(max_id, -1, -1)
    for counter, va in zip(reverse_counter, l_ranks_ids):
        if va < l_threshold:
            l_ranks_ids.append(counter)
            l_threshold = l_threshold * ratio
        else:
            continue
    ranks_ids_ar = _merge_RandL_ranksids(r_ranks_ids, l_ranks_ids,
                                         max_id, ranks_num)
    return ranks_ids_ar


def _merge_RandL_ranksids(r_ranks_ids, l_ranks_ids,
                          max_id, ranks_num):
    ranks_ids = [max_id]
    for rid, lid in zip_longest(r_ranks_ids,
                                l_ranks_ids):
        if rid is not None:
            ranks_ids.append(rid)
        if lid is not None:
            ranks_ids.append(lid)
        if len(ranks_ids) >= ranks_num:
            break
        ranks_ids_ar = np.sort(ranks_ids).astype(np.int64)
    return ranks_ids_ar
