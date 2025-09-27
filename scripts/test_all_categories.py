#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试所有类别的模板选择功能
"""

import os
import json
from batch_blog_generation import get_least_used_template

def test_category_templates(category_path):
    """测试单个类别的模板选择"""
    keywords_file = os.path.join(category_path, 'keywords.json')
    
    if not os.path.exists(keywords_file):
        return False, "keywords.json 不存在"
    
    try:
        with open(keywords_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 检查必要字段
        if 'available_templates' not in data:
            return False, "缺少 available_templates 字段"
        
        if 'template_usage_stats' not in data:
            return False, "缺少 template_usage_stats 字段"
        
        templates = data['available_templates']
        if not templates:
            return False, "模板列表为空"
        
        # 测试模板选择
        templates_dir = os.path.join(category_path, 'templates')
        from pathlib import Path
        selected_template_path = get_least_used_template(Path(templates_dir), data)
        selected_template = selected_template_path.name if selected_template_path else None
        
        if selected_template not in templates:
            return False, f"选择的模板 {selected_template} 不在可用模板列表中"
        
        return True, f"成功 - 找到 {len(templates)} 个模板，选择了 {selected_template}"
        
    except Exception as e:
        return False, f"错误: {str(e)}"

def main():
    """主函数"""
    print("🧪 测试所有类别的模板选择功能...")
    
    base_path = "prompts/blogs_prompt_v1"
    
    if not os.path.exists(base_path):
        print(f"❌ 基础路径不存在: {base_path}")
        return
    
    # 获取所有类别目录
    categories = []
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item.startswith(('0', '1')):
            categories.append((item, item_path))
    
    categories.sort()
    
    success_count = 0
    total_count = len(categories)
    
    print(f"📁 找到 {total_count} 个类别目录\n")
    
    for category_name, category_path in categories:
        print(f"📝 测试类别: {category_name}")
        success, message = test_category_templates(category_path)
        
        if success:
            print(f"   ✅ {message}")
            success_count += 1
        else:
            print(f"   ❌ {message}")
        print()
    
    print(f"🎉 测试完成! 成功: {success_count}/{total_count} 个类别")
    
    if success_count == total_count:
        print("✅ 所有类别的模板选择功能都正常工作！")
    else:
        print(f"⚠️  有 {total_count - success_count} 个类别存在问题")

if __name__ == "__main__":
    main()