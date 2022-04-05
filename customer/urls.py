from django.urls import path
from customer import views
urlpatterns=[
    path("home",views.CustomerIndex.as_view(),name="custhome"),
    path("accounts/register",views.SignUpView.as_view(),name='signup'),
    path("accounts/login",views.SignInView.as_view(),name='signin'),
    path("accounts/logout",views.signout,name="signout"),
    path("accounts/password/reset",views.PasswordResetView.as_view(),name="passwordreset"),
    path("carts/items/add/<int:id>",views.add_to_cart,name="addtocart"),
    path("carts/all",views.ViewMyCart.as_view(),name="viewmycart"),
    path("carts/remove/<int:id>",views.remove_from_cart,name="removeitem"),
    path("order/add/<int:c_id>/<int:p_id>",views.OrderCreateView.as_view(),name="ordercreate"),
    path("orders/all",views.OrdersListView.as_view(),name="listorders"),
]