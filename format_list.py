from read_file import get_read_file

def get_products(some_list):
    eng_list = some_list.replace('Название: ', 'title:').replace('Сорт: ', 'sort:').replace('Цена: ', 'price:')
    product_group_descriptions = eng_list.replace('Картинка: ', 'image:').replace('Выгодное предложение', 'action:True').split('#')
    product_group_descriptions.remove('')
    products = {}
    for group in product_group_descriptions:
        product_list = [branch.split('\n') for branch in group.split('\n\n\n')[1].split('\n\n')]
        products[group.split('\n\n\n')[0]] = [dict([tag.split(':') for tag in product]) for product in product_list]
    return products


if __name__ == '__main__':
    print(get_products(get_read_file('assortment.txt')))