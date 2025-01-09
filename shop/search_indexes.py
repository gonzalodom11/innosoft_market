from haystack import indexes
from .models import Product  # Ajusta según tu modelo

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Define qué productos serán indexados."""
        return self.get_model().objects.filter(available=True)
