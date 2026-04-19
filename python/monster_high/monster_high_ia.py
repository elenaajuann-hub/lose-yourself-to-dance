from sklearn.neighbors import KNeighborsClassifier

# 1. Data (Monster High's Attributes) // Atributos de las Monster High
X = [
    [2, 2, 2, 2], [2, 1, 2, 2],               # Frankie
    [1, 1, 1, 1], [1, 2, 1, 1], [1, 3, 1, 1], # Draculaura
    [3, 3, 3, 3], [3, 2, 3, 3]                # Clawdeen
]

# 2. Labels // Etiquetas
y = ["Frankie", "Frankie", "Draculaura", "Draculaura", "Draculaura", "Clawdeen", "Clawdeen"]

# 3. We set the algorithm to use
"Usamos este algoritmo ya que es el más simple y el que menos datos necesita para hacer una predicción, definimos K que es el numero de vecinos que tiene que visitar antes de decidir"
model = KNeighborsClassifier(n_neighbors=3)

# 4. We train the model
model.fit(X,y)
print("Ya está cargado el modelo")

# 5. We ask for information to the user
print("\n--- Introduce los datos\n")
pelo = int(input("Pelo (1:Rosa, 2:Blanco, 3:Marrón): "))
paleta = int(input("Paleta (1:Rosa, 2:Blanco/Negro/Azul, 3:Morado): "))
piel = int(input("Piel (1:Rosa, 2:Verde, 3:Marrón): "))
marca = int(input("Marca (1:Corazón, 2:Costura, 3:Lobo): "))

# 6. We create a matrix with the attributes
test_personaje = [[pelo, paleta, piel, marca]]

# 7. Now we make the prediction
prediccion = model.predict(test_personaje)

print("\n")
print(f"El makina piensa que es...¡{prediccion[0].upper()}!")

