#!/bin/bash

#Two ideas to create noise. First is long download with wget. second is continuous connection.

curl --limit-rate 10K "https://speed.hetzner.de/100MB.bin" -o /dev/null
#nc -l -p 1234 > /dev/null

wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
wget www.google.com &
