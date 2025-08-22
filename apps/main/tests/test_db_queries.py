from django.test import TestCase
from django.db.models import QuerySet

from apps.main import db_queries, models


class TestGetInputList(TestCase):
    """Testing the get_input_list function"""

    fixtures = ["./apps/main/tests/test_data.json"]

    def test_count_entries(self) -> None:
        """Testing count entries"""

        response = db_queries.get_input_list()
        assert len(response) == 20, len(response)

        models.Inputs.objects.create(input_field={"value": "test"})
        response = db_queries.get_input_list()
        assert len(response) == 21, len(response)
    
    def test_type_of_response(self) -> None:
        """Testing type of response"""

        response = db_queries.get_input_list()
        assert type(response) == QuerySet, type(response)


class TestGetLastInputId(TestCase):
    """Testing the get_last_input_id function"""

    fixtures = ["./apps/main/tests/test_data.json"]

    def test_last_input_id(self) -> None:
        """Testing count entries"""

        response = db_queries.get_last_input_id()
        assert response == 20, response

        models.Inputs.objects.create(input_field={"value": "test"})
        response = db_queries.get_last_input_id()
        assert response == 21, response
    
    def test_default_value(self) -> None:
        """Testing default value"""

        models.Inputs.objects.all().delete()
        response = db_queries.get_last_input_id()
        assert response == 1, response
    
    def test_type_of_response(self) -> None:
        """Testing type of response"""

        response = db_queries.get_last_input_id()
        assert type(response) == int, type(response)

        models.Inputs.objects.all().delete()
        response = db_queries.get_last_input_id()
        assert type(response) == int, type(response)


class TestCreateInput(TestCase):
    """Testing the create_input function"""

    fixtures = ["./apps/main/tests/test_data.json"]

    def test_create_input(self) -> None:
        """Testing create_input"""

        query = models.Inputs.objects.count()
        assert query == 20, query

        response = db_queries.create_input({"value": "value"})
        query = models.Inputs.objects.count()
        self.assertIsNone(response, response)
        assert query == 21, query
