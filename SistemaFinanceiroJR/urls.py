from django.conf.urls import patterns, include, url

from django.contrib import admin
from Cadastro.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaFinanceiroJR.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/$','Cadastro.views.homepage',name='homepage'),
    url(r'^contato/novo/$','Cadastro.views.edita_contato', name='novo_contato'),
    url(r'^contato/(?P<contato_id>\d+)/$','Cadastro.views.edita_contato', name='edita_contato'),
    url(r'^contato/excluir/(?P<contato_id>\d+)/$','Cadastro.views.excluir_contato', name='excluir_contato'),
    url(r'^contatos/$', 'Cadastro.views.Contatos', name='Contatos'),

)
