# ------------- LESSON 8, EXERCISE 3 -------------------
# Realize class Category

class Category:
    categories = [{'name': 'bus', 'is_published': True}, {'name': 'mitsubishi', 'is_published': True},
                  {'name': 'landscape', 'is_published': False}, {'name': 'laptop', 'is_published': True},
                  {'name': 'box', 'is_published': False}]

    @classmethod
    def add(cls, ctgr: str, is_publ: bool) -> int:
        """ Make new category dict in list if it's name doesn't exist in any dict

        :param ctgr: name of category
        :param is_publ: is category published
        :return: index of new category
        """
        for categry in cls.categories:
            if ctgr in categry:
                raise ValueError
        else:
            cls.categories.append(dict(zip(['name', 'is_published'], [ctgr, is_publ])))
            for categry in cls.categories:
                if categry['name'] == ctgr:
                    return cls.categories.index(categry)

    @classmethod
    def get(cls, index: int) -> str:
        if index in range(len(cls.categories)):
            return cls.categories[index]
        else:
            raise IndexError

    @classmethod
    def delete(cls, index: int) -> None:
        if index in range(len(cls.categories)):
            cls.categories.pop(index)

    @classmethod
    def update(cls, ctgr: str, is_publ: bool, index: int) -> None:
        """ Update values in category dict if input index is not out of range, else add new item to list

        :param ctgr: name of category
        :param is_publ: is category published
        :param index: index of category in list
        :return: None
        """
        if index in range(len(cls.categories)):
            cls.categories[index]['name'] = ctgr
            cls.categories[index]['is_published'] = is_publ
        elif ctgr not in cls.categories:
            cls.add(ctgr, is_publ)
        else:
            raise ValueError

    @classmethod
    def make_published(cls, index: int) -> None:
        if index in range(len(cls.categories)):
            cls.categories[index]['is_published'] = True
        else:
            raise IndexError

    @classmethod
    def make_unpublished(cls, index: int) -> None:
        if index in range(len(cls.categories)):
            cls.categories[index]['is_published'] = False
        else:
            raise IndexError


print(Category.add('tables', False))
print(Category.get(0))
Category.update('kitchen', True, 10)
Category.delete(1)
Category.make_published(1)
Category.make_unpublished(1)
print(Category.categories)
