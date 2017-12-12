from .models import StoredItem, Item


def store_item(stored_item=StoredItem):
    item = StoredItem.objects.get(item=stored_item.item)
    print(item)
    if item:
        item.quantity += stored_item.quantity
        item.save()
    else:
        stored_item.save()

