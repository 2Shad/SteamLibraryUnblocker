#!/bin/bash
# Allow all IP ranges for Steam
iptables -D OUTPUT -p tcp --dport 27036:27037 -m iprange --dst-range 0.0.0.0-191.254.254.254 -j DROP
iptables -D OUTPUT -p tcp --dport 27036:27037 -m iprange --dst-range 192.168.2.250-254.254.254.253 -j DROP