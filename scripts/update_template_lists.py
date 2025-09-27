#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新所有 keywords.json 文件中的模板列表
确保 available_templates 字段反映实际存在的模板文件
"""

import os
import json
import glob

def get_template_files(templates_dir):
    """获取模板目录中的所有 .md 文件"""
    if not os.path.exists(templates_dir):
        return []
    
    template_files = []
    for file in os.listdir(templates_dir):
        if file.endswith('.md'):
            template_files.append(file)
    
    return sorted(template_files)

def update_keywords_file(keywords_file_path):
    """更新单个 keywords.json 文件"""
    print(f"📝 处理文件: {keywords_file_path}")
    
    # 获取模板目录路径
    category_dir = os.path.dirname(keywords_file_path)
    templates_dir = os.path.join(category_dir, 'templates')
    
    # 获取实际的模板文件
    actual_templates = get_template_files(templates_dir)
    
    if not actual_templates:
        print(f"⚠️  警告: {templates_dir} 中没有找到模板文件")
        return False
    
    print(f"   找到模板文件: {actual_templates}")
    
    # 读取现有的 keywords.json
    try:
        with open(keywords_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return False
    
    # 更新 available_templates 字段
    data['available_templates'] = actual_templates
    
    # 确保有 template_usage_stats 字段
    if 'template_usage_stats' not in data:
        data['template_usage_stats'] = {}
    
    # 为每个模板初始化使用统计
    for template in actual_templates:
        if template not in data['template_usage_stats']:
            data['template_usage_stats'][template] = {
                "usage_count": 0,
                "last_used": None,
                "created_blogs": []
            }
    
    # 移除不存在的模板的统计信息
    templates_to_remove = []
    for template in data['template_usage_stats']:
        if template not in actual_templates:
            templates_to_remove.append(template)
    
    for template in templates_to_remove:
        del data['template_usage_stats'][template]
        print(f"   移除不存在的模板统计: {template}")
    
    # 保存更新后的文件
    try:
        with open(keywords_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 成功更新: {len(actual_templates)} 个模板")
        return True
    except Exception as e:
        print(f"❌ 保存文件失败: {e}")
        return False

def main():
    """主函数"""
    print("🔄 开始更新所有 keywords.json 文件中的模板列表...")
    
    # 基础路径
    base_path = "prompts/blogs_prompt_v1"
    
    if not os.path.exists(base_path):
        print(f"❌ 基础路径不存在: {base_path}")
        return
    
    # 查找所有类别目录
    category_dirs = []
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item.startswith(('0', '1')):  # 以数字开头的目录
            category_dirs.append(item_path)
    
    category_dirs.sort()
    print(f"📁 找到 {len(category_dirs)} 个类别目录")
    
    success_count = 0
    total_count = 0
    
    # 处理每个类别
    for category_dir in category_dirs:
        keywords_file = os.path.join(category_dir, 'keywords.json')
        
        if os.path.exists(keywords_file):
            total_count += 1
            if update_keywords_file(keywords_file):
                success_count += 1
            print()  # 空行分隔
        else:
            print(f"⚠️  跳过: {keywords_file} (文件不存在)")
    
    print(f"🎉 完成! 成功更新 {success_count}/{total_count} 个文件")

if __name__ == "__main__":
    main()