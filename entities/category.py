class Category:
    cat_id = 0

    def __init__(self, name, parent_categories=None):
        self.name = name
        self.parent_categories = parent_categories or []

        Category.cat_id += 1


