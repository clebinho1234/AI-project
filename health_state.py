import numpy as np

x_train = np.array([[25, 180, 80, 8],               # The array structure is: Age, Height, Weight and Sleep time
                    [39, 170, 99, 5],
                    [82, 157, 60, 9],
                    [42, 172, 74, 6],
                    [31, 158, 60, 7],
                    [56, 164, 83, 4],
                    [72, 171, 70, 8],
                    [18, 190, 93, 6],
                    [21, 187, 87, 7],
                    [64, 161, 64, 7],
                    [46, 151, 80, 9],
                    [50, 142, 65, 4],
                    [44, 174, 60, 4],
                    [31, 185, 100, 8],
                    [22, 168, 72, 8],
                    ])
y_health_states = np.array(['Healthy', 'Not Heatlhy', 'Healthy', 'Healthy', 'Healthy',               # It only have two health states: Healthy
                            'Not Heatlhy', 'Healthy', 'Healthy', 'Healthy', 'Heatlhy',               # or Not Healthy, but it´s possible to put
                            'Not Healthy', 'Not Healthy', 'Not Healthy', 'Not Heatlhy', 'Healthy'])  # more states, for exemple, sedentary if we add activity time to the data.

x_test = np.array([[23, 180, 100, 7], [39, 185, 86, 7], [44, 162, 70, 7], [72, 171, 90, 5]])  # test data
x_health_states = []  # It should give in the end: ['Not Healthy', 'Healthy', 'Healthy', 'Not Healthy']

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
