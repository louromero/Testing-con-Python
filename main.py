import unittest
import datetime
from unittest.mock import patch

def sum(a, b):
    return a + b

class Greeter:
    def greet(self, name):
        # Elimina los espacios en blanco al principio y al final del nombre
        name = name.strip()
        
        # Capitalizar la primera letra del nombre
        name = name.capitalize()
        
        # Obtener la hora actual
        current_time = datetime.datetime.now().time()
        
        if datetime.time(6, 0) <= current_time < datetime.time(12, 0):
            greeting = f"Good morning {name}"
        elif datetime.time(18, 0) <= current_time < datetime.time(22, 0):
            greeting = f"Good evening {name}"
        else:
            greeting = f"Good night {name}"
            
        return greeting

class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        
class GreeterTest(unittest.TestCase):
    @patch('datetime.datetime')
    def test_greet_morning(self, mock_datetime):
        greeter = Greeter()
        mock_datetime.now.return_value.time.return_value = datetime.time(8, 0, 0)  # Hora entre las 6 y las 12
        # Verificamos que el saludo sea "Good morning"
        self.assertEqual(greeter.greet(name), f"Good morning {name.capitalize()}")
    
    @patch('datetime.datetime')
    def test_greet_evening(self, mock_datetime):
        greeter = Greeter()
        mock_datetime.now.return_value.time.return_value = datetime.time(20, 0, 0) # Hora entre las 18 y 22
        self.assertEqual(greeter.greet(name), f"Good evening {name.capitalize()}")
    
    @patch('datetime.datetime')
    def test_greet_night(self, mock_datetime):
        greeter = Greeter()
        mock_datetime.now.return_value.time.return_value = datetime.time(22, 0, 0)
        self.assertEqual(greeter.greet(name), f"Good night {name.capitalize()}")

if __name__ == '__main__':
    
    # Crear una instancia de la clase Greeter
    greeter = Greeter()

    # Pedir al usuario que ingrese su nombre por teclado
    name = input("Please, enter your name: ")

    # Mostrar metodo greeter
    print(greeter.greet(name))
    
    unittest.main()