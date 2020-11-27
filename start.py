# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
from scrapy.utils.python import garbage_collect
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# import robotparser
import os
import sys
import scrapy.spiderloader
import scrapy.statscollectors
import scrapy.logformatter
import scrapy.dupefilters
import scrapy.squeues

import scrapy.extensions.spiderstate
import scrapy.extensions.corestats
import scrapy.extensions.telnet
import scrapy.extensions.logstats
import scrapy.extensions.memusage
import scrapy.extensions.memdebug
import scrapy.extensions.feedexport
import scrapy.extensions.closespider
import scrapy.extensions.debug
import scrapy.extensions.httpcache
import scrapy.extensions.statsmailer
import scrapy.extensions.throttle

import scrapy.core.scheduler
import scrapy.core.engine
import scrapy.core.scraper
import scrapy.core.spidermw
import scrapy.core.downloader

import scrapy.downloadermiddlewares.stats
import scrapy.downloadermiddlewares.httpcache
import scrapy.downloadermiddlewares.cookies
import scrapy.downloadermiddlewares.useragent
import scrapy.downloadermiddlewares.httpproxy
import scrapy.downloadermiddlewares.ajaxcrawl
import scrapy.downloadermiddlewares.chunked
import scrapy.downloadermiddlewares.decompression
import scrapy.downloadermiddlewares.defaultheaders
import scrapy.downloadermiddlewares.downloadtimeout
import scrapy.downloadermiddlewares.httpauth
import scrapy.downloadermiddlewares.httpcompression
import scrapy.downloadermiddlewares.redirect
import scrapy.downloadermiddlewares.retry
import scrapy.downloadermiddlewares.robotstxt

import scrapy.spidermiddlewares.depth
import scrapy.spidermiddlewares.httperror
import scrapy.spidermiddlewares.offsite
import scrapy.spidermiddlewares.referer
import scrapy.spidermiddlewares.urllength

import scrapy.pipelines

import scrapy.core.downloader.handlers.http
import scrapy.core.downloader.contextfactory

import scrapy.core.downloader.handlers.file
import scrapy.core.downloader.handlers.ftp
import scrapy.core.downloader.handlers.datauri
import scrapy.core.downloader.handlers.s3

print(sys.path[0])

print(sys.argv[0])

print(os.path.dirname(os.path.realpath(sys.executable)))

print(os.path.dirname(os.path.realpath(sys.argv[0])))
cfg = os.path.join(os.path.split(sys.path[0])[0], "scrapy.cfg")
print(cfg)
input()

process = CrawlerProcess(get_project_settings())

# 参数1：爬虫名 参数2：域名

process.crawl('lsprobat', domain='qql6k.com')
process.start()  # the script will block here until the crawling is finished
input()