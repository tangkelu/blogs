#!/bin/bash
# 后台爬虫脚本

cd /code/blogs

# 运行改进的爬虫脚本
nohup python3 crawl_top_keywords_blogs_v2.py > /tmp/crawl_top_keywords.log 2>&1 &

echo "Crawler started with PID: $!"
