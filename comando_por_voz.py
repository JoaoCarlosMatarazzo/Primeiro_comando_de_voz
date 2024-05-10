print("Testando...")

import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala:
def ouvir_microfone():
    # Habilita o microfone do usuário:
    microfone = sr.Recognizer()
    
    # Usando o microfone:
    with sr.Microphone() as source:
        # Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)
        print("Por favor, diga algo: ")

        # Armazena o que foi dito:
        audio = microfone.listen(source)
    
    try:
        # Passar a variável de uma forma que o algoritmo reconheça os padrões da língua
        frase = microfone.recognize_google(audio, language='pt-BR')
        if "navegar" in frase:
            os.system("start Chrome.exe")
            return False 
        elif "Excel" in frase:
            os.system("start Excel.exe")
            return False
        elif "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False  
        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False
        elif "Fechar" in frase:
            return True

        # Retornar a frase pronunciada
        print("Você disse: " + frase)

    # Se ele não entender o que foi dito:
    except sr.UnknownValueError:
        print("Não entendi.")
    except sr.RequestError:
        print("Não foi possível conectar-se ao serviço de reconhecimento de fala.")
    return frase

while True:
    if ouvir_microfone():
        break
