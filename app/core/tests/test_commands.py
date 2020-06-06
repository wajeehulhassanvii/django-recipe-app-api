from unittest.mock import patch

from django.core.management import call_command

from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_read(self):
        """Test waiting for the db when db is available"""
        # if retrieves operational error then db isn't available
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # means whenever django.db.utils.ConnectionHandles.__getitem__
            # is called during test, instead of performing the behaviour
            # replace with mock object and return True
            gi.return_velue = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # it will be while loop, itll check for operational handler
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # Five times operatinal error then True
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
