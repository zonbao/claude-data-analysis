# Claude Data Analysis Assistant

A modern, intelligent data analysis platform built with Claude Code's sub-agents, slash-commands, and hooks. Transform your data analysis workflow with AI-powered assistance.

## 🚀 Quick Start

### 1. Set Up Your Data
Place your dataset in the `data_storage/` directory:
```bash
cp your_data.csv ./data_storage/
```

### 2. Start Analysis
Use intuitive slash commands to analyze your data:
```bash
# Basic exploratory analysis
/analyze user_behavior_sample.csv exploratory

# Create visualizations
/visualize user_behavior_sample.csv all

# Generate analysis code
/generate python data-cleaning

# Create comprehensive report
/report user_behavior_sample.csv complete markdown
```

## 🎯 Key Features

### Intelligent Sub-Agents
- **data-explorer**: Expert statistical analysis and pattern discovery
- **visualization-specialist**: Beautiful, insightful charts and graphs
- **code-generator**: Production-ready analysis code
- **report-writer**: Comprehensive analysis reports
- **quality-assurance**: Data validation and quality control
- **hypothesis-generator**: Research hypothesis and insights

### Intuitive Slash Commands
- `/analyze [dataset] [type]` - Perform data analysis
- `/visualize [dataset] [type]` - Create visualizations
- `/generate [language] [type]` - Generate analysis code
- `/report [dataset] [format]` - Generate reports
- `/quality [dataset] [action]` - Quality assurance
- `/hypothesis [dataset] [domain]` - Generate hypotheses

### Automated Workflows
- **Data Validation**: Automatic quality checks on data upload
- **Smart Context**: Project-aware analysis suggestions
- **Reproducible Analysis**: Complete documentation and code generation

## 📊 Usage Examples

### User Behavior Analysis
```bash
# Complete analysis workflow
/analyze user_behavior.csv exploratory
/visualize user_behavior.csv trends
/quality user_behavior.csv clean
/report user_behavior.csv complete html
/generate python user-segmentation
```

### Sales Data Analysis
```bash
# Sales performance analysis
/analyze sales_data.csv statistical
/visualize sales_data.csv trends
/generate sql revenue-analysis
/report sales_data.csv executive pdf
```

### Customer Analytics
```bash
# Customer segmentation
/analyze customer_data.csv predictive
/visualize customer_data.csv distribution
/generate r clustering-analysis
/hypothesis customer_data churn-prediction
```

## 🛠️ Project Structure

```
claude-data-analysis/
├── .claude/
│   ├── agents/          # Sub-agent configurations
│   ├── commands/        # Slash command definitions
│   ├── hooks/          # Automation scripts
│   └── settings.json   # Claude Code settings
├── data_storage/       # Your data files
├── visualizations/     # Generated charts
├── generated_code/     # Analysis code
├── analysis_reports/   # Analysis reports
├── examples/          # Example datasets and workflows
└── docs/             # Documentation
```

## 🎨 Sample Data

The project includes sample data to get you started:

- **user_behavior_sample.csv**: Sample user behavior data with user actions, devices, locations, and revenue
- **Field descriptions**: user_id, session_id, timestamp, action, page_url, device_type, location, revenue

## 🔧 Configuration

### Environment Setup
The project uses Claude Code's configuration system. Key settings:

1. **Hooks**: Automated validation and context loading
2. **Sub-agents**: Specialized AI assistants for different tasks
3. **Commands**: Custom slash commands for common operations

### Requirements
- Python 3.8+ for data analysis
- Claude Code with sub-agents enabled
- Data files in CSV, JSON, or Excel format

## 📚 Getting Started Guide

### For New Users
1. **Place your data** in `data_storage/`
2. **Run exploratory analysis**: `/analyze your_data.csv exploratory`
3. **Create visualizations**: `/visualize your_data.csv all`
4. **Generate report**: `/report your_data.csv complete markdown`

### For Advanced Users
1. **Customize agents**: Modify `.claude/agents/` configurations
2. **Create custom commands**: Add new commands in `.claude/commands/`
3. **Set up automation**: Configure hooks in `.claude/settings.json`
4. **Extend functionality**: Add custom analysis scripts

## 🎯 Analysis Types

### Exploratory Analysis
- Data quality assessment
- Summary statistics
- Pattern discovery
- Initial insights

### Statistical Analysis
- Hypothesis testing
- Correlation analysis
- Regression analysis
- Confidence intervals

### Predictive Analysis
- Feature importance
- Predictive modeling
- Variable relationships
- Model recommendations

### Complete Analysis
- All analysis types
- Comprehensive reports
- Visualizations
- Actionable insights

## 📈 Visualization Types

### All Visualizations
- Comprehensive dashboard
- Multiple chart types
- Interactive exploration
- Executive summary

### Specific Charts
- **Trends**: Time series, moving averages
- **Distribution**: Histograms, box plots, density plots
- **Correlation**: Heatmaps, scatter plots, correlation matrices
- **Comparison**: Bar charts, grouped charts, small multiples

### 中文显示支持
如果使用 `/visualize` 生成的图表中中文不显示或出现方块，请在生成图表前执行中文字体配置（自动识别字体内部名称）：

```bash
python visualizations/font_setup.py
```

将常用中文字体（如 NotoSansSC-Regular.otf、思源黑体、微软雅黑等）放入 `visualizations/fonts/` 目录后运行上述命令，即可让 Matplotlib/Seaborn 和 Plotly 的标题、坐标轴、注释正常显示中文。详细步骤见《docs/chinese_font_support.md》。

## 🔄 将本地修改推送到你的 GitHub 仓库

如果本地已有提交但 GitHub 上看不到更新，通常是还未配置远程或未推送当前分支：

1. 检查远程是否已配置：`git remote -v`（若为空需要添加）。
2. 添加远程：`git remote add origin https://github.com/你的用户名/claude-data-analysis`。
3. 推送当前分支（例如 `work`）：`git push -u origin work`。

更多常见问题与处理方法见《docs/github_sync.md》。

## 🔍 Code Generation

### Supported Languages
- **Python**: Pandas, NumPy, Scikit-learn, Matplotlib
- **R**: Tidyverse, ggplot2, caret
- **SQL**: All major dialects
- **JavaScript**: D3.js, Plotly.js, TensorFlow.js

### Analysis Types
- Data cleaning and preprocessing
- Statistical analysis
- Machine learning
- Visualization code
- Custom analysis

## 📋 Project Status

**Current Phase**: Week 1.1 - Project Initialization ✅

### Completed Features
- [x] Project structure and configuration
- [x] Data Explorer sub-agent
- [x] Visualization Specialist sub-agent
- [x] Core slash commands (/analyze, /visualize, /generate)
- [x] Automation hooks
- [x] Sample data and documentation

### Upcoming Features
- [ ] Report Writer sub-agent
- [ ] Quality Assurance sub-agent
- [ ] Hypothesis Generator sub-agent
- [ ] Advanced slash commands
- [ ] Interactive dashboards
- [ ] Integration with external tools

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
3. **Add your improvements**
4. **Test your changes**
5. **Submit a pull request**

### Development Guidelines
- Follow the established code style
- Add comprehensive documentation
- Include unit tests for new features
- Update the README as needed

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Claude Code](https://claude.ai/code)
- Inspired by the [DATAGEN](https://github.com/starpig1129/DATAGEN) project
- Powered by modern data science tools and frameworks

## 📞 Support

For support and questions:
- Check the documentation in the `docs/` directory
- Review the examples in `examples/`
- Use the `/help` command for usage assistance

---

**Start analyzing your data smarter, not harder!** 🚀