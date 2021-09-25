from django.contrib import admin
from django.urls import path
from app.views import home, cadastro_empresa, menu_empresa, cadastro_produto, menu_produto, edit_empresas, \
                        delete_empresas, update_empresas, edit_produtos, update_produtos, delete_produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cdtempresa/', cadastro_empresa, name='cadastro_empresa'),
    path('mnuempresa/', menu_empresa, name='menu_empresa'),
    path('cdtproduto/', cadastro_produto, name='cadastro_produto'),
    path('mnuproduto/', menu_produto, name='menu_produto'),
    path('editempresa/<int:pk>/', edit_empresas, name='editempresa'),
    path('updateempresa/<int:pk>/', update_empresas, name='updateempresa'),
    path('deleteempresa/<int:pk>/', delete_empresas, name='deleteempresa'),
    path('editproduto/<int:pk>/', edit_produtos, name='editproduto'),
    path('updateproduto/<int:pk>/', update_produtos, name='updateproduto'),
    path('deleteproduto/<int:pk>/', delete_produtos, name='deleteproduto')
]
