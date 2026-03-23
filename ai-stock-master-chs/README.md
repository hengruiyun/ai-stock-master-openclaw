# AI股票大师 For 小龙虾

> 基于 5 位顶级投资专家模型的智能分析系统，专为 [OpenClaw（小龙虾）](https://github.com/hengruiyun/ai-stock-master-openclaw) AI Agent 深度集成而设计。


---

## 简介

**AI股票大师 For 小龙虾** 是 [ai-stock-master-openclaw](https://github.com/hengruiyun/ai-stock-master-openclaw) 的简体中文版官方连接器。

它作为轻量级桥梁，将专业级的智能分析能力注入到 OpenClaw（小龙虾）AI Agent 中。所有复杂计算均在 **云端智能引擎** 侧完成，小龙虾本身仅负责数据的网络中转与播报。

由于核心推演不占用本地算力，本技能完全不会影响小龙虾的运行速度。

---

## 核心功能

| 功能模块 | 描述 | 调用函数 |
|:---|:---|:---|
| **大盘情绪雷达** | 实时监控市场多空力量，判断贪婪/恐慌/震荡区间 | `get_market_sentiment()` |
| **行业竞速排行** | 追踪全市场行业动量评分，识别资金风口 | `get_industry_ranking()` |
| **大师全盘精选** | 全市场扫描，筛选综合评分 7 级以上强势个股 | `get_master_picks()` |
| **热钱流向监测** | 基于真实行业评分动态追踪资金最活跃板块 | `get_hot_money_alerts()` |
| **个股大师终审** | 11位投资大师模型综合决策，输出操作建议与风险等级 | `get_stock_analysis()` |

---

## 5位投资专家策略矩阵

本系统深度融合了以下投资宗师的核心理念：

- **巴菲特** (Buffett) — 价值投资，长期趋势
- **彼得·林奇** (Lynch) — 成长投资，动量确认
- **格雷厄姆** (Graham) — 安全边际，低风险介入
- 以及更多宗师策略...

---

## 快速开始

### 安装依赖

```bash
pip install requests
```

### 基本使用

```python
from scripts.ttfox_master_driver_chs import TTFoxMasterAgent

agent = TTFoxMasterAgent()

# 查询大盘情绪
sentiment = agent.get_market_sentiment()
print(sentiment['advice'])

# 分析指定股票
result = agent.get_stock_analysis("000548")
print(result['broadcast'])
```

### 在小龙虾中使用

将本目录放置于 OpenClaw 的技能 (Skills) 目录下，小龙虾将自动加载本 `SKILL.md` 并注册以下触发场景：

- 用户说 **"大盘怎么样"** → 自动调用大盘情绪分析
- 用户说 **"白酒板块有哪些好股"** → 自动调用行业龙头追踪
- 用户说 **"分析 000548"** → 自动调用 11 大师深度决断

---

## 文件结构

```
ai-stock-master-chs//
├── README.md                       # 本说明文件
├── SKILL.md                        # OpenClaw 技能注册与触发配置
└── scripts/
    └── ttfox_master_driver_chs.py  # 核心驱动引擎
```

---

## 数据来源与时效性

本系统通过 **TTFox 智能服务器** (`https://master.ttfox.com`) 获取智能分析结果。

** 重要声明：**
- **非实时属性**: 本系统所调用的数据均为 **非实时 / 盘后 / 静态智能分析包**。由于 A 股量化计算量巨大，数据包通常存在一定的市场滞后性。
- **用途限制**: 本工具仅适用于 **中长期趋势研究** 和 **智能分析逻辑验证**，严禁将其作为分秒必争的短线实盘交易依据。

---

## 开源地址与支持

- **GitHub**: [https://github.com/hengruiyun/ai-stock-master-openclaw](https://github.com/hengruiyun/ai-stock-master-openclaw)
- **联系邮箱**: [ttfox@ttfox.com](mailto:ttfox@ttfox.com)

---

## 免责声明 (Disclaimers)

1. **非投资建议**: 本项目及其包含的所有内容（包括但不限于分析结论、大师评分、操作建议）仅供 **科研与编程学习** 之用，不构成任何形式的投资建议。
2. **拒绝承担滞后风险**: 由于采用 **非实时数据**，系统生成的结论可能与当前市场实况存在严重偏差。作者及相关开发者不承担任何因数据滞后、解析错误或系统故障而导致的经济损失。
3. **自负盈亏**: 股市有风险，入市需谨慎。用户根据本工具提供的信息进行的一切投资行为，风险由用户自行承担。
