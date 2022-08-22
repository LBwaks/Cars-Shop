from django.urls import path 
from .views import reject_approval, BidsView,buy_car,update_payments,payment_done,payment_canceled, MyBidsView, AddBidView,BidDetailView,EditBidView,DeleteBidView

urlpatterns = [
    path('',BidsView.as_view(),name="bids"),
    path('<slug>',BidDetailView.as_view(),name="bid_details"),
    path('edit/<slug>',EditBidView.as_view(),name='edit_bid'),
    path('delete/<slug>',DeleteBidView.as_view(),name='delete_bid'),
    path('bid_car/<car_id>/',AddBidView.as_view(),name='bid_car'),
    path('my_bids/',MyBidsView.as_view(),name='my_bids'),
    path("<slug>/reject", reject_approval, name="reject_approval"),
    path('<slug>/process-payment/', buy_car, name='buy_car'),
    path('finish_payments/<slug>', update_payments, name='finish_payments'),
    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),
]
