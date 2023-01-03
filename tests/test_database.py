import copy
import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15j', 'Marta', 'Perez'),
            db.Cliente('48h', 'Manolo', 'Lopez'),
            db.Cliente('28z', 'Ana', 'Garcia')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15j')
        cliente_inexistente = db.Clientes.buscar('99x')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39x', 'Hector', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39x')
        self.assertEqual(nuevo_cliente.nombre, 'Hector')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('28z'))
        cliente_modificado = db.Clientes.modificar('28z', 'Mariana', 'Garcia')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('48h')
        cliente_rebuscado = db.Clientes.buscar('48h')
        self.assertEqual(cliente_borrado.dni, '48h')
        self.assertIsNone(cliente_rebuscado)
        