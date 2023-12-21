<template>
  <div>
    <button @click="rs">高斯消元法变为行阶梯形矩阵</button>
    <button @click="cs">高斯消元法变为列阶梯形矩阵</button>
    <button @click="srs">高斯消元法变成行最简形阶梯形矩阵</button>
    <button @click="scs">高斯消元法变成列最简形阶梯形矩阵</button>
    <button @click="gas">高斯消元法求解行列式</button>
    <button @click="inv">初等变换法计算输入矩阵的逆矩阵</button>
    <button @click="lu">使用初等变换法实现了LU分解</button>
    <button @click="ldu">使用初等变换法实现了LDU分解</button>
    <button @click="crt">使用初等变换法实现了Crout分解</button>
    <button @click="qr">实现了QR分解</button>
    <button @click="adj">计算输入矩阵的伴随矩阵</button>
    <button @click="smt">Schmidt正交化过程</button>
    <button @click="egv">对某个矩阵求特征值</button>
    <button @click="egm">求某个矩阵对应的特征多项式</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    rs() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/rs")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    cs() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/cs")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    srs() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/srs")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    scs() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/scs")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    gas() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/gas")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    inv() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/inv")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    lu() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/lu")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    ldu() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/ldu")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    crt() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/crt")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    qr() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/qr")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    adj() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/adj")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    smt() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/smt")
        .then((response) => {
          console.log("命令执行结果:", response.data);
        })
        .catch((error) => {
          console.error("请求失败:", error);
        });
    },
    egv() {
      // 发起对后端的API请求
      axios
        .get("http://10.250.136.172:49154/api/data-matrix/egv")
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
