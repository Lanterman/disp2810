from django.urls import reverse
from django.test import TestCase

from src.main.models import Inputs



class InputListViewTest(TestCase):
    """Testing the ListInputView"""

    fixtures = ["./src/main/tests/test_data.json"]

    def test_view_url(self):
        request = self.client.get('inputs/')
        assert request.status_code == 200, request.status_code

        self.client.login(username='lanterman', password='karmavdele')
        request = self.client.get('')
        assert request.status_code == 200, request.status_code

#     def test_view_template(self):
#         request = self.client.get(reverse('news'))
#         assert request.status_code == 200, request.status_code
#         self.assertTemplateUsed(request, 'main/index.html')

#     def test_pagination(self):
#         request = self.client.get(reverse('news'))
#         assert request.status_code == 200, request.status_code
#         assert "is_paginated" in request.context, request.context
#         assert len(request.context['page_obj']) == 2, len(request.context['page_obj'])

#     def test_lists_all_pub(self):
#         with self.assertLogs(level="WARNING"):
#             request = self.client.get(reverse('news') + '?page=2')
        
#         context = request.context
#         assert request.status_code == 404, request.status_code
#         assert "exception" in context, context
#         assert context['exception'] == "Invalid page (2): That page contains no results", context['exception']

#     def test_publication_rating(self):
#         request = self.client.get(reverse('news'))
#         page_obj = request.context["page_obj"]
#         assert request.status_code == 200, request.status_code
#         assert len(page_obj) == 2, page_obj
#         assert page_obj[0].__str__() == "Second publication", page_obj[0].__str__()
#         assert page_obj[1].__str__() == "publication", page_obj[1].__str__()
#         assert page_obj[0].rat == None, page_obj[0].rat
#         assert page_obj[1].rat == None, page_obj[1].rat


# class CreateInputViewTest(TestCase):
#     """Testing the create_input_view"""

#     fixtures = ["./config/tests/test_data.json"]

#     def test_view_url(self):
#         request = self.client.get('')
#         assert request.status_code == 200, request.status_code

#         self.client.login(username='lanterman', password='karmavdele')
#         request = self.client.get('')
#         assert request.status_code == 200, request.status_code

#     def test_view_template(self):
#         request = self.client.get(reverse('news'))
#         assert request.status_code == 200, request.status_code
#         self.assertTemplateUsed(request, 'main/index.html')

#     def test_pagination(self):
#         request = self.client.get(reverse('news'))
#         assert request.status_code == 200, request.status_code
#         assert "is_paginated" in request.context, request.context
#         assert len(request.context['page_obj']) == 2, len(request.context['page_obj'])

#     def test_lists_all_pub(self):
#         with self.assertLogs(level="WARNING"):
#             request = self.client.get(reverse('news') + '?page=2')
        
#         context = request.context
#         assert request.status_code == 404, request.status_code
#         assert "exception" in context, context
#         assert context['exception'] == "Invalid page (2): That page contains no results", context['exception']

#     def test_publication_rating(self):
#         request = self.client.get(reverse('news'))
#         page_obj = request.context["page_obj"]
#         assert request.status_code == 200, request.status_code
#         assert len(page_obj) == 2, page_obj
#         assert page_obj[0].__str__() == "Second publication", page_obj[0].__str__()
#         assert page_obj[1].__str__() == "publication", page_obj[1].__str__()
#         assert page_obj[0].rat == None, page_obj[0].rat
#         assert page_obj[1].rat == None, page_obj[1].rat