from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import numpy as np

def make_prediction(df):

    features = PolynomialFeatures(degree=2)

    df['Days'] = generate_x(df)
    x = df['Days']
    y = df['Victims']

    # Reshape x so I can transform features
    x = np.array(x).reshape(-1,1)

    X = features.fit_transform(x)

    poly_model = LinearRegression()

    poly_model.fit(X,y)

    print("The model explains {:.2f}% of the accidents.".format(poly_model.score(X,y)*100))



'''
Since the x values are strings, I use numbers 0,1,2 as a way to distinguish them numerically. 
'''
def generate_x(df):
    x = []
    days = df['Part of the day']
    for i in days:
        if i == 'Morning':
            x.append(0)
        elif i == 'Afternoon':
            x.append(1)
        else:
            x.append(2)
    return x

