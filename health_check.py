#!/usr/bin/env python3

import psutil
import shutil
import socket
import os
import emails

def cpu_check():
    usage = psutil.cpu_percent(2)
    return usage > 80

def disk_usage():
    # change("c:") for ("/") in linux
    usage = shutil.disk_usage("c:")
    usage_percent = (usage[1] * 100) / usage[0]
    return usage_percent > 80

def memory_usage():
    usage = psutil.virtual_memory()
    free_mb = usage[1] / 1000 / 1000
    return free_mb < 500

def resolve_localhost():
    localhost = socket.gethostbyname("localhost")
    return localhost != "127.0.0.1"

def send_mail(sender, recipient, subject, body):
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send(message)


sender = "automation@example.com"
# "os.environ.get("USER")" only in linux
recipient = str(os.environ.get("USER")) + "@example.com"
body = "Please check your system and resolve the issue as soon as possible."

if cpu_check():
    send_mail(sender, recipient, "Error - CPU usage is over 80%", body)

if disk_usage():
    send_mail(sender, recipient, "Error - Available disk space is less than 20%", body)

if memory_usage():
    send_mail(sender, recipient, "Error - Available memory is less than 500MB", body)

if resolve_localhost():
    send_mail(sender, recipient, "Error - localhost cannot be resolved to 127.0.0.1", body)