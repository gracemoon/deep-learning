from MNIST_Analysis import export


# 矩阵转向量
def mat_to_vec(matrix):
    vector = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            vector.append(matrix[i][j])

# 准备数据,数据使用the MNIST database of handwritten digit
def load_data():
    images, labels = export()
    dataset=[]
    for i in range(0,100):
        dataset.append(mat_to_vec(images[i]))
    return dataset, labels[0:100]


# 权重计算
def update_weight():


# 反向传播算法实现
def back_propagation():


# 可视化
def visual():
