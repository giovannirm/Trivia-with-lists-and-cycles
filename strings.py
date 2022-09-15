import time as t  # Importamos la libería time
import random as r  # Importamos la librería random
import colors as c  # Importamos los colores

error = c.RED + "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:" + c.RESET + "\n"

welcome = [
  c.YELLOW + "Bienvenido a mi Trivia",
  "Pondremos a prueba tus conocimientos",
  "¿Qué tanto sabes sobre Computación, Historia del Perú y Universal?" + c.RESET
]

def score(points, color = ""):
  if color == "red":
    color = c.RED
  else:
    color = c.CYAN
  print(color + "Tienes", points, "puntos", c.RESET)
  t.sleep(1)

def request_name():
  name = input(c.GREEN + "Ingresa tu nombre: " + c.RESET)
  t.sleep(1)  
  print("\n" + c.MAGENTA + "Hola" + c.YELLOW, name.upper() + c.RESET + c.MAGENTA, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n" + c.RESET)
  t.sleep(1)
  return name

def alternatives(index):
  alternativas = []
  if index == 1:
    alternativas = ["a", "b", "c", "d", "x"]
  else:
    alternativas = ["a", "b", "c", "d"]
  return alternativas
  
def answer(index):
  respuesta = input("Tu respuesta: ")
  alternativas = alternatives(index)
  
  while respuesta not in alternativas:
    respuesta = input(error)
  return respuesta

def repeat(name, score):
  print(c.GREEN,
          "Gracias", name.upper(), "por jugar mi trivia, alcanzaste", sum(score), "puntos", c.RESET)
  return False

questions = [
  c.RED + "{}) ¿Quién fue el creador de windows?",
  c.RED + "{}) ¿Cual de estos lenguajes de programación es de más bajo nivel?",
  c.RED + "{}) ¿En que lenguaje se progamo Minecraft?",
  c.RED + "{}) Los Chancas, pueblo que estuvo a punto de derrotar a los Incas, vivieron en lo que ahora es:"
]

secret_message = {
  "answer": c.YELLOW + "Este es un mensaje secreto" + c.RESET,
  "points": r.randint(5, 33)
}

array_alternatives = [
  [
    c.BLUE + "a) Linus Torvalds",
    "b) Bill Gates",
    "c) Mark Zuckerberg",
    "d) Dennis Ritchie" + c.RESET
  ],
  [
    c.BLUE + "a) Python",
    "b) Java",
    "c) PHP",
    "d) Assembly" + c.RESET
  ],
  [
    c.BLUE + "a) Python",
    "b) Java",
    "c) PHP",
    "d) Assembly" + c.RESET
  ],
  [
    c.BLUE + "a) Junín",
    "b) Puno",
    "c) Apurímac",
    "d) Caral" + c.RESET
  ]  
]

array_answers = [
  [
    {
      "answer": c.RED + "Linus Torvalds es el creador de Linux" + c.RESET,
      "status": False,
      "points": r.randint(-5, -1)
    },
    {
      "answer": c.GREEN + "Excelente " + c.YELLOW + "{}" + c.RESET + "!",
      "status": True,
      "points": r.randint(5, 10)
    },
    {
      "answer": c.RED + "Mark Zuckerberg es el creador de Facebook" + c.RESET,
      "status": False,
      "points": r.randint(-5, -1)
    },
    {
      "answer": c.RED + "Dennis Ritchie es el creador de Unix" + c.RESET,
      "status": False,
      "points": r.randint(-5, -1)
    }
  ],
  [
    {
      "answer": c.RED + "Python es un lenguaje de alto nivel" + c.RESET,
      "status": False,
      "points": r.randint(-8, -2)
    },
    {
      "answer": c.RED + "Java es un lenguaje de alto nivel" + c.RESET,
      "status": False,
      "points": r.randint(-8, -2)
    },
    {
      "answer": c.RED + "PHP es un lenguaje de alto nivel" + c.RESET,
      "status": False,
      "points": r.randint(-8, -2)
    },
    {
      "answer": c.GREEN + "Excelente " + c.YELLOW + "{}" + c.RESET + "!",
      "status": True,
      "points": r.randint(8, 15)
    }
  ],
  [
    {
      "answer": c.RED + "Totalmente incorrecto!" + c.RESET,
      "status": False,
      "points": 0
    },
    {
      "answer": c.GREEN + "Excelente " + c.YELLOW + "{}" + c.RESET + "!",
      "status": True,
      "points": 0
    },
    {
      "answer": c.RED + "Incorrecto!" + c.RESET,
      "status": False,
      "points": 0
    },
    {
      "answer": c.RED + "Estás equivocado!" + c.RESET,
      "status": False,
      "points": 0
    }    
  ],
  [
    {
      "answer": c.RED + "Totalmente incorrecto!" + c.RESET,
      "status": False,
      "points": r.randint(-8, -2)
    },
    {
      "answer": c.RED + "Incorrecto!" + c.RESET,
      "status": False,
      "points": r.randint(-8, -2)
    },
    {
      "answer": c.GREEN + "La respuesta correcta es la C. Apurímac" + c.RESET,
      "status": True,
      "points": r.randint(8, 15)
    },
    {
      "answer": c.RED + "Estás equivocado!" + c.RESET,
      "status": False,
      "points": r.randint(-8, -2)
    }    
  ],
]