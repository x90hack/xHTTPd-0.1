#!/usr/bin/python
# -*- coding: utf-8 -*-

# 크롤러는 페이지에 들어 있는 데이터인 엔터티 정보를 모두 긁어서와서
# 2단계 또는 3단계까지 정보를 탐색하는 프로그램을 말하고
# 파이썬의 뷰티풀 수프 모듈로 잘 지원하고 있다

import requests
from bs4 import BeautifulSoup

domain = 'https://www.google.com'

res = requests.get('https://www.google.com/search?q=%EC%A0%95%EA%B2%BD%EC%A3%BC&sxsrf=AOaemvJvBPUlvNRi2Yjkz4hmUfBNKk0YAw%3A1642717385998&source=hp&ei=yeDpYaDVOq3fmAWf67n4Cg&iflsig=ALs-wAMAAAAAYenu2f7rE20n6aTn_ChaF7e_lJVkp0CE&ved=0ahUKEwjg3YaSr8H1AhWtL6YKHZ91Dq8Q4dUDCAk&uact=5&oq=%EC%A0%95%EA%B2%BD%EC%A3%BC&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyCgguEIAEEIcCEBQyBQgAEIAEMgoILhCABBCHAhAUMgUIABCABDIFCAAQgAQyBAgAEB4yBAgAEB4yBAgAEB46BwgjEOoCECc6BAgAEEM6CwgAEIAEELEDEIMBOggILhCABBCxAzoRCC4QgAQQsQMQgwEQxwEQowI6BAguEAM6BQguEIAEUKwGWMcQYPkRaAJwAHgAgAGoAYgB6QiSAQMwLjmYAQCgAQGwAQo&sclient=gws-wiz')

# print(res)

soup = BeautifulSoup(res.content, 'html.parser')

arr1 = []

i = 0

# 인덱스 페이지 파싱
for link in soup.findAll('a'):
        href = link['href']
        if 'https://' not in href:
                arr1.append(domain+href)
        else:
                if '/' in href[0]:
                        arr1.append(domain+href)
                else:
                        arr1.append(href)

        value = link.get_text()
        print(value+': '+arr1[i])
        i = i + 1

print('-----[1]-----\n')
arr2 = []

i = 0

max_count = 5

# 1, 2, ... 링크로 크롤링 파싱.

for a in [1, 2]:
        print('--[' + str(a) + ']--\n')

        req = requests.get(arr1[a])
        html = req.content
        soup1 = BeautifulSoup(html, 'html.parser')

        i = 0

        for link in soup1.findAll('a'):
                if i < max_count:
                        i = i + 1
                        if link['href'][0] == '/':
                                print(link.get_text() + '= ' + domain + link['href'])
                        else:
                                print(link.get_text() + '= ' + link['href'])
                else:
                        break
