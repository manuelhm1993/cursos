"""ISP: principio de segregación de la interfaz, dicta que ningún cliente tiene que
ser forzado a depender de interfaces que no utilice. Hay que eliminar las interfaces
que no se van a utilizar."""
from .classes.humano import Humano
from .classes.robot import Robot

robot  = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()