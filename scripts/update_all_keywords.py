#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为所有类别的 keywords.json 文件添加模板使用统计结构
"""

import json
from pathlib import Path

def update_keywords_file(keywords_file: Path):
    """更新单个 keywords.json 文件，添加模板使用统计"""
    try:
        # 加载现有数据
        with open(keywords_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 检查是否已经有模板使用统计
        if "template_usage_stats" in data:
            print(f"  ✅ {keywords_file.parent.name} 已有模板使用统计")
            return True
        
        # 获取可用模板列表
        available_templates = data.get("available_templates", [])
        if not available_templates:
            print(f"  ❌ {keywords_file.parent.name} 没有可用模板列表")
            return False
        
        # 创建模板使用统计结构
        template_usage_stats = {}
        for template_name in available_templates:
            template_usage_stats[template_name] = {
                "usage_count": 0,
                "last_used": None,
                "created_blogs": []
            }
        
        # 添加到数据中
        data["template_usage_stats"] = template_usage_stats
        
        # 保存文件
        with open(keywords_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ {keywords_file.parent.name} 已添加模板使用统计 ({len(available_templates)} 个模板)")
        return True
        
    except Exception as e:
        print(f"  ❌ {keywords_file.parent.name} 更新失败: {e}")
        return False

def main():
    """主函数"""
    print("🔄 为所有类别添加模板使用统计结构")
    print("=" * 60)
    
    prompts_dir = Path("prompts/blogs_prompt_v1")
    if not prompts_dir.exists():
        print(f"❌ 提示词目录不存在: {prompts_dir}")
        return
    
    success_count = 0
    total_count = 0
    
    # 遍历所有类别目录
    for category_dir in sorted(prompts_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        
        # 检查是否是编号的类别目录
        if not category_dir.name.startswith(('01-', '02-', '03-', '04-', '05-', 
                                             '06-', '07-', '08-', '09-', '10-',
                                             '11-', '12-', '13-', '14-', '15-',
                                             '16-', '17-', '18-', '19-')):
            continue
        
        keywords_file = category_dir / "keywords.json"
        if not keywords_file.exists():
            print(f"  ❌ {category_dir.name} 没有 keywords.json 文件")
            continue
        
        total_count += 1
        print(f"📁 处理类别: {category_dir.name}")
        
        if update_keywords_file(keywords_file):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"🎉 更新完成！")
    print(f"✅ 成功更新: {success_count} 个类别")
    print(f"📊 总计类别: {total_count} 个")
    print("=" * 60)

if __name__ == "__main__":
    main()