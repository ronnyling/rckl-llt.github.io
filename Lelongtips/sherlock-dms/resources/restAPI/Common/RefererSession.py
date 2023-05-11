import requests


class RefererSession(requests.Session):
    def rebuild_auth(self, prepared_request, response):
        super().rebuild_auth(prepared_request, response)
        prepared_request.headers["Referer"] = response.url

    def get(self, url, **kwargs):
        self.headers.update((k, v) for k, v in self.cookies.items())
        return super().get(url, headers=self.headers, **kwargs)

    def post(self, url, **kwargs):
        self.headers.update((k, v) for k, v in self.cookies.items())
        return super().post(url, headers=self.headers, **kwargs)
