export default {
    data() {
      return {
        matrix: [],
      };
    },
    mounted() {
      this.generateMatrix(4, 3); // 传入矩阵的行数和列数
    },
    methods: {
      generateMatrix(numRows, numCols) {
        for (let i = 0; i < numRows; i++) {
          const row = [];
          for (let j = 0; j < numCols; j++) {
            // 假设矩阵元素为随机数
            row.push(1);
          }
          this.matrix.push(row);
        }
      },
    },
  };