<template>
  <div>
    <form
      id="uploadForm"
      enctype="multipart/form-data"
      action="http://10.250.136.172:49154/upload"
      method="post"
    >
      <input type="file" name="imageFile" id="imageFile" />
      <button type="submit">上传图片</button>
    </form>
    <a href="http://10.250.136.172:49154/download" download="结果.txt"
      >点击这里下载结果</a
    >
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>
