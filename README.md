# picture_tag_tools
it is a pyQt tools to tag picuture to positive one and negative examples which could be used in picture manual  tagging


this is just a based pic tag tools. Next feature need will be added are：
1. zoom in and zoom out  
2. show the previous pic   
3. Drag the image  


2.0 标注工具
1. 指定标注目录
2. 可以指定输出目录，默认就是在标注目录下建一个输出文件夹
3. 只处理一张图片有一个类别的情况
4. 每个类别都是一个标签
5. 点击标签之后，直接保存结果，并且跳转到下一张图片
6. 输出用xml输出，主要内容有：1. 原始图片路径，标注的类别
7. 可以加载输出内容，通过解析哪些已经标注了，来过滤已经标注的图片
