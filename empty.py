from docxtpl import DocxTemplate
import csv
import json
with open('data', 'r') as f:
    list_data = f.read()
a = ','
list_data = list_data.replace(', ',a)
list_data = list_data.split(',')
list_data = list(list_data)
marka = list_data[0]
model = list_data[1]
consumption = list_data[2]
price = list_data[3]

def get_context(marka, model, consumption, price):
    return {'марка': marka, 'модель': model, 'расход': consumption, 'цена': price}

def from_template(marka, model, consumption, price, template):
    template = DocxTemplate(template)
    context = get_context(marka, model, consumption, price)
    template.render(context)
    template.save(marka + '_report.doсх')

def generate_report(marka, model, consumption, price):
    template = 'doc.docx'
    document = from_template(marka, model, consumption, price, template)
generate_report(marka, model, consumption, price)

list_1 = [['car','model','consumption','price'],['toyota','corolla',1,1.5]]

with open('car.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&')
    writer.writerows(list_1)

with open('car.csv') as m:
    reader = csv.reader(m, delimiter = '&')
    for row in reader:
        print(row)

dict = {'car' : 'toyota', 'model' : 'corolla', 'consumption' : 7, 'price' : 1.5}

with open('dict_to_json.txt', 'w') as f:
    json.dump(dict, f)

with open('dict_to_json.txt') as f:
    data = json.load(f)
    print(data)