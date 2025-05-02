from django.urls import  path, include



urlpatterns=[
    path("category/", include("api.category.urls")),
    path("product/",include("api.product.urls")),
    path("user/",include("api.user.urls")),
    path('region/', include('api.region.urls'), name='region'),
    path("blog/",include("api.blog.urls"))
]