<template>
  <div>
    <button @click="executeCommand">矩阵求逆</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    executeCommand() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/inverse")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
  },
};
</script>
