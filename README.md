# AI Stock Master for OpenClaw / AI股票大师 For 小龙虾

> **Professional AI Analysis Engine for AI Agents.**
> Powered by 3 Legendary Investment Expert Models.

---

### Introduction
**AI Stock Master for OpenClaw** is a specialized AI analysis driver designed for the [OpenClaw](https://github.com/henguiyun/openclaw) AI Agent ecosystem. It acts as a lightweight interface that connects your Agent to our high-performance cloud intelligence engine.

### Key Features
- **3-Master Decision Grid**: Combined logic from Buffett, Lynch, Graham, etc.
- **Deep Market Sentiment**: Real-time evaluation of Greedy/Fearful states via bull-bear ratios.
- **Sector Momentum Tracking**: Identification of capital inflows and top momentum sectors.
- **Master Recommendation Score**: Scoring and actionable advice for thousands of stocks.

### How to Install into OpenClaw (Installation & Integration)

1. **Clone/Download**: Download this repository.
2. **Move into Skills**: Copy either the `ai-stock-master-chs` or `ai-stock-master-en` directory into your **OpenClaw** root directory under the `skills/` folder.
   - Example path: `OpenClaw/skills/ai-stock-master-en/`
3. **Minimum Requirements**: Ensure your environment has the `requests` library installed (used solely for secure connection to the cloud intelligence engine):
   ```bash
   pip install requests
   ```
4. **Zero Local Compute**: All complex AI Analysis is performed on our remote **Intelligence Server** (`master.ttfox.com`). Your Agent will remain lightweight with zero extra CPU usage for analysis.
5. **Restart OpenClaw**: Restart your OpenClaw AI Agent. It will automatically detect the `SKILL.md` and load the AI Analysis capabilities.
6. **Start Chatting**: Try asking: *"How is the market today?"* or *"Analyze AAPL"*.

### Legal Disclaimer & Data Latency
- **Non-Real-Time Notice**: All data are **DELAYED / POST-MARKET** AI analysis packages. Not suitable for live intraday trading.
- **No Liability**: The authors take NO responsibility for any financial loss incurred by using this tool.

---


### 简介
**AI股票大师 For 小龙虾** 是专为 [OpenClaw（小龙虾）](https://github.com/henguiyun/openclaw) AI 代理生态系统打造的顶级智能分析连接器。它作为轻量级桥梁，将小龙虾与高性能云端智能引擎无缝对接。

### 核心优势
- **3位大师模型**: 深度融合巴菲特、彼得·林奇、格雷厄姆等 3 位宗师的投研逻辑。
- **大师个股诊断**: 输出 0-100 的智能分析分值，并匹配专属的操作建议与风险评级。
- **真实资金流向**: 动态捕捉全市场活跃板块，锁定行业龙头。
- **双语全量适配**: 针对简体中文 (CHS) 和 英文 (EN) 用户环境分别优化。

### 如何安装到小龙虾 (安装与集成)

1. **获取代码**: 下载或克隆本仓库。
2. **移动目录**: 将 `ai-stock-master-chs` (中文) 或 `ai-stock-master-en` (英文) 文件夹复制到 **OpenClaw (小龙虾)** 根目录下的 `skills/` 文件夹中。
   - 示例路径: `OpenClaw/skills/ai-stock-master-chs/`
3. **最小运行环境**: 确保已安装 `requests` 库（仅用于与云端智能引擎建立加密通信）：
   ```bash
   pip install requests
   ```
4. **零算力消耗**: 所有的复杂智能分析计算均在我们的远程 **智能服务器** (`master.ttfox.com`) 侧完成。小龙虾仅作为播报终端，**不占用本地任何计算资源**。
5. **重启小龙虾**: 重新启动你的 OpenClaw AI 代理。系统会自动扫描 `SKILL.md` 并注册智能分析能力。
6. **开启对话**: 尝试对小龙虾说：*"分析大盘"* 或 *"分析股票 000548"*。

### 免责声明与数据时效
- **非实时警告**: 本项目所使用的数据均为 **非实时 / 盘后 / 延时智能分析包**。由于计算需要时间，数据存在显著市场滞后性。
- **免责声明**: 本工具仅供学术研究使用。作者拒绝承担任何因数据滞后、解析错误或用户决策失误导致的经济损失。**股市有风险，入市需谨慎。**

---

**GitHub Repository**: [ai-stock-master-openclaw](https://github.com/hengruiyun/ai-stock-master-openclaw)  
**Support Email**: [ttfox@ttfox.com](mailto:ttfox@ttfox.com)  
**License**: AGPL-3.0
