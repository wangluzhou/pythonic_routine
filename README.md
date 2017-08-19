# Introduction

一起来写作写gitbook吧~

规则：
## 一级目录按照周数来，符合大家的学习顺序。
## 内容分类：

  1. 开智卡片内容：完成卡片的抄录和整理，特别是对卡片里链接里的内容进行整理
  2. **[环境]**Python三座大山之一：环境。讲述你遇到的一些环境配置的问题。
  3. **[语言]**Python三座大山之一：Python语言。讲述你碰到的一些Python本身的问题。
  4. **[包]**Python三座大山之一：Python包。讲述你用到一些包信息，比如爬虫包，科学计算包等等。
  5. [作业]作业交流

## 卡片内容是我们的主线，直接写在每一周的README.md文件内。
## 如果要分享三座大山里面的相关内容，请直接在对应的weekX里面插入新的md文件，并且在文件summary.md里面进行补充，加入一个二级目录。
比如我想加入一些gitbook的使用心得。那么我需要在summary.md文件加入如下[环境.gitbook使用]，其中的环境表示这块内容属于环境子内容：
```
* [Introduction](README.md)
* [第0周](week0/README.md)
  * [环境.gitbook使用](week0/gitbook.md)
* [第二章](week1/README.md)

```

然后在week0下面添加gitbook.md
