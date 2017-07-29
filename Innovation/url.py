from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^api/project/create/$', views.Projects.as_view(), name='project_create'),
    url(r'^api/projects$', views.ProjectGet.as_view(), name='project_get'),
    url(r'^api/collaborator/create/$', views.CollaboratorCreate.as_view(), name='collaborative_create'),
    url(r'^api/collaborators$', views.CollaboratorGet.as_view(), name='collaborative_get'),
    url(r'^api/project/like/(?P<id>[0-9]+)$', views.ProjectLike.as_view(), name='project_like'),
    url(r'^api/project/favourite/(?P<id>[0-9]+)$', views.ProjectFavourite.as_view(), name='project_favourite'),

]

