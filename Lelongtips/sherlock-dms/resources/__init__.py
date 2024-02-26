import sys
import os
from resources.Common import Common

COMMON_KEY = Common()

sys.path.append(os.path.abspath('.'))
PROTOCOL = 'https://'
LLT_URL = 'www.lelongtips.com.my/search?keyword=&property_type%5B%5D=1&property_type%5B%5D=4&property_type%5B%5D=5&property_type%5B%5D=3&state=kl_sel&min_price=150000&max_price=1000000&min_size=&max_size=&sort=price-asc&page=' #&page=[1-300]'\n",
LLT_TOKEN = '2a2528f1fe702b30de4754240bfbf1f24a50eddb5928cc5bd0eb30c21ccc22f05'
TEST_URL = 'www.lelongtips.com.my/search?keyword=&property_type%5B%5D=1&property_type%5B%5D=4&property_type%5B%5D=5&property_type%5B%5D=3&state=kl_sel&min_price=150000&max_price=1000000&min_size=&max_size=&sort=price-asc&page=1' #&page=[1-300]'\n",

# APP_URL, COMMON_KEY, LLT_URL, LLT_TOKEN, GMAPS_TOKEN, PHONE_ID, TOKEN, NUMBER, \
#     MESSAGE, TEST_URL