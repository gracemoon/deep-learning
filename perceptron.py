# 准备数据
def load_data():
    matrix = [[0, 0],
              [0, 1],

              [1, 1],
              [1, 0]
              ]
    labels = [0, 0, 1, 0]
    return matrix, labels


# 更新权重和偏差
def update(weights, bias, ratio, error, x):
    for i in range(len(weights)):
        weights[i] += x[i] * ratio * error
    bias += ratio * error
    return weights, bias


# 激活函数
def sigmoid(weights, bias, x):
    y = 0
    for i in range(len(weights)):
        y += weights[i] * x[i]
    y += bias
    if y > 0:
        y = 1
    else:
        y = 0
    return y


# perceptron algorithm
def perceptron(dataset, labels):
    flag = 1
    weights = [0] * len(dataset[0])
    bias = 0
    result = [0] * len(labels)
    error = [0] * len(labels)
    while flag:
        # 对每个x都计算result,如果result跟labels一致，则迭代成功，退出。否则修改权重与偏差
        for i in range(len(dataset)):
            result[i] = sigmoid(weights, bias, dataset[i])
            error[i] = labels[i] - result[i]
        temp = 0
        for j in range(len(error)):
            temp += error[j]
        if temp == 0:
            break
        else:
            for k in range(len(dataset)):
                weights, bias = update(weights, bias, 0.1, error[k], dataset[k])

    return weights, bias


g_dataset, g_labels = load_data()
g_weights, g_bias = perceptron(g_dataset, g_labels)


print(g_weights)
print(g_bias)


def test(dataset, weights, bias):
    for i in range(len(dataset)):
        print(sigmoid(weights, bias, dataset[i]))


test(g_dataset, g_weights, g_bias)
