export default {
  data() {
    return {
      matrix: [],
    };
  },
  mounted() {
    // 发起请求获取数据
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch('http://10.250.136.172:49154/api/data-matrix')
        .then(response => response.json())
        .then(data => {
          // 更新前端界面的 matrix 数据
          this.matrix = data.dataMatrix;
        })
        .catch(error => console.error('Error:', error));
    },
  },
};
