from read_file import get_read_file

def get_products(some_list):
    eng_list = some_list.replace('Название: ', 'title:').replace('Сорт: ', 'sort:').replace('Цена: ', 'price:')
    list_by_branch = eng_list.replace('Картинка: ', 'image:').replace('Выгодное предложение', 'action:True').split('#')
    list_by_branch.remove('')
    products = {}
    for branch_txt in list_by_branch:
        product_list = [branch.split('\n') for branch in branch_txt.split('\n\n\n')[1].split('\n\n')]
        products[branch_txt.split('\n\n\n')[0]] = [dict([tag.split(':') for tag in product]) for product in product_list]
    return products


if __name__ == '__main__':
    print(get_products(get_read_file('assortment.txt')))