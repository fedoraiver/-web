<template>
  <div id="app">
    <!-- top bar -->
    <div
      style="
        height: 60px;
        line-height: 60px;
        background-color: white;
        margin-bottom: 2px;
      "
    >
      <img
        src="@/assets/logo.png"
        alt=""
        style="width: 40px; position: relative; top: 16px; left: 20px"
      />
      <span style="margin-left: 24px; font-size: 24px">矩阵计算</span>
    </div>

    <!-- side bar and main body -->
    <div style="display: flex">
      <!-- side bar -->
      <div
        style="
          width: 200px;
          min-height: calc(100vh - 62px);
          overflow: hidden;
          margin-right: 2px;
          background-color: white;
        "
      >
        <el-menu :default-active="$router.path" router class="el-menu-demo">
          <el-menu-item index="/">首页</el-menu-item>
          <el-menu-item index="/result">结果</el-menu-item>
          <el-submenu>
            <template slot="title">其他</template>
            <el-menu-item index="/about">帮助</el-menu-item>
            <el-menu-item index="/people">制作人员</el-menu-item>
          </el-submenu>
        </el-menu>
      </div>

      <!-- main body -->
      <div style="flex: 1; background-color: white">
        <router-view />
      </div>
    </div>
  </div>
</template>
