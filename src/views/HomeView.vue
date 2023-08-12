<template>
  <div>
    <form id="uploadForm" enctype="multipart/form-data">
      <input type="file" name="imageFile" id="imageFile" />
      <button type="submit">上传图片</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>
