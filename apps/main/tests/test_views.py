from django.urls import reverse
from django.test import TestCase


class TestGetInputListViewTest(TestCase):
    """Testing the get_list_inputs_view"""

    fixtures = ["./apps/main/tests/test_data.json"]

    def test_get_view_status(self) -> None:
        response = self.client.get(reverse("input-list"))
        assert response.status_code == 200, response.status_code

    def test_view_template(self) -> None:
        response = self.client.get(reverse("input-list"))
        self.assertTemplateUsed(response, "main/inputs.html")

    def test_get_method_context(self) -> None:
        response = self.client.get(reverse("input-list"))
        assert response.context["title"] == "Список инпутов", response.context["title"]
        assert len(response.context["inputs"]) == 20, len(response.context["inputs"])


class CreateInputViewTest(TestCase):
    """Testing the create_input_view"""

    fixtures = ["./apps/main/tests/test_data.json"]

    def test_get_view_status(self) -> None:
        response = self.client.get(reverse("create-input"))
        assert response.status_code == 200, response.status_code
    
    def test_post_view_status(self) -> None:
        response = self.client.post(reverse("create-input"), data={"value": "Input name1"})
        assert response.status_code == 200, response.status_code

    def test_view_template(self) -> None:
        response = self.client.get(reverse("create-input"))
        self.assertTemplateUsed(response, "main/create_input.html")

    def test_get_method_context(self) -> None:
        response = self.client.get(reverse("create-input"))
        assert response.context["title"] == "Создать инпут", response.context["title"]
        assert response.context["last_entry_id"] == 20, response.context["last_entry_id"]
