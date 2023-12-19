<template>
  <div>
    <button @click="handleButtonClick">矩阵求逆</button>
  </div>
</template>

<script>
export default {
  methods: {
    handleButtonClick() {
      // 你可以在这里设置需要传递给后端的信息
      const messageToSend = "Hello from frontend!";

      // 发送POST请求给后端
      fetch("", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: messageToSend }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("后端返回的数据:", data);
          // 在这里可以处理后端返回的数据
        })
        .catch((error) => {
          console.error("请求错误:", error);
        });
    },
  },
};
</script>
