# Meta_backend_developer_capstone

 Through this api, restaurants can build their own dishes and manage the price, name and other details of each dish. Users can order meals through this API, and the model of the meal and the information of the dish created by the restaurant will be associated in the form of an external key in the database. Based on this API, developers can use React for further website construction or mobile app construction. Applications on different platforms can use this API for unified data management. The api includes a user authentication system, and each user has a unique token. auth includes a page for users to register, and users can access and upload their own bookings by associating users with tokens.
 
To the specific api url:
    path('admin/', admin.site.urls),
    path('',views.index),
    path('api/booking/', include(router.urls)),
    path('api/menu-items/', include('reastaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
    
    user need to regist a account and being assigned a token which can be used for api request
