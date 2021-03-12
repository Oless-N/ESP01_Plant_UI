from app.setup_ui import ssid_populate


def test_combobox_populate(get_list, tag_tools):
    expected = '<option>networt</option><option>ssid</option><option>wifi</option>'

    res = tag_tools.combobox_populate(get_list)

    assert expected == res


def test_ssid_populate(get_list, ssid_page):
    expected = """
    <html>
        <head>
            <meta charset="UTF-8">
            <link href="img/favicon.ico" rel="icon" type="image/png"/>
            <link rel="stylesheet" type="text/css" href="style.css">
            <title>Plant WiFi Setup</title>
        </head>
        <body class="container">
        <div class="header">
            Wi-Fi Plant Setup
        </div>
        <div class="body_box">
        
            <div class="body">
                <div class="ssids">
                 Networks:
                <select class="select_ssid"><option>networt</option><option>ssid</option><option>wifi</option></select>
            </div>
            </div>
        
            <div class="body">
                <div class="input_password">
                    Password: <input name="password" type="password" class="input_line"/>
                </div>
            </div>
        
            <div class="body">
                <form action="configure" method="post">
                    <button class="button" type="submit" value="Submit">
                        Connect
                    </button>
                </form>
        
        
                <form action="index.html">
                    <button class="button" type="submit" value="Home">Home</button>
                </form>
            </div>
        </div>
        
        </body>
        </html>
    """
    res = ssid_populate(get_list, ssid_page)

    print('>>>>', res)
    assert res == expected
