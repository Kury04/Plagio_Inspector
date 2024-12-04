
from nltk.corpus import stopwords
from plagiarismchecker.algorithm import webSearch
import sys
import re

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def getQueries(text, n):
    sentenceEnders = re.compile("['.!?]")
    sentenceList = sentenceEnders.split(text)
    sentencesplits = []
    en_stops = set(stopwords.words('english'))

    for sentence in sentenceList:
        x = re.compile(r'\W+', re.UNICODE).split(sentence)
        for word in x:
            if word.lower() in en_stops:
                x.remove(word)
        x = [ele for ele in x if ele != '']
        sentencesplits.append(x)
    finalq = []
    for sentence in sentencesplits:
        l = len(sentence)
        if l > n:
            l = int(l/n)
            index = 0
            for i in range(0, l):
                finalq.append(sentence[index:index+n])
                index = index + n-1
                if index+n > l:
                    index = l-n-1
            if index != len(sentence):
                finalq.append(sentence[len(sentence)-index:len(sentence)])
        else:
            if l > 4:
                finalq.append(sentence)
    return finalq


def findSimilarity(text):

    # Seleccionar un párrafo del texto (opcional: primer párrafo no vacío)
    parrafos = [p.strip() for p in text.split('\n') if p.strip()]
    parrafo_seleccionado = parrafos[0] if parrafos else "No se encontró texto para mostrar."

    # n-grams N VALUE SET HERE
    n = 9
    queries = getQueries(text, n)
    print('GetQueries task complete')
    
    # Crear una lista de consultas válidas (sin elementos vacíos)
    q = [' '.join(d) for d in queries if d]  
    numqueries = min(len(q), 100)  # Limita las consultas a un máximo de 100

    output = {}
    c = {}
    textos_plagiados = []  # Lista para almacenar los fragmentos plagiados
    coincidencias = []  # Para almacenar texto plagiado con su URL
    posiciones_texto_plagiado = []  # Para almacenar las posiciones del texto plagiado

    for s in textos_plagiados:
        for link, count in c.items():
            if count > 0:
                coincidencias.append({'texto': s.strip(), 'url': link})

    for s in q[:numqueries]:  # Usa numqueries como límite
        output, c, errorCount = webSearch.searchWeb(s, output, c)
        if errorCount == 0:  # Si no hubo error en la búsqueda
            for link, count in c.items():
                if count > 0:  # Si el enlace tiene resultados
                    textos_plagiados.append(s)  # Agrega el fragmento que coincide
                    start_index = text.find(s)  # Encuentra la posición del texto plagiado
                    if start_index != -1:
                        posiciones_texto_plagiado.append((start_index, start_index + len(s)))

    totalPercent = 0
    outputLink = {}
    prevlink = ''

    for link in output:
        if numqueries > 0:
            percentage = (output[link] * c[link] * 100) / numqueries
        else:
            percentage = 0

        if percentage > 10:
            totalPercent += percentage
            prevlink = link
            outputLink[link] = percentage
        elif len(prevlink) != 0:
            totalPercent += percentage
            outputLink[prevlink] += percentage
        elif c[link] == 1:
            totalPercent += percentage

    print(f"Total Porcentaje: {totalPercent}")
    print(f"Enlaces con porcentaje: {outputLink}")
    print("\nProceso terminado.")

    return totalPercent, outputLink, textos_plagiados, coincidencias, posiciones_texto_plagiado 

def findSimilarity2(text1, text2):
    # Lógica para calcular el porcentaje de similitud
    from difflib import SequenceMatcher

    # Comparar los textos y calcular similitud
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    similarity_percentage = similarity_ratio * 100

    # Retornar el porcentaje y, opcionalmente, las fuentes analizadas
    return similarity_percentage, []


