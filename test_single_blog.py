#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试单个博客生成流程（不调用API）
"""

from pathlib import Path
from batch_blog_generation import (
    load_keywords, 
    select_keywords, 
    get_least_used_template,
    fill_template_variables,
    generate_filename,
    update_template_usage,
    update_keyword_usage,
    save_keywords
)

def test_single_blog_generation():
    """测试单个博客生成流程"""
    print("🧪 测试单个博客生成流程")
    
    # 测试目录
    test_category = Path("prompts/blogs_prompt_v1/01-DataCenter-ServerPCB")
    keywords_file = test_category / "keywords.json"
    templates_dir = test_category / "templates"
    
    print(f"📁 测试类别: {test_category.name}")
    
    # 1. 加载关键词
    keywords_data = load_keywords(keywords_file)
    if not keywords_data:
        print("❌ 无法加载关键词数据")
        return False
    print("✅ 成功加载关键词数据")
    
    # 2. 选择关键词
    main_keyword, lsi_keywords = select_keywords(keywords_data)
    if not main_keyword:
        print("❌ 无法选择关键词")
        return False
    print(f"✅ 选择关键词: {main_keyword['keyword']}")
    print(f"   LSI关键词: {', '.join(lsi_keywords)}")
    
    # 3. 选择模板（基于使用次数）
    template_file = get_least_used_template(templates_dir, keywords_data)
    if not template_file:
        print("❌ 无法选择模板")
        return False
    print(f"✅ 选择模板: {template_file.name}")
    
    # 显示当前模板使用统计
    template_stats = keywords_data.get("template_usage_stats", {})
    print("📊 当前模板使用统计:")
    for template_name, stats in template_stats.items():
        marker = " 👈" if template_name == template_file.name else ""
        print(f"   - {template_name}: {stats['usage_count']} 次{marker}")
    
    # 4. 加载并填充模板
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
        print("✅ 成功加载模板内容")
    except Exception as e:
        print(f"❌ 加载模板失败: {e}")
        return False
    
    filled_prompt = fill_template_variables(template_content, main_keyword["keyword"], lsi_keywords)
    print("✅ 成功填充模板变量")
    
    # 5. 生成文件名
    filename = generate_filename(main_keyword["keyword"], template_file.stem)
    print(f"✅ 生成文件名: {filename}")
    
    # 6. 更新模板使用统计
    update_template_usage(keywords_data, template_file.name, filename)
    print("✅ 更新模板使用统计")
    
    # 7. 更新关键词状态
    if update_keyword_usage(keywords_data, main_keyword["keyword"], lsi_keywords, template_file.name):
        print("✅ 更新关键词状态")
    
    # 显示更新后的模板使用统计
    template_stats = keywords_data.get("template_usage_stats", {})
    print("📊 更新后模板使用统计:")
    for template_name, stats in template_stats.items():
        marker = " 👈" if template_name == template_file.name else ""
        print(f"   - {template_name}: {stats['usage_count']} 次{marker}")
    
    # 8. 保存更新（可选，这里只是测试）
    # save_keywords(keywords_file, keywords_data)
    print("✅ 测试完成（未实际保存文件）")
    
    return True

if __name__ == "__main__":
    test_single_blog_generation()