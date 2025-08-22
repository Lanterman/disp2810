import logging

from django.test import TestCase
from django.db.models import QuerySet

from apps.main import services, models


class TestGetInputList(TestCase):
    """Testing the get_input_list function"""

    fixtures = ["./apps/main/tests/test_data.json"]

    def test_count_entries(self) -> None:
        """Testing count entries"""

        response = services.get_input_list()
        assert len(response) == 20, len(response)

        models.Inputs.objects.create(input_field={"value": "test"})
        response = services.get_input_list()
        assert len(response) == 21, len(response)
    
    def test_type_of_response(self) -> None:
        """Testing type of response"""

        response = services.get_input_list()
        assert type(response) == QuerySet, type(response)
    
    def test_console_message(self) -> None:
        """Testing"""

        services.get_input_list()
        self.assertWarnsMessage(logging.INFO, "Count elems: 20")


class TestCreateInput(TestCase):
    """Testing the create_input function"""

    fixtures = ["./apps/main/tests/test_data.json"]

    def test_create_input(self) -> None:
        """Testing create_input"""

        query = models.Inputs.objects.count()
        assert query == 20, query

        response = services.create_input({"value": "value"})
        query = models.Inputs.objects.count()
        self.assertIsNone(response, response)
        assert query == 21, query
    
    def test_console_message(self) -> None:
        """Testing"""

        data = {"value": "value"}
        services.create_input(data)
        self.assertWarnsMessage(logging.INFO, f"The entry {data} is added!")