# ------------- LESSON 8, EXERCISE 3 -------------------
# Realize class Category

class Category:
    def __init__(self, categories: list[dict[str: str, str: bool]]):
        self.categories = categories

    def add(self, ctgr: str, is_publ: bool) -> int:
        """
        Make new category dict in list if it's name doesn't exist in any dict
        :param ctgr: name of category
        :param is_publ: is category published
        :return: index of new category
        """
        for categry in self.categories:
            if ctgr in categry:
                raise ValueError
        else:
            self.categories.append(dict(zip(['name', 'is_published'], [ctgr, is_publ])))
            for categry in self.categories:
                if categry['name'] == ctgr:
                    return self.categories.index(categry)

    def get(self, index: int) -> str:
        if index in range(len(self.categories)):
            return self.categories[index]
        else:
            raise IndexError

    def delete(self, index: int) -> None:
        if index in range(len(self.categories)):
            self.categories.pop(index)

    def update(self, ctgr: str, is_publ: bool, index: int) -> None:
        """
        Update values in category dict if input index is not out of range, else add new item to list
        :param ctgr: name of category
        :param is_publ: is category published
        :param index: index of category in list
        :return: None
        """
        if index in range(len(self.categories)):
            self.categories[index]['name'] = ctgr
            self.categories[index]['is_published'] = is_publ
        elif ctgr not in self.categories:
            self.add(ctgr, is_publ)
        else:
            raise ValueError

    def make_published(self, index: int) -> None:
        if index in range(len(self.categories)):
            self.categories[index]['is_published'] = True
        else:
            raise IndexError

    def make_unpublished(self, index: int) -> None:
        if index in range(len(self.categories)):
            self.categories[index]['is_published'] = False
        else:
            raise IndexError


category = Category([{'name': 'bus', 'is_published': True}, {'name': 'mitsubishi', 'is_published': True},
                     {'name': 'landscape', 'is_published': False}, {'name': 'laptop', 'is_published': True},
                     {'name': 'box', 'is_published': False}])

print(category.add('tables', False))
print(category.get(5))
category.update('kitchen', True, 10)
category.delete(1)
category.make_published(1)
category.make_unpublished(1)
print(category.categories)
