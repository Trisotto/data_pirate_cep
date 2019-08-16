import jsonlines

def beautify_str(string):
    return string.strip()

def beautify_item(item):
    item['range_cep'] = beautify_str(item.get('range_cep'))
    item['address'] = beautify_str(item.get('address'))

def validate_item(item):
    return item.get('range_cep') != None and item.get('range_cep') != '' and \
            item.get('address') != None and item.get('address') != ''

def write_addresses(addresses):
    with jsonlines.open('addresses.jsonl', mode='w') as writer:
        for uf in addresses.keys():
            writer.write({'uf': uf, 'addresses': addresses.get(uf)})