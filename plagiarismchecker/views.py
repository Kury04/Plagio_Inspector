from django.shortcuts import render, redirect
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
from docx import Document
from plagiarismchecker.algorithm import fileSimilarity
import PyPDF2

# Función de login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Aquí deberías incluir la lógica de autenticación
        if username == 'admin' and password == 'password':
            # Si el login es exitoso, redirigir al usuario al index
            return redirect('pc/index.html')
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            return render(request, 'pc/login.html', {'error': 'Credenciales incorrectas'})

    # Si la petición no es de tipo POST, renderizar el formulario de login
    return render(request, 'pc/login.html')

# Home
def home(request):
    return render(request, 'pc/index.html')

# Web search (Text)
def test(request):
    print("request is welcome test")
    print(request.POST['q'])  
    
    if request.POST['q']: 
        percent, link = main.findSimilarity(request.POST['q'])
        percent = round(percent, 2)
    print("Output.....................!!!!!!!!", percent, link)
    return render(request, 'pc/index.html', {'link': link, 'percent': percent})

# Web search file (.txt, .docx, .pdf)
def filetest(request):
    value = ''
    docfile = request.FILES.get('docfile')  # Obtiene el archivo subido
    
    if docfile:
        if docfile.name.endswith(".txt"):
            value = docfile.read().decode('utf-8')  # Leer el archivo .txt en memoria

        elif docfile.name.endswith(".docx"):
            document = Document(docfile)
            for para in document.paragraphs:
                value += para.text

        elif docfile.name.endswith(".pdf"):
            pdfReader = PyPDF2.PdfReader(docfile)  # Leer el archivo PDF en memoria
            for page_num in range(len(pdfReader.pages)):
                page = pdfReader.pages[page_num]
                value += page.extract_text()

    # Procesa el contenido del archivo (por ejemplo, buscar similitudes)
    percent, link = main.findSimilarity(value)
    percent = round(percent, 2)

    print("Output...................!!!!!!!!", percent, link)
    return render(request, 'pc/index.html', {'link': link, 'percent': percent})

# Text compare
def fileCompare(request):
    return render(request, 'pc/doc_compare.html') 

# Two text compare (Text)
def twofiletest1(request):
    print("Submiited text for 1st and 2nd")
    print(request.POST['q1'])
    print(request.POST['q2'])

    if request.POST['q1'] != '' and request.POST['q2'] != '': 
        print("Got both the texts")
        result = fileSimilarity.findFileSimilarity(request.POST['q1'], request.POST['q2'])
    result = round(result, 2)    
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!", result)
    return render(request, 'pc/doc_compare.html', {'result': result})

# Two text compare (.txt, .docx)
def twofilecompare1(request):
    value1 = ''
    value2 = ''
    
    if (str(request.FILES['docfile1'])).endswith(".txt") and (str(request.FILES['docfile2'])).endswith(".txt"):
        value1 = str(request.FILES['docfile1'].read())
        value2 = str(request.FILES['docfile2'].read())

    elif (str(request.FILES['docfile1'])).endswith(".docx") and (str(request.FILES['docfile2'])).endswith(".docx"):
        document1 = Document(request.FILES['docfile1'])
        for para in document1.paragraphs:
            value1 += para.text
        document2 = Document(request.FILES['docfile2'])
        for para in document2.paragraphs:
            value2 += para.text

    result = fileSimilarity.findFileSimilarity(value1, value2)
    
    print("Output..................!!!!!!!!", result)
    return render(request, 'pc/doc_compare.html', {'result': result})
