<!-- toc -->
# gitbook
[参考教程](http://www.chengweiyang.cn/gitbook/basic-usage/README.html)
需要注意的是，我们正常安装的其实是gitbook-cli,如果只是安装gitbook的话，gitbook的命令行是无效的。也就是输入：
```
npm install -g gitbook-cli
```
gitbook可能支持两级目录。
推荐在编写gitbook的时候始终打开gitbook serve,这样一来，在文件的编写修改过程中，每一次保存文件，gitbook serve都会自动编译，所以可以持续通过浏览器查看最新的书籍效果。非常酷炫！！！

整体流程就按照上面参考教程的指示操作就行。但是需要注意的是，我们的最终目的都是希望能有自己的书籍域名可以公开发布我们的书籍。因此最后必然需要同步到github通过gitpage进行发布。

另外gitbook自带搜索引擎，你说酷不酷！

GitBook.com 为每本书籍都创建了一个 Git 项目，并且使用这个 Git 项目来管理书籍源码（注意：这里的源码是指所有用户提交的内容）。正如在 编辑书籍 中介绍的那样，我们可以通过向书籍的 Git 项目提交内容来更新书籍。

另外，GitBook.com 还可以集成 GitHub，所以用户可以将书籍的源码通过 GitHub 上的项目来管理，这样可以使用 GitHub 带来的各种优点，例如：

其它用户可以 fork
用户可以点赞，获得更新提醒
用户可以贡献自己的内容GitBook.com 为每本书籍都创建了一个 Git 项目，并且使用这个 Git 项目来管理书籍源码（注意：这里的源码是指所有用户提交的内容）。正如在 [编辑书籍](http://www.chengweiyang.cn/edit.html) 中介绍的那样，我们可以通过向书籍的 Git 项目提交内容来更新书籍。

另外，GitBook.com 还可以集成 [GitHub](https://github.com/)，所以用户可以将书籍的源码通过 GitHub 上的项目来管理，这样可以使用 GitHub 带来的各种优点，例如：

*   其它用户可以 fork
*   用户可以点赞，获得更新提醒
*   用户可以贡献自己的内容



[关于如何将本地的gitbook上传到gitbook](https://help.gitbook.com/books/how-can-i-use-git.html)
但是我们其实并不需要这么做，只要上传到github，然后将github这个库和gitbook的某本书关联一下就行了，唯一要注意的就是这个库的文件树格式要遵循gitbook的要求。所以本地的环境维持github的环境就好，减少踩坑的概率。
如果你的gitbook找不到你在github的库，你就需要去github上设置一下。
在github右上角点击setting,进入设置页面，在左下角做到installed Github apps，点击进去，然后点击gitbook，在repository access设置All repositories即可。

## 添加.gitignore添加一些不需要上传的文件


## 如何将gitbook发布到自己的域名的子域名上
将gitbook挂在到自己的子域名一定是一个非常有趣的问题。

## gitbook如何安装插件？
似乎有两种安装方法:
[方法一](https://plugins.gitbook.com/plugin/search-pro)
[方法二](http://www.css88.com/archives/6622)
有空研究一下


## gitbook editor只支持https并不支持ssh
我们需要将gitbook远程库的连接方式改成https

## gitbook插件介绍
[资源1](http://zhaoda.net/2015/11/09/gitbook-plugins/)
[gitbook官网资源](https://plugins.gitbook.com/browse?page=1)

## gitbook动态更新问题
当我们输入`gitbook serve`的时候，一旦更新了文件，就会报错，导致gitbook serve停止工作。
```
Restart after change in file SUMMARY.md
Stopping server
Error: EPERM: operation not permitted, mkdir 'C:\Users\cleopatra\Desktop\abum_code\_book'
```
github上的[creatop-john](https://github.com/GitbookIO/gitbook/issues/1379)提出了一个办法,有时会有效：
1. gitbook serve
2. delete _book folder once
3. now each time you change the md file, the server will stop and start over again and again

## 注意：gitbook editor打开的时候不要直接选择云端的gitbook库，而是要选择本地的gitbook库，这样gitbook和atom就可以实现本地的同步。

## 如何将gitbook发布到个人域名的子域名下
[参考资料](https://yuzeshan.gitbooks.io/gitbook-studying/content/publish/gitpages.html)
