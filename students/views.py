from django.shortcuts import render
from studentsapp.models import student
from django.http import HttpResponse

import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler

logger = logging.getLogger("django")

"""
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)
"""
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('oFIGY3vVcqShlfPRLoEiL9Ae9i8AdegpgsQuthXtELpmtWUAlogA9GRtQh7qqjrl767E+JnlWJcSIaPsHjDvX1uodUvso9TDlPkMu8A0eCn0PpUL954SSOLlfO5ZyRsCbxjKS8miIZjwYy5693pJlAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('cd9af7d9501307934f631780d224ea0e')

line_bot_api.push_message('Uff684bec73afec37e18f1a1a56d66101', TextSendMessage(text='你可以開始了'))
