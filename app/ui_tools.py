class BasePage:

    def combobox_populate(self, items):
        items = sorted(items)
        return ''.join([f'<option>{i}</option>' for i in items])

    def prepare_chunk(self, data_list, chunk_type):
        return getattr(chunk_type, data_list)


class Page(BasePage):
    def __init__(self, path_template):
        self.path = path_template
        with open(self.path) as template:
            self.page = template.read()

    def render(self, tag_dict):
        if self.page:
            for key, value in tag_dict:
                self.page.replace(key, value)
