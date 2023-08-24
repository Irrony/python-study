### Appium 环境搭建 ###

1. Pre-Condition：
    (1) 检查java：java -version
    (2) 检查homebrew: brew -v
    (3) 检查git：git --version
    (4) 安装carthage: brew install carthage
    (5) 安装安卓SDK：
        1) 先cd到android-sdk-macosx文件夹下：
        2) 再输入命令：tools/android update sdk --no-ui
    (6) 配置环境变量：
        1) vim ~/.bash_profile
        2) export ANDROID_HOME=/Users/rong.yin/Downloads/android-sdk-macosx
           export PATH=${PATH}:${ANDROID_HOME}/tools
           export PATH=${PATH}:${ANDROID_HOME}/platform-tools
           export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-20.jdk/Contents/Home
           export PATH=$JAVA_HOME/bin:$PATH
2. 安装Appium-Server
    (1) 安装命令：npm install -g appium
    (2) 检查命令：appium -v
3. 安装Appium-Client
    (1) 安装命令：pip3 install Appium-Python-Client
    (2) 检查命令：
        1) 安装doctor：npm install appium-doctor -g
        2) 检查：appium-doctor
4. 启动Appium：appium &
5. 查看端口使用情况：lsof -i tcp:4723
6. 杀死进程：kill xxxx