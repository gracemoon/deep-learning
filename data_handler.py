import pandas
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import cross_val_score
file_path = 'datasets/housing.csv'


def load_data():
    return pandas.read_csv(file_path)


# 数据预处理
# 1、文本数据转化为数值数据，能更好处理
# 2、normalization（归一化）
# 3、填补缺失值（去掉该feature、去掉缺失值的数据、中位数）
def data_prepare(dataset):
    house_data = dataset.drop('median_house_value', axis=1)
    house_labels = dataset['median_house_value'].copy()
    median = house_data['total_bedrooms'].median()
    house_data = house_data.fillna(median)
    # print(house_data.info())
    house_category = house_data['ocean_proximity']
    house_category_encoded, house_categories = house_category.factorize()
    print(house_category_encoded)
    house_data['ocean_proximity'] = house_category_encoded
    return house_data, house_labels


def linear_regression(dataset, labels):
    lin_reg = LinearRegression()
    lin_reg.fit(dataset, labels)
    return lin_reg


def visual(housing):
    print(housing.head())
    print(housing.info())
    print(housing['ocean_proximity'].value_counts())
    housing.hist(bins=50, figsize=(20, 15))
    housing.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4,
                 s=housing['population'] / 100, label='population',
                 c='median_house_value', cmap=plot.get_cmap('jet'), colorbar=True
                 )
    # plot.show()
    plot.legend()
    plot.show()


def test():
    housing = load_data()
    house_data, house_labels = data_prepare(housing)
    # print(house_data.info())
    lin_reg = linear_regression(house_data, house_labels)
    # some_data = house_data.iloc[:5]
    # some_labels = house_labels.iloc[:5]
    # print('prediction:\t', lin_reg.predict(some_data))
    # print('labels:\t', list(some_labels))
    housing_predictions = lin_reg.predict(house_data)
    lin_mse = mean_squared_error(house_labels, housing_predictions)
    lin_rmse = np.sqrt(lin_mse)
    print(lin_rmse)
    print(cross_val_score(sgd_clf,x))

test()
