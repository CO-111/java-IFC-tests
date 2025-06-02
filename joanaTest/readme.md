This project uses docker to build the java environment.

# command

docker build -t joana-env .

(linux)docker run --rm -it -v $(pwd):/joana joana-env
(windows)docker run --rm -it -v ${PWD}:/joana joana-env

(windows)docker run --rm -it -e DISPLAY=host.docker.internal:0 -v ${PWD}:/joana joana-env

java -jar /joana/joana.ui.ifc.wala.cli.jar
java -jar /joana/joana.ui.ifc.wala.console.jar
java -jar /joana/joana.ui.ifc.sdg.graphviewer.jar

# java compile

编译成 .class：
javac -d out test/starttest1/ExampleIFC.java
编译完 out/ 目录下会有 test/starttest1/ExampleIFC.class JOANA 用它就能分析了。

打包成 .jar（可选）
jar cf out/jars/example-ifc.jar -C out .
然后你可以在 JOANA 的项目配置里把这个 .jar 作为 classpath 加进去。

# to make GUI workable in windows

Windows 下 Docker 运行 GUI 应用的图形化配置
1. 安装 X Server
推荐用 VcXsrv，免费且常用。

下载地址：https://sourceforge.net/projects/vcxsrv/

安装时直接下一步即可

安装完成后，启动 XLaunch 配置

2. 启动 VcXsrv
运行 XLaunch

选择 Multiple windows

选择 Start no client（只启动 X Server，不启动任何程序）

选择 Disable access control（允许所有连接，为方便调试；安全要求高时可单独配置）

点击 Finish 启动 X Server

这样你的 Windows 就有了一个运行中的 X Server，监听默认的 0 号显示器（DISPLAY=:0）

3. 配置 Windows 防火墙（如果弹窗允许）
确保防火墙允许 VcXsrv 的网络访问，否则 Docker 容器连不上。

4. 在 PowerShell 里运行 Docker 命令，指定 DISPLAY
打开 PowerShell，进入你的工作目录，运行：

powershell
docker run --rm -it -e DISPLAY=host.docker.internal:0 -v ${PWD}:/joana joana-env
说明：

-e DISPLAY=host.docker.internal:0 ：告诉 Docker 容器去连接 Windows 主机的 X Server

-v ${PWD}:/joana ：挂载当前目录（已做）

5. 允许 X Server 接受 Docker 连接
默认 VcXsrv 允许所有连接，因为刚才启动时选了 “Disable access control”。

如果你没选或者连接有问题，可以手动允许访问：

打开 PowerShell，运行：

powershell
xhost +  # 在 Linux 上运行的命令，Windows 没有这个命令，通常直接禁用访问控制即可
所以在 Windows 上就是启动 VcXsrv 时选择 “Disable access control” 来绕过。

6. 运行 GUI Java 程序
容器里执行你的命令：

bash
java -jar /joana/joana.ui.ifc.sdg.graphviewer.jar
它会通过 DISPLAY=host.docker.internal:0 把窗口显示在你 Windows 上的 VcXsrv 里。

额外提醒
有时候 Windows 上网络配置复杂，host.docker.internal 不生效，可以用 Windows 主机的实际 IP 地址替代（比如 192.168.x.x:0）。

如果不想装 X Server，也可以继续用命令行版本（CLI），无 GUI。