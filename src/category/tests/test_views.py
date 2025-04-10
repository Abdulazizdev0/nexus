import pytest
from category.views import region
from category.models import Region


@pytest.mark.django_db
def test_region_views():
    region = Region.objects.create(name="USA",sorting=5)

    assert region.name == "USA"
    assert region.sorting == 5
