def main_screen(data, template_index_page=None):
    if template_index_page is None:
        template_index_page = open('template/index.html').read()

    data = struct_populate(data)

    template_index_page.replace('<{DATA_BOX}>', data)

    return template_index.render(ssid_list=data)
