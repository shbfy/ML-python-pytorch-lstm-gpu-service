from __future__ import unicode_literals

import falcon
import apiserver
from wsgiref import simple_server


class StandaloneApplication:

    def __init__(self, api):
        self.application = api
        apiserver.config(api)
        super(StandaloneApplication, self).__init__()

    def load(self):
        return self.application


if __name__ == '__main__':
    app = StandaloneApplication(falcon.API())
    httpd = simple_server.make_server('0.0.0.0', 8080, app.application)  # nosec
    httpd.serve_forever()
