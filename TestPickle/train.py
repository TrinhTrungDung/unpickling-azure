import os
import pickle

from model import Model


if __name__ == "__main__":
    x_train = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    m = Model()
    m.fit(x_train)

    directory = os.path.dirname(os.path.realpath(__file__))

    pickle.dump(m, open(f"{directory}/model.pkl", "wb"))