const express = require('express');
const multer = require('multer'); // 用于处理文件上传的中间件
const path = require('path');

const app = express();
const port = 3000; // 你可以根据需要更改端口号

// 配置文件上传的存储位置和文件名
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/'); // 存储文件的目录，确保该目录存在
  },
  filename: (req, file, cb) => {
    const ext = path.extname(file.originalname);
    cb(null, 'uploaded_' + Date.now() + ext); // 为上传的文件生成唯一的文件名
  }
});

const upload = multer({ storage: storage });

// 设置静态文件目录，以便可以访问上传的文件
app.use(express.static('public'));

// 处理文件上传的 POST 请求
app.post('/upload', upload.single('imageFile'), (req, res) => {
  if (req.file) {
    // 文件上传成功
    res.json({ message: '文件上传成功' });
  } else {
    // 没有选择文件或上传失败
    res.status(400).json({ message: '文件上传失败' });
  }
});

app.listen(port, () => {
  console.log(`服务器运行在 http://localhost:${port}`);
});
