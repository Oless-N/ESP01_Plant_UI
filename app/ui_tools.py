def combobox_populate(items):
    items = sorted(items)
    return ''.join([f'<option>{i}</option>' for i in items])
