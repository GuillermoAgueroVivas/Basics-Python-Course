#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'BIG MAMA'
pw = ''
auth = False
count = 0
max_attempts = 5

while pw != secret:
    count += 1
    if count > max_attempts: break
    pw = input(f"Attempt number {count} : What's the secret word? ").upper()
else:
    auth = True

print('Authorized') if auth else "Calling The FBI..."


