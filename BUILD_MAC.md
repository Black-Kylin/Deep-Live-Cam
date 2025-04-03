# Mac应用打包指南

本指南将帮助你将Deep-Live-Cam打包成一个独立的Mac应用程序。

## 准备工作

1. 确保你的系统已安装Python 3.10和pip
2. 安装虚拟环境（推荐）：
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   ```

## 安装依赖

1. 安装项目依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 安装打包工具：
   ```bash
   pip install py2app
   ```

## 准备图标

1. 将SVG图标转换为ICNS格式：
   ```bash
   # 创建临时iconset目录
   mkdir media/icon.iconset
   
   # 使用sips命令将SVG转换为不同尺寸的PNG
   sips -s format png media/icon.svg --out media/icon.iconset/icon_16x16.png -z 16 16
   sips -s format png media/icon.svg --out media/icon.iconset/icon_32x32.png -z 32 32
   sips -s format png media/icon.svg --out media/icon.iconset/icon_64x64.png -z 64 64
   sips -s format png media/icon.svg --out media/icon.iconset/icon_128x128.png -z 128 128
   sips -s format png media/icon.svg --out media/icon.iconset/icon_256x256.png -z 256 256
   sips -s format png media/icon.svg --out media/icon.iconset/icon_512x512.png -z 512 512
   
   # 创建2x版本
   cp media/icon.iconset/icon_16x16.png media/icon.iconset/icon_16x16@2x.png
   cp media/icon.iconset/icon_32x32.png media/icon.iconset/icon_32x32@2x.png
   cp media/icon.iconset/icon_64x64.png media/icon.iconset/icon_64x64@2x.png
   cp media/icon.iconset/icon_128x128.png media/icon.iconset/icon_128x128@2x.png
   cp media/icon.iconset/icon_256x256.png media/icon.iconset/icon_256x256@2x.png
   cp media/icon.iconset/icon_512x512.png media/icon.iconset/icon_512x512@2x.png
   
   # 生成icns文件
   iconutil -c icns media/icon.iconset
   
   # 清理临时文件
   rm -rf media/icon.iconset
   ```

## 打包应用

1. 清理旧的构建文件（如果存在）：
   ```bash
   rm -rf build dist
   ```

2. 执行打包命令：
   ```bash
   python setup.py py2app
   ```

打包完成后，你可以在`dist`目录下找到`Deep-Live-Cam.app`。

## 注意事项

1. 确保所有模型文件都已下载并放置在正确的位置
2. 打包过程可能需要几分钟时间
3. 生成的应用体积可能较大，这是正常的，因为它包含了所有必要的依赖
4. 首次运行可能需要在系统偏好设置中允许来自身份不明开发者的应用