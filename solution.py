import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 957195795 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p_value = ks_2samp(x, y)
    if p_value < 0.05:
        res = False # отвергаем H0
    else:
        res = True
    return res # Ваш ответ, True или False
