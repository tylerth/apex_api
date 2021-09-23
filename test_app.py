import unittest
from app import app

class BasicTestCase(unittest.TestCase):

    # tests "/<platform>/<user>"
    def test_player_data(self):
        tester = app.test_client(self)
        response = tester.get('/X1/iCATxMythos', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'iCATxMythos', response.data)

    # tests "/map_rotations"
    def test_map_rotations(self):
        tester = app.test_client(self)
        response = tester.get('/map_rotations', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'arenas_unranked', response.data)
        self.assertIn(b'br_unranked', response.data)

    # tests "/map_rotation/<gamemode>"
    def test_map_rotation(self):
        tester = app.test_client(self)
        response = tester.get('/map_rotation/battle_royale', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'current_map', response.data)

    # tests route "/<platform>/<user>/legends"
    def test_legends_info(self):
        tester = app.test_client(self)
        response = tester.get('/X1/iCATxMythos/legends', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bangalore', response.data)

    # tests route "/<platform>/<user>/<legend>"
    def test_legend_info(self):
        tester = app.test_client(self)
        response = tester.get('/X1/iCATxMythos/Gibraltar', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Missing', response.data)


if __name__ == '__main__':
    unittest.main()