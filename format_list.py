def get_production(filename):
	with open(filename, "r", encoding='utf-8-sig') as rose_file:
		rose_list = rose_file.read()
	eng_list = rose_list.replace('Название: ', 'title:').replace('Сорт: ', 'sort:').replace('Цена: ', 'price:')
	list_by_branch = eng_list.replace('Картинка: ', 'image:').replace('Выгодное предложение' , 'action:True').split('#')
	list_by_branch.remove('')
	production = {}
	for branch_txt in list_by_branch:
		branch_list = branch_txt.split('\n\n\n')
		product_list_data = [branch.split('\n') for branch in branch_list[1].split('\n\n')]
		all_tag_dict = [dict([tag.split(':') for tag in product]) for product in product_list_data]
		production[branch_list[0]] = all_tag_dict
	return production


if __name__ == '__main__':
	print(get_production('action.txt'))