from .models import StoredItem


def store_item(stored_item):
    try:
        item = StoredItem.objects.get(item=stored_item.item)
        item.quantity += stored_item.quantity
        item.save()
    except StoredItem.DoesNotExist:
        stored_item.save()
