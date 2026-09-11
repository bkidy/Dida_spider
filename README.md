# Dida_spider

2019 年的实验代码：通过 mitmproxy 抓包嘀嗒拼车客户端 App，把拼车 / 顺风车相关接口的返回内容落到本地 MongoDB。

## 组成

| 文件 | 作用 |
| --- | --- |
| `didas-f.py` | mitmproxy 脚本（`response` 钩子），匹配 App 的若干接口 URL 并解析 JSON |
| `handle_db.py` | MongoDB 写入封装（`spring` 库，按 `id` 做 upsert 去重） |
| `didaspring/main.py` | Scrapy 爬虫 |
| `tuhu.py` | 途虎相关抓取脚本 |

## 运行方式（2019 年的环境：Python 3.7）

```bash
pip install mitmproxy pymongo scrapy
mitmdump -s didas-f.py
```

App 接口地址会不定期变化，脚本里每个接口都留了两个候选 URL。

## 维护状态

**已停止维护。** 相关接口地址与客户端协议早已变更，本仓库仅作当年的抓包 / 落库思路参考，请勿用于任何未经授权的数据获取。
