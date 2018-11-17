import numpy as np
# 准备数据,数据使用the MNIST database of handwritten digit
def load_data():
    import struct
    for file in ['gemfield_data/t10k-labels-idx1-ubyte', 'gemfield_data/train-labels-idx1-ubyte']:
        data = open(file, 'rb').read()
        # fmt of struct unpack, > means big endian, i means integer, well, ii mean 2 integers
        fmt = '>ii'
        offset = 0
        magic_number, label_number = struct.unpack_from(fmt, data, offset)
        print('magic number is {} and label number is {}'.format(magic_number, label_number))
        # slide over the 2 numbers above
        offset += struct.calcsize(fmt)
        # B means unsigned char
        fmt = '>B'
        labels = np.empty(label_number)
        for i in range(label_number):
            labels[i] = struct.unpack_from(fmt, data, offset)[0]
            offset += struct.calcsize(fmt)
        print(labels)

# 权重计算
def update_weight():

# 反向传播算法实现
def back_propagation():


# 可视化
def visual():