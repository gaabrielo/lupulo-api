def irrigation(TemperaturaAcima30,
Temperatura20_30,
Temperatura10_20,
TemperaturaMinima,
UmidadeArAbaixo50,
UmidadeArAbaixo30,
UmidadeAr,
TempChuva,
UmidadeSoloAcima60,
UmidadeSoloAbaixo60,
PlantaAcima6,HorarioLimite):
    global res, resp

    if (PlantaAcima6):
      resp = "Planta acima dos 6 metros - irrigar metade do volume."
    else:
      resp = None

    if (HorarioLimite):
      res = "Passou das 16h - não irrigar"
      
    elif (TempChuva):
      if (UmidadeArAbaixo50):
        res = "Pouco chuva e Umidade baixa - irrigar com frequencia diminida pela metade"
      elif (UmidadeAr):
        res = "Clima chuvoso - não irrigar"
        
    else:
        if(TemperaturaAcima30):
          if(UmidadeArAbaixo30):
            res = "Ambiente superAquecido-Irrigação será ligada de 1 em 1 hora!"
          else:
            res = "Temperatura alta - Irigação será ligada de 2 em 2 horas!"
            
        elif (Temperatura20_30):
            if(UmidadeAr):
                if(UmidadeSoloAbaixo60):
                    res = "Solo seco/Temperatura Baixa - liguar a irrigaçao com menor frequencia"
                elif(UmidadeSoloAcima60):
                    res= "Solo Umido/Temperatura Baixa - Não irá ligar a irrigação"
            elif(UmidadeArAbaixo50):
                if(UmidadeSoloAcima60):
                    res="Solo Muito umido - Não irrigar"
                elif(UmidadeSoloAbaixo60):
                    res = "Solo seco - Ligar irrigação normal"
                    
        elif (TemperaturaMinima):
            res = "Clima muito frio - Não irrigar"
            
        elif (Temperatura10_20):
            if(UmidadeAr):
                if(UmidadeArAbaixo50):
                    res = "Temperatura baixa e umidade do solo baixa - ligar uma vez de manhã com metade do volume"
                else:
                    res = "Temperatura Baixa - Não irá ligar irrigação"
            elif(UmidadeArAbaixo50):
                if(UmidadeSoloAcima60):
                    res = "Solo Muito umido - Não irrigar"
                elif(UmidadeSoloAbaixo60):
                    res = "Ligar irrigação só uma vez de manhã"

    return [res, resp]
