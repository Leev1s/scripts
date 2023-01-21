import argparse
from pypushdeer import PushDeer
import base64

## argparse
parser = argparse.ArgumentParser()
parser.add_argument('--message','-m',help='your message',default='⚠️')
parser.add_argument('--desp','-d',help='desp message',default='⚠️')
args = parser.parse_args()

## get key
keyfile = open('/root/pushkey')
key = keyfile.read()
key = key[:-1]

pushdeer = PushDeer(pushkey=key)
pushdeer.send_markdown(args.message,desp=args.desp)
