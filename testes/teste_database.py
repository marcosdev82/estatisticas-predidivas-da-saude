# tests/test_database.py

import unittest
from database.db import init_db

class TestDatabase(unittest.TestCase):
    def test_init_db(self):
        try:
            init_db()
            self.assertTrue(True)  # Supondo que não ocorreu erro
        except Exception as e:
            self.fail(f'Erro ao inicializar o banco de dados: {e}')

if __name__ == '__main__':
    unittest.main()