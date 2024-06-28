import unittest
from task_3 import find_differences


class TestFindDifferences(unittest.TestCase):
    def test_simple_diff(self):
        Json_old = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T11:00:00+03:00',
            }
        }

        Json_new = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T13:00:00+03:00',
            }
        }

        diff_list = ['services', 'staff', 'datetime']
        expected_result = {
            'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                          'amount': 1}],
            'datetime': '2022-01-25T13:00:00+03:00'
        }

        self.assertEqual(find_differences(Json_old, Json_new, diff_list), expected_result)

    def test_no_diff(self):
        Json_old = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T11:00:00+03:00',
            }
        }

        Json_new = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T11:00:00+03:00',
            }
        }

        diff_list = ['services', 'staff', 'datetime']
        expected_result = {}

        self.assertEqual(find_differences(Json_old, Json_new, diff_list), expected_result)

    def test_empty_diff_list(self):
        Json_old = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T11:00:00+03:00',
            }
        }

        Json_new = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T13:00:00+03:00',
            }
        }

        diff_list = []
        expected_result = {}

        self.assertEqual(find_differences(Json_old, Json_new, diff_list), expected_result)

    def test_additional_param_in_diff_list(self):
        Json_old = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T11:00:00+03:00',
                'confirmed': 1
            }
        }

        Json_new = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}],
                'staff': {'id': 1819441, 'name': 'Мастер'},
                'datetime': '2022-01-25T11:00:00+03:00',
                'confirmed': 0
            }
        }

        diff_list = ['services', 'staff', 'datetime', 'confirmed']
        expected_result = {
            'confirmed': 0
        }

        self.assertEqual(find_differences(Json_old, Json_new, diff_list), expected_result)


if __name__ == '__main__':
    unittest.main()
