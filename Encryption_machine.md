# Encryption_machine
It is merely a encryption_machine.

## 中文

### 关于release中app打不开的解决方案
​    右键文件，点击「显示包内容」，打开「macos」文件夹，会发现文件是文稿而不是unix可执行文件，这就是问题所在。
​    原因是解压的时候标签被刷了。

​    解决：
​        打开终端，输入以下代码
        ```
        $ chmod +x 「macos」中文件的路径
        ```
​        重新打开就解决了