lsof -i :49153 | grep "node" | awk '{print $2}' | xargs kill
lsof -i :49154 | grep "node" | awk '{print $2}' | xargs kill
