from models import Category, Goods
import random

CATEGORIES = (
    {"name": "Electronics"},
    {"name": "Phones", "parent_category": "Electronics"},
    {"name": "Laptops", "parent_category": "Electronics"},
    {"name": "Books"},
    {"name": "Novels", "parent_category": "Books"},
    {"name": "Clothes"},
    {"name": "T-Shirts", "parent_category": "Clothes"}
)


def add_categories(add_root_categories_not_sub=True):
    if add_root_categories_not_sub:
        for category in CATEGORIES:
            if category.get("parent_category", None) is None:
                db_category = Category.objects.filter(name=category['name'])
                if db_category:
                    continue
                print(f"Added: {Category.objects.create(**category).save()}")
    else:
        for category in CATEGORIES:
            if category.get("parent_category", None) is not None:
                parent_category = Category.objects.filter(name=category['parent_category'])
                if not parent_category:
                    print(f"Error adding {category}")
                    continue
                db_category = Category.objects.filter(name=category['name'],
                                                      parent_category=parent_category[0].id)
                if db_category:
                    print(f"Category {category} already exists")
                    continue
                category['parent_category'] = parent_category[0].id
                print(f"Added: {Category.objects.create(**category).save()}")


def add_goods(count=5):
    categories = Category.objects
    while count:
        query = {}
        rand_category = random.randint(0, len(categories) - 1)
        query['category'] = categories[rand_category]
        it = 0
        while True:
            query['name'] = query['category'].name + str(it)
            name_db = Goods.objects.filter(name=query['name'])
            if name_db:
                it += 1
                continue
            break
        query['model'] = query['category'].name + '_' + "Model" + str(it)
        query['available'] = random.randint(0, 200)
        query['price'] = random.randint(5, 100) * 10
        print(f"Created goods: {Goods.objects.create(**query).save()}")
        count -= 1



