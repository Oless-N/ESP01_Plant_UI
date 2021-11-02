from microWebSrv import MicroWebSrv


def status_box():
    name = 'name'
    status = 'status'
    response = '<p><div><a>%s</a></div> <div><a></a>%s</div></p>' % (
        name, status)
    return response


def content_page(path, *args, **kwargs):
    with open(path) as page:
        return page


@MicroWebSrv.route('/')
def _index(httpClient, httpResponse):
    httpResponse.WriteResponseOk(
        headers=None,
        contentType="text/html",
        contentCharset="UTF-8",
        content=content_page('templates/index.html'),
    )


@MicroWebSrv.route('/setup')
def _setup(httpClient, httpResponse):
    httpResponse.WriteResponseOk(
        headers=None,
        contentType="text/html",
        contentCharset="UTF-8",
        content=content_page('templates/setup.html'),
    )


@MicroWebSrv.route('/setting')
def _setting(httpClient, httpResponse):
    httpResponse.WriteResponseOk(
        headers=None,
        contentType="text/html",
        contentCharset="UTF-8",
        content=content_page('templates/settings.html'),
    )


def main():
    mws = MicroWebSrv()  # TCP port 80 and files in /flash/www
    mws.Start(threaded=True)  # Starts server in a new thread
