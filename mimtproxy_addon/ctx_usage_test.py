from mitmproxy import ctx

# 并不能正常运行，hint指定类型也仅仅是指定而已。并没有产生变量。
ctx.log.info("1234")
