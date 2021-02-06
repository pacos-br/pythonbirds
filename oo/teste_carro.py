from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade) # O assertEqual(0, motor.velocidade) compara o valor esperado 0 com o vloer que vai recevber no motor.velocidade

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
