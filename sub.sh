#!/usr/bin/zsh
echo $(curl -s "https://air.fq233.cf/api/v1/client/subscribe?token=09f3dc505721ba13bc3d3f213bfee261") > /root/files/air_sub
decode_sub=$(base64 -d /root/files/air_sub)
python3 /root/scripts/wecom_push.py -m "${decode_sub}"
python3 /root/scripts/warn.py -m 已投递订阅链接