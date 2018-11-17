# coding=UTF-8
import numpy as np
import struct
import matplotlib.pyplot as plt


def parese_idx3(idx3_file):
    """
    idx3文件解析方法
    :param idx3_file: idx3文件路径
    :return: 数据集
    """
    # 读取二进制数据
    bin_data = open(idx3_file, 'rb').read()

    # 解析文件头信息 magic、imgs、height、width
    # '>IIII'是说使用大端法读取4个unsinged int32
    offset = 0
    fmt_header = '>iiii'
    magic, imgs, height, width = struct.unpack_from(fmt_header, bin_data, offset)
    print('magic:%d, imgs: %d, heightXwidth: %dX%d' % (magic, imgs, height, width))

    # 解析数据集
    image_size = height * width
    offset += struct.calcsize(fmt_header)
    fmt_image = '>' + str(image_size) + 'B'
    images = np.empty((imgs, height, width))
    for i in range(imgs):
        if (i + 1) % 10000 == 0:
            print('已解析 %d' % (i + 1) + '张')
        images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((height, width))
        offset += struct.calcsize(fmt_image)
    return images


def parese_idx1(idx1_file):
    """
    idx1文件解析方法
    :param idx1_file: idx1文件路径
    :return: 数据集
    """
    # 读取二进制数据
    bin_data = open(idx1_file, 'rb').read()

    # 解析文件头信息 magic、imgs
    offset = 0
    fmt_header = '>ii'
    magic, imgs = struct.unpack_from(fmt_header, bin_data, offset)
    print('magic:%d, imgs: %d' % (magic, imgs))

    # 解析数据集
    offset += struct.calcsize(fmt_header)
    fmt_image = '>B'
    labels = np.empty(imgs)
    for i in range(imgs):
        if (i + 1) % 10000 == 0:
            print('已解析 %d' % (i + 1) + '张')
        labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
        offset += struct.calcsize(fmt_image)
    return labels


def export():
    imgs = parese_idx3("D:\Download\\train-images-idx3-ubyte\\train-images.idx3-ubyte")
    labs = parese_idx1("D:\Download\\train-labels-idx1-ubyte\\train-labels.idx1-ubyte")
    return imgs, labs


imgs, labs = export()
# print(imgs[0])
print(labs[2])