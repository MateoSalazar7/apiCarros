from rest_framework import routers
from .api import CarroviewSet

router=routers.DefaultRouter()
router.register('api/apiCarros',CarroviewSet,'apiCarros')

urlpatterns = router.urls
