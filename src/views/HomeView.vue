<template>
  <div>
    <form
      id="uploadForm"
      enctype="multipart/form-data"
      action="http://localhost:49154/upload"
      method="post"
    >
      <input type="file" name="imageFile" id="imageFile" />
      <button type="submit">上传图片</button>
    </form>
    <img src="../../uploads/1.png" />
    <img src="../../uploads/2.png" />
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>
