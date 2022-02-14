from django.urls     import path
from querysets.views import get_all, filter, exclude, aggregate, alias, annotate, order_by, distinct, select_related, prefetch_related, select_for_update, BeforePrefetchView

urlpatterns = [
    path('/all', get_all),
    path('/filter', filter),
    path('/exclude', exclude),
    path('/aggregate', aggregate),
    path('/annotate', annotate),
    path('/alias', alias),
    path('/order_by', order_by),
    path('/distinct', distinct),
    path('/select_related', select_related),
    path('/prefetch_related', prefetch_related),
    path('/select_for_update', select_for_update),
    path('/before-prefetch/<int:city_id>', BeforePrefetchView.as_view())
]