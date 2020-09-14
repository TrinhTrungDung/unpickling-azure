import pickle
import os


class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        renamed_module = module
        if module == "model":
            renamed_module = "__app__.TestPickle.model"
        return super(CustomUnpickler, self).find_class(renamed_module, name)


class Suggester:
    def __init__(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        self.model = CustomUnpickler(open(f"{directory}/model.pkl", "rb")).load()

    def suggest(self, x):
        return self.model.predict(x)
