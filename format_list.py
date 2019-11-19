def get_products(some_list):
    eng_list = some_list.replace('Название: ', 'title:').replace('Сорт: ', 'sort:').replace('Цена: ', 'price:')
    list_by_branch = eng_list.replace('Картинка: ', 'image:').replace('Выгодное предложение' , 'action:True').split('#')
    list_by_branch.remove('')
    products = {}
    for branch_txt in list_by_branch:
        branch_list = branch_txt.split('\n\n\n')
        product_list_data = [branch.split('\n') for branch in branch_list[1].split('\n\n')]
        all_tag_dict = [dict([tag.split(':') for tag in product]) for product in product_list_data]
        products[branch_list[0]] = all_tag_dict
    return products


if __name__ == '__main__':
    print(get_products('assortment.txt'))