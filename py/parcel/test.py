# 打散热点key
import random
from datetime import datetime, timedelta


def modify_combination_info(combination_info):
    target_value = '[{"item_id": 26400696726, "model_id": 255876303078, "quantity": 1}]'
    if combination_info == target_value:
        random_number = str(int(random.random() * 100))
        return combination_info + '#' + random_number
    return combination_info


def rollback_combination_info(combination_info):
    if '#' in combination_info:
        return combination_info[:len(combination_info) - combination_info[::-1].index('#') - 1]
    return combination_info

if __name__ == '__main__':
    a = '[{"item_id": 26400696726, "model_id": 255876303078, "quantity": 1}]'
    for i in range(100):
        b = modify_combination_info(a)
        # print(b)
        c = rollback_combination_info(b)
        # print(c)

    today = datetime.now()
    dd = datetime.strptime('2024-11-05', '%Y-%m-%d')
    dd_ = dd - timedelta(days=90)
    print(dd_)
    last_time = today - timedelta(days=180)
    # print(today)
    # print(last_time)