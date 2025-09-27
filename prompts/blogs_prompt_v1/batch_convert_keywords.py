#!/usr/bin/env python3
"""
批量转换所有keywords.json文件的脚本
将字符串数组格式转换为对象数组格式，支持使用状态和模板链接
"""

import json
import os
import glob
from pathlib import Path

def get_available_templates(directory):
    """获取目录下可用的模板文件"""
    templates_dir = os.path.join(directory, 'templates')
    if not os.path.exists(templates_dir):
        return []
    
    template_files = []
    for file in os.listdir(templates_dir):
        if file.endswith('.md'):
            template_files.append(file)
    
    return sorted(template_files)

def convert_keywords_format(file_path):
    """转换单个关键词文件格式"""
    
    try:
        # 读取原始文件
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 获取目录路径
        directory = os.path.dirname(file_path)
        
        # 获取可用模板
        available_templates = get_available_templates(directory)
        
        # 添加available_templates字段（如果不存在）
        if 'available_templates' not in data:
            data['available_templates'] = available_templates
        
        converted_count = 0
        
        # 转换每个subsection中的keywords
        for subsection in data.get('subsections', []):
            keywords = subsection.get('keywords', [])
            
            # 检查是否需要转换（如果第一个元素是字符串）
            if keywords and isinstance(keywords[0], str):
                new_keywords = []
                for keyword in keywords:
                    new_keywords.append({
                        "keyword": keyword,
                        "used": False,
                        "template": None,
                        "usage_date": None,
                        "notes": ""
                    })
                subsection['keywords'] = new_keywords
                converted_count += len(keywords)
                print(f"  转换了 '{subsection['name']}' 部分的 {len(keywords)} 个关键词")
        
        if converted_count > 0:
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ {file_path} - 转换了 {converted_count} 个关键词")
            return True
        else:
            print(f"⏭️  {file_path} - 已经是新格式，跳过")
            return False
            
    except Exception as e:
        print(f"❌ {file_path} - 转换失败: {str(e)}")
        return False

def batch_convert_all():
    """批量转换所有keywords.json文件"""
    
    base_dir = "."
    pattern = "*/keywords.json"
    
    # 查找所有keywords.json文件
    json_files = glob.glob(pattern, recursive=False)
    
    if not json_files:
        print("未找到任何keywords.json文件")
        return
    
    print(f"找到 {len(json_files)} 个keywords.json文件")
    print("=" * 60)
    
    converted_files = 0
    skipped_files = 0
    failed_files = 0
    
    for file_path in sorted(json_files):
        result = convert_keywords_format(file_path)
        if result is True:
            converted_files += 1
        elif result is False:
            skipped_files += 1
        else:
            failed_files += 1
    
    print("=" * 60)
    print(f"批量转换完成:")
    print(f"  ✅ 成功转换: {converted_files} 个文件")
    print(f"  ⏭️  跳过文件: {skipped_files} 个文件")
    print(f"  ❌ 失败文件: {failed_files} 个文件")

if __name__ == "__main__":
    batch_convert_all()