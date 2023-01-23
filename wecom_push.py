# -*- encoding: utf-8 -*-
'''
@File    :   wecom_push.py
@Time    :   2023/01/20 15:05:17
@Author  :   Lev1s
@Version :   1.0
@Contact :   Lev1sStudio.cn@gmail.com
@PW      :   http://Lev1s.cn
@Github  :   https://github.com/o0Lev1s0o

'''
print('''
    __             ___        _____ __            ___     
   / /   ___ _   _<  /____   / ___// /___  ______/ (_)___ 
  / /   / _ \ | / / / ___/   \__ \/ __/ / / / __  / / __ \\
 / /___/  __/ |/ / (__  )   ___/ / /_/ /_/ / /_/ / / /_/ /
/_____/\___/|___/_/____/   /____/\__/\__,_/\__,_/_/\____/
''')
# here put the import lib
import sys
sys.path.append("/root/scripts")

from datetime import datetime
from datetime import timedelta
from datetime import timezone

import wecom
import argparse

## argparse
parser = argparse.ArgumentParser()
parser.add_argument('--message','-m',help='your message',default='⚠️')
parser.add_argument('--time','-t',help='show instant time or not',action="store_true")
args = parser.parse_args()

CID = "ww996e2e704963f44b"
APPID = "1000002"
SECRET = "sHaEQCr8b9X1aWG9--ldiiOpAmTMDFrZ15oU_rhMPXE"
if args.time:
    SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',)

    # 北京时间
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ)
    time = beijing_now.strftime("「%Y-%m-%d %H:%M:%S」")
    ret = wecom.send_to_wecom(time+"\r\n"+args.message, CID, APPID, SECRET)
else:
    ret = wecom.send_to_wecom(args.message, CID, APPID, SECRET)

print( ret )