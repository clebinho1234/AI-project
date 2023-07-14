import numpy as np

x_train = np.array([[25, 180, 80, 8],               # The array structure is: Age, Height, Weight and Sleep time
                    [39, 170, 99, 5],
                    [82, 157, 60, 9],
                    [42, 172, 74, 6],
                    [25, 180, 820, 8],
                    [39, 170, 99, 5],
                    [82, 157, 60, 9],
                    [42, 172, 74, 6],
                    [25, 180, 820, 8],
                    [39, 170, 99, 5],
                    [82, 157, 60, 9],
                    [42, 172, 74, 6]
                    ])
y_health_states = np.array(['Healthy', 'Not Heatlhy', 'Healthy', 'Healthy'])   # It only have two health states: Healthy
                                                                               # or Not Healthy, but it´s possible to put
                                                                               # more states, for exemple, sedentary if we add activity time to the data.

x_test = np.array([[23, 180, 100, 7], [39, 185, 86, 7], [39, 185, 86, 7], [39, 185, 86, 7]])
x_health_states = []

def dist(test_item, train_item):
    return np.sqrt(np.sum((test_item - train_item) ** 2))

if __name__ == "__main__":
    n_train = len(x_train)

    for test_item in x_test:
        d = np.empty(n_train)
        for i, train_item in enumerate(x_train):
            d[i] = dist(test_item, train_item)
        nearest_index = np.argmin(d)
        health_state = y_health_states[nearest_index]
        x_health_states.append(health_state)

    print(x_health_states)
