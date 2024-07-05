import numpy as np
from numpy import random as rand


def taste_based_predictions(positions: list, ratings: list):
    for i in range(0, positions.__len__()):
        if (ratings[i] >= 4):
            t = positions[i]
            print("Al usuario ",t[0]," le recomendamos la película ", t[1])
        else:
            t = positions[i]
            print("Al usuario ",t[0]," no le debe gustar la película ", t[1])


def prediction_matrix(matrix: list[list], ratings: list, positions: list):
    for i in range(0, ratings.__len__()):
        t = positions[i]
        matrix[t[0], t[1]] = ratings[i]
    return matrix


def comparition_system(value):
    if (value > 0.5):
        return 5
    elif (value > 0.1):
        return 4
    elif (value > -0.3):
        return 3
    elif (value > -0.7):
        return 2
    elif (-0.7 > value):
        return 1


def convert_values_to_ratings(values: list):
    ratgs = []
    for i in range(0, values.__len__()):
        ratgs.append(comparition_system(values[i]))
    return ratgs



# This method replaces values ​​that are zero with the average ratings for each item
# Este método sustituye los valores que son cero por el promedio de ratings para cada item
def arrange_matrix(matrix: list[list], positions_to_predict: list):
    for r in range(matrix.__len__()):
        for c in range(matrix[r].__len__()):
            if (matrix[r][c] == 0):
                mean_value = mean_movie_clasification_value(matrix, c)
                matrix[r][c] = mean_value
                positions_to_predict.append((r, c))


def mean_movie_clasification_value(matrix: list[list], column):
    sum = 0
    cant_rows = matrix.__len__()
    div = cant_rows
    for i in range(cant_rows):
        current_element = matrix[i][column]
        if current_element != 0:
            sum += current_element
        elif div >= 2:
            div -= 1
    sum = sum/div
    return sum

# This method generates a random matrix to test, values ​​equal to zero mean that user has not rated the article
# Este método genera una matriz aleatoria para probar, los valores iguales a cero significan que ese usuario no a puntuado el item
def random_rating_matrix(size):
    x = rand.randint(5, size)
    y = rand.randint(5, size)
    return rand.randint(6, size=(x, y))


def truncar_matriz_columns(matrix: list[list], new_dimension):
    truncada = []
    for i in range(new_dimension):
        truncada.append(matrix[:, i])
    truncada = np.array(truncada)
    return truncada.T


def truncar_matriz_rows(matrix: list[list], new_dimension):
    truncada = []
    for i in range(new_dimension):
        truncada.append(matrix[i])
    truncada = np.array(truncada)
    return truncada.T


def cant_caract(values):
    for e in range(values.__len__()):
        if values[e] < 2:
            return e
    return values.__len__()

# This method reduces the matrices to the most significant values
# Este metodo reduce las matrices a los valores mas significativos
def truncar_matrices(u, v, s):
    caract = cant_caract(s)
    u = truncar_matriz_columns(u, caract)
    v = truncar_matriz_rows(v, caract)
    s = s[:caract]
    return u, v, s

# This method calculates the cosine distances of the elements that do not have a rating
# Este metodo calcula las distancias del coseno de los elmentos que no tienen rating
def get_cosenos(u: np.array, v: np.array, positions_to_predict):
    cosenos = []
    for t in positions_to_predict:
        user = (u[t[0]])
        item = (v[t[1]])
        cosenos.append((np.dot(user, item)))
    return cosenos


# This is the entry matrix, the zero values means there is no rating
rating_matrix = random_rating_matrix(10)

# Printing results to check
print("MATRIZ ORIGINAL")
print(rating_matrix)

# This method changes the no_rated positions for the mean_value of that movies ratings
positions_to_predict = []
arrange_matrix(rating_matrix, positions_to_predict)

u, s, v = np.linalg.svd(rating_matrix)  # SVD Descomposition
u, v, s = truncar_matrices(u, v, s) # Truncating the matrices to keep the significant values / Truncando las matrices para quedarme con los valores significativos
cosenos = get_cosenos(u, v, positions_to_predict) # Finding the distances of the cosines /  Hallando las distancias de los cosenos 

print("RATINGS")
rating_array = convert_values_to_ratings(cosenos)
print(rating_array)

print("DEFINITIVE MATRIX")
print(prediction_matrix(rating_matrix, rating_array, positions_to_predict))
print(taste_based_predictions(positions_to_predict,rating_array))