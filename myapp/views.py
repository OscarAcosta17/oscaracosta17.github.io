from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from docx import Document
import os
import whisper

def index(request):
    return render(request, 'index.html')

def transcribe_audio(audio_file):
    try:
        # Guardar el archivo de audio en la carpeta "Clases" del sistema de archivos de Django
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'Clases'))
        filename = fs.save(audio_file.name, audio_file)

        # Obtener la ruta completa del archivo de audio
        ruta_audio = fs.path(filename)
        print(f"Ruta del archivo de audio: {ruta_audio}")  # Debug: Verificar la ruta del archivo de audio

        # Ejemplo de transcripción usando Whisper
        model = whisper.load_model("medium")
        print(f"Modelo cargado correctamente: {model}")  # Debug: Verificar que el modelo se carga correctamente

        result = model.transcribe(ruta_audio)
        print(f"Resultado de la transcripción: {result}")  # Debug: Verificar el resultado de la transcripción

        texto_transcrito = result["text"]

        # Crear el documento Word
        doc = Document()
        doc.add_paragraph(texto_transcrito)

        # Nombre del archivo .docx y carpeta donde se guardará
        nombre_archivo = audio_file.name.split('.')[0] + ".docx"
        carpeta_transcripciones = "Transcripciones"
        ruta_completa = os.path.join(settings.MEDIA_ROOT, carpeta_transcripciones, nombre_archivo)
        print(f"Ruta del documento .docx: {ruta_completa}")  # Debug: Verificar la ruta del documento .docx

        # Guardar el documento Word en la carpeta Transcripciones
        doc.save(ruta_completa)
        print("Documento .docx guardado correctamente.")  # Debug: Confirmar que el documento se guarda correctamente

        return ruta_completa

    except Exception as e:
        print(f"Error en la transcripción: {str(e)}")
        return None

def upload_and_process(request):
    if request.method == 'POST' and request.FILES['audio']:
        audio_file = request.FILES['audio']

        # Realizar la transcripción del audio y obtener la ruta del documento .docx
        ruta_docx = transcribe_audio(audio_file)

        if ruta_docx:
            # Crear la respuesta HTTP para la descarga automática del archivo .docx
            with open(ruta_docx, 'rb') as docx_file:
                response = HttpResponse(docx_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(ruta_docx)}"'
                return response
        else:
            return HttpResponse('Error en la transcripción del audio.', status=500)

    return render(request, 'index.html')