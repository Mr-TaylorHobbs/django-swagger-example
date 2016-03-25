import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from api.models import Swag


class SwagTestCase(TestCase):

    def test_swag_view(self):
        one = Swag.objects.create(name='First', is_dj=False)
        response = self.client.get(reverse('swag_endpoint', kwargs={'pk': one.pk}))
        json_response = json.loads(response.content.decode())
        from pprint import pprint
        pprint(json_response)
        self.assertEqual({'name': 'good'}, json_response)
