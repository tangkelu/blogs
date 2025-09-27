#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试模板选择功能
"""

import json
from pathlib import Path
from batch_blog_generation import get_least_used_template, load_keywords

def test_template_selection():
    """测试模板选择功能"""
    print("🧪 测试模板选择功能")
    
    # 测试目录
    test_category = Path("prompts/blogs_prompt_v1/01-DataCenter-ServerPCB")
    keywords_file = test_category / "keywords.json"
    templates_dir = test_category / "templates"
    
    if not keywords_file.exists():
        print(f"❌ 关键词文件不存在: {keywords_file}")
        return False
    
    if not templates_dir.exists():
        print(f"❌ 模板目录不存在: {templates_dir}")
        return False
    
    # 加载关键词数据
    keywords_data = load_keywords(keywords_file)
    if not keywords_data:
        print("❌ 无法加载关键词数据")
        return False
    
    print(f"✅ 成功加载关键词数据")
    
    # 检查模板使用统计
    template_stats = keywords_data.get("template_usage_stats", {})
    print(f"📊 当前模板使用统计:")
    for template_name, stats in template_stats.items():
        print(f"  - {template_name}: 使用次数 {stats['usage_count']}")
    
    # 测试模板选择
    print(f"\n🎯 测试模板选择...")
    for i in range(5):
        selected_template = get_least_used_template(templates_dir, keywords_data)
        if selected_template:
            print(f"  第 {i+1} 次选择: {selected_template.name}")
            
            # 模拟使用模板（增加使用次数）
            template_stats = keywords_data.get("template_usage_stats", {})
            if selected_template.name in template_stats:
                template_stats[selected_template.name]["usage_count"] += 1
            else:
                template_stats[selected_template.name] = {"usage_count": 1, "last_used": None, "created_blogs": []}
        else:
            print(f"  第 {i+1} 次选择: 无法选择模板")
    
    # 显示最终统计
    print(f"\n📊 模拟使用后的模板统计:")
    template_stats = keywords_data.get("template_usage_stats", {})
    for template_name, stats in template_stats.items():
        print(f"  - {template_name}: 使用次数 {stats['usage_count']}")
    
    return True

if __name__ == "__main__":
    test_template_selection()