import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
std = StandardScaler()

data_path = 'concrete.csv'

def model_dev(data_dir):
    data = pd.read_csv(data_dir)
    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]
    scaled_X = std.fit_transform(X)
    model = GradientBoostingRegressor(learning_rate= 0.1, max_depth= 4, max_features= 1.0, min_samples_leaf= 3, n_estimators= 500)
    model.fit(scaled_X, y)
    pickle.dump(model, open('artifacts\prediction_model.pkl','wb'))
    print('>> Model Created')

if __name__ == '__main__':
    model_dev(data_path)

