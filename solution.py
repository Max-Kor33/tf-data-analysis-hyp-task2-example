import pandas as pd
import numpy as np
from hippo.ksample import MMD


chat_id = 957195795 # Ваш chat ID, не меняйте название переменной

def solution(x, y):
    ## Используем MMD
    res = MMD(compute_kernel='rbf', gamma=1.0).test(x, y)
    if res[1] < 0.03:
        bool_final = True
    else:
        bool_final = False
    return bool_final
