import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np




if __name__ == '__main__':
    # Reading the CSV file
    order_plan_path = pd.read_csv("/Users/shengwang/Downloads/order_plan_path.csv")
    order_tracking = pd.read_csv("/Users/shengwang/Downloads/order_tracking.csv")

    sorted_df = order_tracking.sort_values(by=['shipment_id', 'ctime']).groupby('shipment_id').apply(lambda x: x)

    # 打印前几个 shipment_id 的部分结果
    for shipment_id, group in sorted_df.head(3).groupby('shipment_id'):
        print(f"Shipment ID: {shipment_id}")
        print(group.head())
        print("\n")


    # merged_df = order_tracking.merge(order_plan_path, left_on='shipment_id', right_on='shipment_id', how='left',
    #                                  suffixes=('', '_tracking'))
