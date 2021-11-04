def load_page():
    with open('index.html', 'r') as index_page:

        return index_page.read()

fake_data = {
    'k1': 'v65tf89x7v',
    'k2': 'v1c9vewfx7vdvs',
    'k3': 'v1w389x7vfer',
    'k4': 'v1c9vsrgw',
    'k5': 'v1c9v7rg3efx7v',
}

def reload_box(data):
    str_box_list = []
    for k, v in data:
        str_box_list.append(
            f'<li>{k} {v}</li>'
        )
    return f'<ul>{str_box_list}</ul>'


if __name__ == '__main__':
    print(load_page().replace('{{reload.box}}', reload_box(fake_data)))

