import pytest
from django.urls import reverse
from category.models import Region
from category.forms import RegionForm



#
# @pytest.mark.django_db
# def test_region_post_valid(client):
#     url = reverse('region')
#     data = {'name':'Moskva','sorting':24}
#     response = client.post(url,data)
#
#     assert response.status_code == 200
#     assert Region.objects.filter(name='Moskva',sorting=24).exists()





