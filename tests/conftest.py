import pytest

from app.setup_ui import PopulateTools


@pytest.fixture
def get_list():
    return ['ssid', 'networt', 'wifi']


@pytest.fixture
def ssid_page():
    return """
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
                <select class="select_ssid">{{ssid_list}}</select>
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


@pytest.fixture
def tag_tools():
    return PopulateTools()
