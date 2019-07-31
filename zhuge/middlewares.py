# -*- coding: utf-8 -*-
import random


class UserAgentDownloadMiddleware(object):
    USER_AGENTS = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:55.0) Gecko/20100101 Firefox/55.0",

    ]

    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent

