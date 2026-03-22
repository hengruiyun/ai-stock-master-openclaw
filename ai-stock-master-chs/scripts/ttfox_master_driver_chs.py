# -*- coding: utf-8 -*-
try:
    import requests
    DEPENDENCY_OK = True
except ImportError:
    DEPENDENCY_OK = False
    print("【警告】未检测到 requests 库，请执行 'pip install requests' 以启用智能分析功能。")
import json
import urllib.parse
import traceback

class TTFoxMasterAgent:
    """
    TTFox AI股票大师 - OpenClaw 驱动程序 (中文版)
    包含六大核心侦测模块，涵盖大盘情绪、行业异动、个股大师决策、全市场精选过滤等。
    """
    
    def __init__(self):
        # 统一使用配置好的公网生产环境域名
        self.web_url = "https://master.ttfox.com"
        self.api_url = "https://master.ttfox.com"
        self.headers = {"Content-Type": "application/json"}

    def _check_dep(self):
        """内部依赖检查逻辑"""
        if not DEPENDENCY_OK:
            return {
                "status": "error",
                "broadcast": "报告主人：我目前无法连接远程智能中心。由于运行环境缺少 `requests` 模块，请在终端执行 `pip install requests` 后重启我，即可开启 3 大宗师分析能力！",
                "advice": "请安装 requests 依赖",
                "error": "Missing requests library"
            }
        return None

    def get_market_sentiment(self, market="CN"):
        """1. 获取大盘情绪"""
        err_msg = self._check_dep()
        if err_msg: return err_msg

        try:
            url = f"{self.web_url}/api/rating/stats?market={market}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_data = response.json()
                if json_data.get('success') and json_data.get('data'):
                    dist = json_data['data'].get('distribution', {})
                    bull_count = sum(dist.get(str(i), 0) for i in range(5, 9))
                    bear_count = sum(dist.get(str(i), 0) for i in range(1, 5))
                    total = bull_count + bear_count
                    if total == 0: return {"status": "error", "message": "暂无数据"}
                    bull_ratio = (bull_count / total) * 100
                    state = "贪婪主导" if bull_ratio > 55 else "恐慌主导" if bull_ratio < 45 else "震荡博弈"
                    return {
                        "status": "success",
                        "market": market,
                        "market_state": state,
                        "bull_ratio": f"{bull_ratio:.1f}%",
                        "advice": f"当前市场多方占比为 {bull_ratio:.1f}%，大盘处于【{state}】。"
                    }
        except Exception as e:
            return {"status": "error", "message": f"大盘情绪获取失败: {str(e)}"}
        return {"status": "error", "message": "获取失败"}

    def get_industry_ranking(self, market="CN", top_n=5):
        """2. 获取全市场行业排行榜"""
        err_msg = self._check_dep()
        if err_msg: return err_msg
        try:
            url = f"{self.web_url}/api/treeview/industries?market={market}&limit=100"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('data'):
                    sorted_industries = sorted(data['data'], key=lambda x: x.get('score', 0), reverse=True)
                    top_industries = [{"name": ind.get('name'), "score": ind.get('score')} for ind in sorted_industries[:top_n]]
                    return {"status": "success", "top_industries": top_industries}
        except Exception as e:
            return {"status": "error", "message": f"排序失败: {str(e)}"}
        return {"status": "error", "message": "排序失败"}

    def get_industry_top_stocks(self, industry_name, market="CN"):
        """3. 获取行业龙头个股"""
        err_msg = self._check_dep()
        if err_msg: return err_msg
        try:
            url = f"{self.web_url}/api/treeview/stocks?market={market}&industry={urllib.parse.quote(industry_name)}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('data'):
                    sorted_stocks = sorted(data['data'], key=lambda x: x.get('rating_level', 0), reverse=True)
                    top_stocks = [{"code": s.get('code'), "name": s.get('name'), "rating": s.get('rating_level')} for s in sorted_stocks[:5]]
                    return {"status": "success", "top_stocks": top_stocks}
        except Exception as e:
            return {"status": "error", "message": f"未找到个股: {str(e)}"}
        return {"status": "error", "message": "未找到个股"}

    def get_master_picks(self, market="CN"):
        """4. 大师全盘精选过滤"""
        err_msg = self._check_dep()
        if err_msg: return err_msg
        try:
            url = f"{self.web_url}/api/treeview/stocks?market={market}&limit=3000"
            response = requests.get(url, timeout=8)
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('data'):
                    strong = [s for s in data['data'] if s.get('rating_level', 0) >= 7]
                    picks = [{"code": s.get('code'), "name": s.get('name'), "level": s.get('rating_level')} for s in strong[:10]]
                    return {"status": "success", "total_found": len(strong), "top_picks": picks}
        except Exception as e:
            return {"status": "error", "message": f"扫描失败: {str(e)}"}
        return {"status": "error", "message": "扫描失败"}

    def get_hot_money_alerts(self, market="CN"):
        """5. 游资热钱流向监测 - 基于真实行业评分动态提取"""
        err_msg = self._check_dep()
        if err_msg: return err_msg
        try:
            url = f"{self.web_url}/api/treeview/industries?market={market}&limit=20"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('data'):
                    # 排序找出评分（涨幅/活跃度）最高的 Top 3
                    hot_data = sorted(data['data'], key=lambda x: x.get('score', 0), reverse=True)[:3]
                    hot_names = [h.get('name') for h in hot_data]
                    
                    if not hot_names:
                        return {"status": "error", "message": "暂时无法捕捉热点异动"}
                    
                    names_str = "、".join(hot_names)
                    return {
                        "status": "success",
                        "market": market,
                        "hot_concepts": hot_names,
                        "advice": f"当前市场资金最活跃的板块为【{names_str}】，建议关注相关板块内的龙头走势。",
                        "broadcast": f"【热钱预警】检测到资金正在流入 {names_str} 板块。"
                    }
        except Exception as e:
            return {"status": "error", "message": f"监测失败: {str(e)}"}
        return {"status": "error", "message": "热钱数据获取失败"}

    def get_stock_analysis(self, stock_code, market="CN"):
        """6. 个股 大师深度决断"""
        err_msg = self._check_dep()
        if err_msg: return err_msg
        try:
            url = f"{self.api_url}/api/analyze"
            payload = {"stock_code": stock_code}
            response = requests.post(url, json=payload, headers=self.headers, timeout=10)
            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "success":
                    master = result.get("master_analysis", {})
                    advice = result.get("investment_advice", {})
                    indicators = result.get("indicators", {})
                    action = advice.get("recommendation", "观望")
                    return {
                        "status": "success",
                        "stock_code": result.get("symbol"),
                        "current_price": indicators.get("current_price", 0),
                        "overall_score": master.get("overall_score", 0),
                        "best_strategy": master.get("best_strategy", "多模型综合"),
                        "recommendation": action,
                        "risk_level": advice.get("risk_level", "防守"),
                        "action_guidance": advice.get("reasoning", ""),
                        "broadcast": f"{stock_code} 综合评分 {master.get('overall_score', 0)} 分，操作建议【{action}】。"
                    }
                else:
                    return {"status": "error", "message": result.get("error", "该股票代码无分析数据")}
        except Exception as e:
            return {"status": "error", "message": f"连接失败: {str(e)}"}
        return {"status": "error", "message": "连接失败"}

