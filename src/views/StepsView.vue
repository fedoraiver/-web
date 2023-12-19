<template>
  <div class="matrix-container">
    <h1>步骤展示</h1>
    <table>
      <tr v-for="(row, rowIndex) in matrix" :key="rowIndex">
        <td v-for="(cell, colIndex) in row" :key="colIndex">{{ cell }}</td>
      </tr>
    </table>
  </div>
</template>

<script src="../steps.js"></script>

<style>
/* 可以添加样式，根据需要自定义样式 */
.matrix-container {
  text-align: center;
}

table {
  border-collapse: collapse;
  margin-top: 10px;
}

table,
th,
td {
  border: 1px solid black;
}

th,
td {
  padding: 10px;
  text-align: center;
}
</style>
