def setups_screen(wifi_list, wifi_manager_page=None):
    if wifi_manager_page is None:
        wifi_manager_page = open('templates/setup.html').read()
    template_wifi_manager = Template(wifi_manager_page)
    data = combobox_populate(wifi_list)

    return template_wifi_manager.render(ssid_list=data)
