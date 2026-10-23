import serial

porta_serial = serial.Serial('COM3', 9600) 

with open('dados_sensores.csv', 'a') as arquivo:
    arquivo.write("batt_voltage,id,bme_pressure,bme_rh,bme_temp,scd30_temp,scd30_rh,scd30_co2,sds_pm25,sds_pm10\n")
    
    while True:
        try:
            linha = porta_serial.readline().decode('utf-8')
            print(linha, end='') 
            arquivo.write(linha)
            arquivo.flush()
        except KeyboardInterrupt:
            print("Encerrando...")
            break