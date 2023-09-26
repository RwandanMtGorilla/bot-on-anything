import requests
from config import model_conf
from common import log

class mymodel:
    def __init__(self):
        self.api_url = 'http://localhost:5000/chat'
        log.info("[CHATGPT] Initialized")

    def reply(self, query, context=None):
        if context.get('type', 'TEXT') == 'TEXT':
            log.info("[CHATGPT] query={}".format(query))
            return self.reply_text(query)

    def reply_text(self, query):
        try:
            response = requests.post(self.api_url, json={"query": query})
            response_json = response.json()
            reply_content = response_json.get('answer', '未能获取答案')
            log.info("[CHATGPT] reply={}".format(reply_content))
            return reply_content

        except requests.exceptions.RequestException as e:
            log.warn(e)
            return "我连接不到网络，请稍后重试"

        except Exception as e:
            log.exception(e)
            return "请再问我一次吧"
