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
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [1, 6],
        [1, 7],
        [1, 8],
        [1, 9],
        [1, 10]
    ]
    labels = [
        0.8,
        2.3,
        3.3,
        3.7,
        4.3,
        6.6,
        7.5,
        7.1,
        9.0,
        11
    ]
    return dataset, labels


# 计算回归值和错误率
def calculate(dataset, weights):
    temp_labels = [0] * len(dataset)
    for i in range(len(dataset)):
        temp_value = 0
        for j in range(len(dataset[i])):
            temp_value += dataset[i][j] * weights[j]
        temp_labels[i] = temp_value
    return temp_labels


# 更新权重
def update_weights(labels, temp_labels, ratio, weights, dataset):
    new_weights = [0] * len(weights)

    for i in range(len(weights)):
        temp_value = 0
        for j in range(len(dataset)):
            temp_value += (labels[j] - temp_labels[j]) * dataset[j][i]
        new_weights[i] = weights[i] - ratio * temp_value
    return new_weights


# 线性回归
def linear_regression(dataset, labels):
    # 初始化权重，b项为W0
    weights = [0] * len(dataset[0])
    error = [0] * len(dataset[0])
    # 定义学习率
    ratio = 0.01
    # 定义容错度
    error_ratio = 0.01
    while 1:
        temp_labels = calculate(dataset, weights)
        for i in range(len(error)):
            error[i] = labels[i] - temp_labels[i]
        flag = 0
        for j in range(len(error)):
            if error[j] < error_ratio:
                flag += 1
        if flag == len(labels):
            break
        else:
            weights = update_weights(labels, temp_labels, ratio, weights, dataset)
    return weights


g_dataset, g_labels = load_data()
g_weights = linear_regression(g_dataset, g_labels)
print(g_weights)
