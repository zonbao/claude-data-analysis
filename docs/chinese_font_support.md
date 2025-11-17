# 中文字体显示支持（可视化）

使用 `/visualize` 或本地脚本生成图表时，如果 Matplotlib/Seaborn 或 Plotly 缺少中文字体，会出现中文不显示、方块或问号的情况。可以按以下步骤启用中文字体：

## 1. 准备字体文件
1. 下载任意 CJK 字体（推荐 [NotoSansSC-Regular.otf](https://github.com/googlefonts/noto-cjk) 或思源黑体/微软雅黑等）。
2. 将字体文件放到仓库中的 `visualizations/fonts/` 目录下（目录已包含占位符 `.gitkeep`，可直接复制字体）。

> 如果当前环境无法联网，可在有网络的机器上下载字体后，通过文件拷贝/挂载的方式放入该目录。

## 2. 注册字体
在生成图表前调用辅助脚本完成字体注册（会同时处理 Matplotlib/Seaborn 和 Plotly，并自动读取字体内部名称）：

```bash
python visualizations/font_setup.py
```

或在代码中显式调用：

```python
from visualizations.font_setup import configure_chinese_font
configure_chinese_font()  # 注册 visualizations/fonts/ 下的 NotoSansSC-Regular.otf
```

运行成功后会输出：

```
✅ Chinese font registered: visualizations/fonts/NotoSansSC-Regular.otf
```

## 3. 生成图表
完成字体注册后，再运行 `/visualize` 生成的脚本或本地可视化代码。Matplotlib/Seaborn 的中文标题、坐标轴标签、注释，以及 Plotly HTML 图表中的中文都会正常显示，同时已修复负号显示异常的问题。

## 4. 故障排查
- **提示未找到字体**：确认字体文件已放入 `visualizations/fonts/`，文件名与大小写正确。
- **仍然乱码**：在代码开头再次调用 `configure_chinese_font()`，确保在创建图形对象前完成注册；同时删除 Matplotlib 字体缓存（`~/.cache/matplotlib`）后重试。
- **需要自定义字体**：调用 `configure_chinese_font(Path("你的字体路径.otf"))` 即可。
