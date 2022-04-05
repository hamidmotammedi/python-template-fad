import pandas as pd
import pickle

# loed trained model

file_to_open = open("data/models/baummethoden_lr.pickle")
trained_model = pickle.load(file_to_open)

file_to_open.close()


# load data that we want predictions for

prediction_data = pd.read_csv("data/prediction-data.csv", sep=";")

print(trained_model.predict(prediction_data))
