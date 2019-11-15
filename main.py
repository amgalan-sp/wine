from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from winery_age import get_winery_age


with open("action.txt", "r", encoding='utf-8-sig') as rose_file:
	rose_list= rose_file.read()
eng_list= rose_list.replace('Название: ', 'title:').replace('Сорт: ', 'sort:').replace('Цена: ', 'price:')
list_by_branch = eng_list.replace('Картинка: ','image:').replace('Выгодное предложение','action:True').split('#')
list_by_branch.remove('')
production = {}
for branch_txt in list_by_branch:
	branch_list= branch_txt.split('\n\n\n')
	product_list_data = [branch.split('\n') for branch in branch_list[1].split('\n\n')]
	all_tag_dict = [dict([tag.split(':') for tag in product]) for product in product_list_data]
	production.update({branch_list[0]:all_tag_dict})


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    winery_age=get_winery_age(), production=production)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
