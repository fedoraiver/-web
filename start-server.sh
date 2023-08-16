#!/bin/bash

# 运行 npm run server
npm run serve &

# 等待一段时间，确保服务器已经启动
sleep 5

# 运行 node server.js
node server.js

