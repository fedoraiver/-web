const express = require('express');
const cors = require('cors'); // 引入 cors 中间件
const multer = require('multer');
const path = require('path');

const app = express();
const port = 49154;
app.use(cors()); // 使用 cors 中间件，允许跨域请求
// 配置文件上传的存储位置和文件名
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/'); // 存储文件的目录，确保该目录存在
  },
  filename: (req, file, cb) => {
    cb(null, '1.png' ); // 为上传的文件生成唯一的文件名
  }
});

const fileFilter = (req, file, cb) => {
  if (file.mimetype === 'image/png' || file.mimetype === 'image/jpeg' || file.mimetype === 'image/jpg' ) {
    cb(null, true);
  } else {
    cb(new Error('只允许上传图片'));
  }
};


const upload = multer({ storage: storage, fileFilter: fileFilter });

// 设置静态文件目录，以便可以访问上传的文件
app.use(express.static('public'));

// 处理文件上传的 POST 请求
app.post('/upload', upload.single('imageFile'), (req, res) => {
  if (req.file) {
    // 文件上传成功
    res.redirect('http://192.168.31.89:49153/');
  } else {
    // 没有选择文件或上传失败
    res.status(400).json({ message: '文件上传失败' });
  }
});

app.listen(port, () => {
  console.log(`服务器运行在 http://localhost:${port}`);
});



