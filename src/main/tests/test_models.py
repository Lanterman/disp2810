from django.test import TestCase

from src.main.models import Inputs


class TestInputsModel(TestCase):
    """Testing the Inputs model"""

    fixtures = ["./src/main/tests/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.input = Inputs.objects.get(id=1)

    def test_name_label(self):
        field_label = self.input._meta.get_field('input_field').verbose_name
        assert field_label == 'input field', field_label

    def test_str(self):
        test_data = "{'name': 'Input name1'}"
        assert self.input.__str__() == f"{self.input.input_field}", self.input.__str__()
        assert self.input.__str__() == test_data, self.input.__str__()