import matplotlib.pyplot as plot


# 可视化
def data_visual(dataset):
    x = []
    y = []
    for i in range(len(dataset)):
        x.append(dataset[i][0])
        y.append(dataset[i][1])
    # plot.figure()
    # plot.plot(x, y)
    plot.scatter(x, y)
    plot.show()


# 准备数据
def load_data():
    dataset = [
        [1, 0.8],
        [2, 2.3],
        [3, 3.3],
        [4, 3.7],
        [5, 4.3],
        [6, 6.6],
        [7, 7.5],
        [8, 7.1],
        [9, 9.0],
        [10, 11],
    ]
    return dataset


data_visual(load_data())
