from sklearn import tree
import json


class DecisionTree:

    X = []
    Y = []
    clf = 0

    def __init__(self):
        self.clf = tree.DecisionTreeClassifier()

    def read_data_from_file(self):
        with open('learning_data.txt', 'rb') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                result = self.process_line(line)

                self.Y.append(result[0][0])
                self.X.append(result[1])
        f.close()

    def process_line(self, line):
        line = line.rstrip().decode('utf-8')
        params = line.split(" ", 1)
        params[0] = json.loads(params[0])
        params[1] = json.loads(params[1])
        return params

    def learn_tree(self):

        self.read_data_from_file()
        self.clf = self.clf.fit(self.X, self.Y)

    def predict_result(self, square):
        return self.clf.predict([square])
