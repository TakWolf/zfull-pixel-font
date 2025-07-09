> [!WARNING]
> 
> 本字体并非公有领域，您在使用时，请务必谨慎考量并自负版权风险。
> 
> 如果您正在寻找可以免费商用的开源中文像素字体，请尝试以下项目：
>
> - [方舟像素字体](https://github.com/TakWolf/ark-pixel-font)
> - [缝合像素字体](https://github.com/TakWolf/fusion-pixel-font)

# Zfull 像素字体

[![Releases](https://img.shields.io/github/v/release/TakWolf/zfull-pixel-font)](https://github.com/TakWolf/zfull-pixel-font/releases)

过去曾在网络流行的点阵字体。

原始字体的点阵数据基于内嵌的 [OpenType - EBDT](https://learn.microsoft.com/en-us/typography/opentype/spec/ebdt) 数据格式，其点阵字形在现代系统中使用起来不太方便。

这个项目进行了如下工作：

1. 将原始字体中的每个点阵尺寸各拆分为一个独立字体。
2. 将原始的点阵数据转换为轮廓字形。

## 程序依赖

- [Pixel Font Builder](https://github.com/TakWolf/pixel-font-builder)
- [FontTools](https://github.com/fonttools/fonttools)
- [Loguru](https://github.com/Delgan/loguru)
- [Cyclopts](https://github.com/BrianPugh/cyclopts)
- [Vue.js](https://cn.vuejs.org)

## 许可证

### 字体

原始字体来源于 [zfull-for-yosemite](https://github.com/andot/zfull-for-yosemite/tree/master/fonts)，作者以及版权不明。

因此，本字体并非公有领域，您在使用时，请务必谨慎考量并自负版权风险。

字体在转换的过程中，保留了原始字体的元信息。

### 构建程序

使用 [「MIT 许可证」](LICENSE-MIT) 授权。
