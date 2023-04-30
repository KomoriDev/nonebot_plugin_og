
<div align="center">

# Nonebot-plugin-og

_✨ 检测链接并生成预览图 ✨_  

</div>

## 📖 介绍

检测链接并生成预览图，基于 [Open Graph](https://ogp.me/) 协议

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-og

</details>

<details>
<summary>使用pip安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入以下指令即可安装

    pip iqnstall nonebot-plugin-og

</details>


打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_og"]


## 🎉 使用

直接发送任意链接，只要是支持 Open Graph 协议的网站，此插件都会自动发送预览图。

## 鸣谢

* [`nonebot/noenbot2`](https://github.com/nonebot/nonebot2)：跨平台Python异步机器人框架
* [`Mrs4s/go-cqhttp`](https://github.com/Mrs4s/go-cqhttp)：cqhttp的golang实现，轻量、原生跨平台.
* [`koishijs/koishi-plugin-og`](https://github.com/koishijs/koishi-plugin-og)：本项目直接参考 ~~（直接开抄~~


## 开源许可证

使用 [MIT](#) 许可证发布。

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```