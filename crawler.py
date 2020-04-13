#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exception.ConnectionError:
        pass


target_url = "google.com"

with open("subdomains.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)
