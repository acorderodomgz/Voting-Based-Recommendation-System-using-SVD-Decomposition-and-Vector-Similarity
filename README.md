Code summary:
The project begins with a matrix that represents the ratings by a number n of users of a number m of items.

We take a randomly generated matrix, although this is not a case that happens in reality, and decompose it into singular values.

Then we truncate it to eliminate terms of little importance, as is usually the way to proceed in the application of the SVD (in real life a good approximation can be 30 eigenvalues).

And then by calculating the cosine distance we can find out how similar the user and the item are and make a prediction of the rating they would give it.



Resumen del código:
El proyecto parte de que tenemos una matriz que representa las calificaciones por una cantidad n de usuarios de una cantidad m de items.

Tomamos una matriz generada aleatoriamente, aunque este no es un caso que suceda en la realidad, y la descompones en valores singulares.

Luego la truncamos para eliminar términos de poca importancia como suele ser la forma de proceder en la aplicación del SVD (en la vida real una buena aproximación puede ser 30 valores propios).

Y luego calculando la distancia del coseno podemos hallar cuánto se parecen el usuario y el item y realizar una predicción de la calificación que le daría
