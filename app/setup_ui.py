from jinja2 import Template

def combobox_populate(items):
    items = sorted(items)
    return ''.join([f'<option>{i}</option>' for i in items])

def setup_template(wifi_list, wifi_manager_page=None):
    if wifi_manager_page is None:
        wifi_manager_page = open('templates/setup.html').read()
    template_wifi_manager = Template(wifi_manager_page)
    data = combobox_populate(wifi_list)

    return template_wifi_manager.render(ssid_list=data)


def main_populate(data, template_index_page=None):
    if template_index_page is None:
        template_index_page = open('template/index.html').read()
    template_index = Template(template_index_page)
    data = struct_populate(data)

    return template_index.render(ssid_list=data)

