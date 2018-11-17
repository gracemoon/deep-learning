from MNIST_Analysis import export
import math


# 矩阵转向量
def mat_to_vec(matrix):
    vector = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            vector.append(matrix[i][j])


# 定义数字字典
dictionary = [
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.9, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.9, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.9, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.9, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9]
]


# 准备数据,数据使用the MNIST database of handwritten digit
def load_data():
    images, old_labels = export()
    dataset = []
    new_labels = []
    for i in range(len(images)):
        dataset.append(mat_to_vec(images[i]))
    for j in range(len(old_labels)):
        new_labels.append(dictionary[int(old_labels[j])])
    return dataset, new_labels


# 权重计算
def update_weight():


# 计算误差项
def errors():



# 计算输出值
def calculate(inputs, weights_array):
    outputs = []
    neural_nodes = []
    for i in range(len(weights_array[0])):
        temp_value = 0
        for j in range(len(inputs)):
            temp_value += weights_array[0][i][j] * inputs[j]
        temp_value = 1 / (1 + math.exp(-temp_value))
        neural_nodes.append(temp_value)
    for k in range(len(weights_array[1])):
        temp_value=0
        for l in range(len(neural_nodes)):
            temp_value+=weights_array[1][k][l]*neural_nodes[l]
        outputs.append(temp_value)
    return outputs

# 反向传播算法实现
def back_propagation(m, dataset, labels):
    # 定义神经网络的层数与神经元个数
    # neural_layers = m
    # neural_nodes = [] * len(dataset[0])
    # weights=
    # 初始化权重
    weights_array = []
    weights = []
    for i in range(300):
        temp = []
        for j in range(len(dataset[0])):
            temp.append(0)
        weights.append(temp)
    weights_array.append(weights)
    temp_weight = []
    for i in range(10):
        temp = []
        for j in range(300):
            temp.append(0)
        weights.append(temp)
    weights_array.append(temp_weight)

    iteration=0
    while iteration<10:
        outputs=calculate(dataset[0],weights_array)
        
# 可视化
def visual():
