#!/usr/bin/env python3

import argparse
import sys
import socket


def clear_console_line():
	sys.stdout.write("\033[K")  # clear line


parser = argparse.ArgumentParser(description='Scan a host.')

parser.add_argument('--host', required=True)
parser.add_argument('--min-port', default=0, type=int)
parser.add_argument('--max-port', default=65535, type=int)

args = parser.parse_args()

host = args.host
min_port = args.min_port
max_port = args.max_port

print("Scanning {}".format(host))

try:
	for port in range(min_port, max_port):

		clear_console_line()
		print('Scanning port {:s}:{:d}'.format(host, port), end="\r", flush=True)

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)  # float
		result = sock.connect_ex((host, port))  # error code

		if result == 0:
			clear_console_line()
			print("Port {} OPEN".format(port), flush=True)

		sock.close()

except socket.gaierror:
	print("Could not resolve {}".format(host))

except socket.error:
	print("Could not connect to {}".format(host))
