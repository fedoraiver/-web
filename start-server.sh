#!/bin/bash

# 运行 npm run server
PORT=49153 npm run serve --prefix /Users/tangdanyu/Desktop/HITsz/大一立项/project/vue &

# 等待一段时间，确保服务器已经启动
sleep 5

# 运行 node server.js
node /Users/tangdanyu/Desktop/HITsz/大一立项/project/vue/server.js

