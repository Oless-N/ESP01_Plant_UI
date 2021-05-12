def render(page, tag_dict):
    if page:
        for key, value in tag_dict:
            page.replace(key, value)
        return page

def main_screen(data, template_index_page=None):
    if template_index_page is None:
        template_index_page = open('template/index.html').read()

    data = struct_populate(data)

    template_index_page.replace('<{DATA_BOX}>', data)

    return template_index.render(ssid_list=data)
