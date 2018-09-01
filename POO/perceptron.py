import random
class Perceptron:
    def __init__(self, input_number, step_size = 0.1):
        self._ins = input_number # n input parameters
        # Select random weights
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size # convergence rate
    def train(self, inputs, ex_outputs):
        output = self.predict(inputs)
        error = ex_outputs - output
        if error != 0:
            self._w = [w+self._eta*error*x for w, x in zip(self._w, inputs)]
        return error
    def predict(self,inputs):
        weighted_average = sum(w*elm for w,elm in zip(self._w,inputs))
        if weighted_average > 0:
            return 1
        return 0

input_data = [[1.7,56,1],[1.72,63,0],[1.6,50,1],[1.7,63,0],[1.74,66,0],[1.58,55,1],[1.83,80,0],[1.82,70,0],[1.65,54,1]]
pr = Perceptron(3)
for _ in range(100):
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1]
        err = pr.train(inp, output)

h = float(input("Enter your height-> "))
w = float(input("Enter your weight-> "))
if pr.predict([1,h,w]) == 1: print "Mujer"
else: print "Hombre"
