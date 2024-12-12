import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

def graph( data, title):
    ax = sns.boxplot(x="hour", y='lead_time', data=data)
    # hours = list(range(24))
    # ax.set_xticklabels(hours)
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(1))  # 设置刻度间隔为 1
    # plt.title(title)
    # 使用 IndexLocator 和 IndexFormatter 确保刻度和标签对应
    # ax.xaxis.set_major_locator(ticker.IndexLocator(base=1, offset=0))
    # ax.xaxis.set_major_formatter(ticker.IndexFormatter(values=list(range(24))))
    # 设置 X 轴刻度为 0 到 23，间隔为 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xticks(np.arange(24))
    ax.set_xticklabels(np.arange(24))
    # 设置刻度间隔为 1，并使用自定义的刻度标签格式化函数
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    # def format_func(value, tick_number):
    #     if value < 24:
    #         return str(int(value))
    #     else:
    #         return ''
    # ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_func))

    plt.xticks(rotation=45)  # 旋转刻度标签 45 度
    plt.title(title)



if __name__ == '__main__':
    # Reading the CSV file
    df = pd.read_csv("/Users/shengwang/Downloads/edge_lead_time.csv")
    df.describe()

    # Printing top 5 rows
    df.head()

    filtered_df = df[df['end_point'] == 'soc_4']
    filtered_df = filtered_df[filtered_df['start_point'] == 'shop_1195230934']

    monday_df = filtered_df[filtered_df['week'] == 'Monday']
    tuesday_df = filtered_df[filtered_df['week'] == 'Tuesday']
    wednesday_df = filtered_df[filtered_df['week'] == 'Wednesday']
    thursday_df = filtered_df[filtered_df['week'] == 'Thursday']
    friday_df = filtered_df[filtered_df['week'] == 'Friday']
    saturday_df = filtered_df[filtered_df['week'] == 'Saturday']
    sunday_df = filtered_df[filtered_df['week'] == 'Sunday']

    # plt.figure(figsize=(24, 20))
    #
    # # Adding the subplot at the specified
    # # grid position
    # plt.subplot(421)
    # graph( monday_df, 'Monday')
    #
    # plt.subplot(422)
    # graph( tuesday_df, 'Tuesday')
    #
    # plt.subplot(423)
    # graph( wednesday_df, 'Wednesday')
    #
    # plt.subplot(424)
    # graph( thursday_df, 'Thursday')
    #
    # plt.subplot(425)
    # graph( friday_df, 'Friday')
    #
    # plt.subplot(426)
    # graph( saturday_df, 'Saturday')
    #
    # plt.subplot(427)
    # graph( sunday_df, 'Sunday')
    #
    # plt.tight_layout()
    # plt.show()

    # 周一到周日分别绘制箱线图
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    fig, axes = plt.subplots(7, 1, figsize=(10, 20))

    filtered_df.describe()

    for i, day in enumerate(days):
        day_data = filtered_df[filtered_df['week'] == day]
        sns.boxplot(x='hour', y='lead_time', data=day_data, ax=axes[i], showfliers=True)
        axes[i].set_title(day)
        axes[i].set_xlabel('Hour')
        axes[i].set_ylabel('Lead Time')
        axes[i].xaxis.set_major_locator(ticker.MultipleLocator(1))
        axes[i].set_xticks(np.arange(24))
        axes[i].set_xticklabels(np.arange(24))

    plt.tight_layout()
    plt.show()
