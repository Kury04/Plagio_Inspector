import re
import math
from nltk.corpus import stopwords

def findFileSimilarity(inputQuery, database):
    universalSetOfUniqueWords = []
    matchPercentage = 0

    lowercaseQuery = inputQuery.lower()
    en_stops = set(stopwords.words('english'))

    # Reemplazar la puntuación por espacios y dividir
    queryWordList = re.sub(r"[^\w]", " ", lowercaseQuery).split()

    # Elimina stopwords del query
    queryWordList = [word for word in queryWordList if word not in en_stops]

    # Si la lista está vacía después de eliminar stopwords
    if not queryWordList:
        return 0

    for word in queryWordList:
        if word not in universalSetOfUniqueWords:
            universalSetOfUniqueWords.append(word)

    database1 = database.lower()

    # Reemplazar la puntuación por espacios y dividir
    databaseWordList = re.sub(r"[^\w]", " ", database1).split()

    # Elimina stopwords de la base de datos
    databaseWordList = [word for word in databaseWordList if word not in en_stops]

    # Si la lista está vacía después de eliminar stopwords
    if not databaseWordList:
        return 0

    for word in databaseWordList:
        if word not in universalSetOfUniqueWords:
            universalSetOfUniqueWords.append(word)

    queryTF = []
    databaseTF = []

    for word in universalSetOfUniqueWords:
        queryTfCounter = queryWordList.count(word)
        queryTF.append(queryTfCounter)

        databaseTfCounter = databaseWordList.count(word)
        databaseTF.append(databaseTfCounter)

    dotProduct = sum([queryTF[i] * databaseTF[i] for i in range(len(queryTF))])

    queryVectorMagnitude = math.sqrt(sum([tf**2 for tf in queryTF]))
    databaseVectorMagnitude = math.sqrt(sum([tf**2 for tf in databaseTF]))

    # Verifica si alguno de los vectores tiene magnitud cero
    if queryVectorMagnitude == 0 or databaseVectorMagnitude == 0:
        return 0  # No se puede dividir por cero, retorna 0% de similitud

    matchPercentage = (dotProduct / (queryVectorMagnitude * databaseVectorMagnitude)) * 100

    return matchPercentage
