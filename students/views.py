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
line_bot_api = LineBotApi('/IiYT15vRmdIlPWIb25zd1OL06vPWpNpOAvhWq7dQoq6IKKO0RwkRyU0NtkCP8puDxgrDYxdHtCyfEL9RVOh3ttvxtix7ulyRIKfqqIRcFOnp2Cu/9sdebfZyEu6x+6jUWNOWZtaJ95PQ+m0j4nWSwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('77420eff1299232cf4314b8aebb2a960')

line_bot_api.push_message('U366d13dc7ad1cb2324e08671ba0302c8', TextSendMessage(text='你可以開始了'))
