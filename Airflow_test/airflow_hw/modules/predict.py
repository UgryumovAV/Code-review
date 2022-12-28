import dill
import pandas as pd
import os
from datetime import datetime
import json

path = os.environ.get('PROJECT_PATH', '..')


def predict():
    def loan_model():
        model_filename_list = os.listdir(f'{path}/data/models')
        model_path = f'{path}/data/models/{model_filename_list[-1]}'

        with open(model_path, 'rb') as file:
            cars_pipe = dill.load(file)

        return cars_pipe

    test_names_list = os.listdir(f'{path}/data/test')
    dict_pred = {}
    model = loan_model()

    for test_name in test_names_list:
        with open(f'{path}/data/test/{str(test_name)}') as train_file:
            json_train = json.load(train_file)
            data_predict = pd.DataFrame.from_dict([json_train])
            y = model.predict(data_predict)
            dict_pred[test_name] = y[0]

    df_pred = pd.DataFrame(list(dict_pred.items()), columns=['name', 'prediction'])
    df_pred.to_csv(f'{path}/data/predictions/cars_pipe_{datetime.now().strftime("%Y%m%d%H%M")}.csv', sep='\t')

    pass

if __name__ == '__main__':
    predict()
