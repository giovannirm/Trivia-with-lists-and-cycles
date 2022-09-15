import time as t  # Importamos la libería time
import colors as c  # Importamos los colores
import strings as s # Importamos las cadenas de texto

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje"
puntaje = [0]

# Mostramos el texto de bienvenida
for message_welcome in s.welcome:
  print(message_welcome)
  # for i in message_welcome:
  #   print(i, end="")
  #   t.sleep(0.1)
  t.sleep(1)
  
s.score(puntaje[0], "red")

nombre = s.request_name()

# Para repetir la trivia
iniciar_trivia = True
# Para mostrar los intentos realizados
intento = 1
i = 0

# La trivia continuará hasta que cambie su estado
while iniciar_trivia == True:
  for question in s.questions:
    # Pregunta
    print(question.format(i + 1))
    t.sleep(1)
    alternatives = s.alternatives(s.questions.index(question))
    # Alternativas
    for alternativas in s.array_alternatives[s.questions.index(question)]:
      print(alternativas)

    # Almacenamos la respuesta del usuario en la variable respuesta
    respuesta = s.answer(s.questions.index(question))

    # Mensaje secreto para el pregunta 2
    if respuesta == "x" and s.questions.index(question) == 1:
      puntaje.append(s.secret_message["points"])
      print(s.secret_message["answer"])
      i += 1
      s.score(puntaje[i])
    else:
      # Respuestas
      for answer in s.array_answers[s.questions.index(question)]:
        # Respuesta correcta
        if answer["status"] == True:
          if alternatives.index(respuesta) == s.array_answers[s.questions.index(question)].index(answer):
            mensaje = ""
            # Si se trata de la tercera pregunta
            if s.questions.index(question) == 2:
              # Si su puntaje es positivo
              if(sum(puntaje)) >= 0:
                mensaje = "Tu puntaje se multiplicó por 2"
                puntos = sum(puntaje) * 2
                
              # Si su puntaje es negativo
              else:
                mensaje = "Tu puntaje volvió a 0 para compensar tus puntos negativos"
                puntos = 0
                
              puntaje = [0, 0, 0]
              puntaje.append(puntos)
            else:
              puntaje.append(answer["points"])
            
            # Imprimimos la respuesta de la alternativa correcta
            print(answer["answer"].format(nombre.upper()))
            i += 1
            if mensaje == "":
              s.score(puntaje[i])
            else:
              print(c.CYAN + mensaje + c.RESET)
        # Respuesta incorrecta
        elif answer["status"] == False:
          # Debemos encontrar la respuesta recibida por pantalla
          if alternatives.index(respuesta) == s.array_answers[s.questions.index(question)].index(answer):
            # Si se trata de la tercera pregunta
            if s.questions.index(question) == 2:
              if s.array_answers[s.questions.index(question)].index(answer) == 0:  
                puntos = sum(puntaje) / 2
                mensaje = "Tu puntaje se dividió a la mitad"
              if s.array_answers[s.questions.index(question)].index(answer) == 2:
                puntos =  sum(puntaje) - 5
                mensaje = "A tu puntaje se le restó 5"
              if s.array_answers[s.questions.index(question)].index(answer) == 3:
                puntos =  (sum(puntaje) + (-8))
                mensaje = "A tu puntaje se le sumó -8"
              puntaje = [0, 0, 0]
              puntaje.append(puntos)
              print(answer["answer"])
              i += 1
              print(c.CYAN + mensaje + c.RESET)
            else:
              puntaje.append(answer["points"])
              print(answer["answer"])
              i += 1
              s.score(puntaje[i])
                 
    print(c.GREEN + "Tu puntaje total es de:", sum(puntaje), c.RESET, "\n")
    t.sleep(2)

  print("\nIntento número:", intento)

  print(c.RED, "\n¿Deseas intentar la 'ruleta de puntaje final' nuevamente?", c.RESET)

  repetir_trivia = input(
      c.YELLOW +
      "Ingresa 'sí' para repetir, o cualquier tecla para finalizar: " +
      c.RESET + "\n").lower()

  intento += 1

  if repetir_trivia != "sí":  # != significa "distinto"    
    iniciar_trivia = s.repeat(nombre, puntaje)  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
    
  else:
    puntaje = [0]
    i = 0
