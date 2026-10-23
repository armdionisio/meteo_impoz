import requests
import time

# Variables for ThingSpeak
server = "https://api.thingspeak.com/update"
apiKey = "G294TLEBZ42P57G0" 
# Get values from the captors
temperatura = 101
humidade = 100
pressao = 100000
luz = 10
rain = "moderada"
clima = "nublado"
airStatus = "Boa"
vento = 10.2
while(True):


    # Define the parameters as a dictionary
    payload = {
        "api_key": apiKey,
        "field1": f"{temperatura:.1f}",
        "field2": f"{humidade:.1f}",
        "field3": f"{pressao:.1f}",
        "field4": luz,
        "field5": rain,
        "field6": clima,
        "field7": f"{vento:.1f}",
        "field8": airStatus
    }

    # Sending and receiving the answer using the params argument
    resposta = requests.get(server, params=payload)
    vento += 1
    if resposta.status_code == 200:
        print("Enviado com sucesso")
        print(resposta.text)
    else: 
        print(f"Erro: {resposta.status_code}")

    time.sleep(30)