import pytest
from category.models import Category, Region, Brand

@pytest.mark.django_db
def test_create_main_category():
    category = Category.objects.create(
        name="Elektronika",
        is_main=True,
        slug="elektronika"
    )
    assert category.name == "Elektronika"
    assert category.is_main is True
    assert category.slug == "elektronika"
    assert category.parent is None

@pytest.mark.django_db
def test_create_subcategory():
    parent = Category.objects.create(name="Elektronika", slug="elektronika")
    sub = Category.objects.create(
        name="Telefonlar",
        slug="telefonlar",
        parent=parent
    )
    assert sub.parent == parent

@pytest.mark.django_db
def test_create_region():
    region = Region.objects.create(name="Toshkent", sorting=4)
    assert region.name == "Toshkent"
    assert region.sorting == 4

@pytest.mark.django_db
def test_create_brand():
    brand = Brand.objects.create(name="Samsung")
    assert brand.name == "Samsung"


