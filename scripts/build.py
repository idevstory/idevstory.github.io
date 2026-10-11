"""Build the GitHub Pages site from editable Markdown and HTML templates."""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]

def fill(template, values):
    for key, value in values.items():
        template = template.replace('{{' + key + '}}', str(value))
    if re.search(r'\{\{\w+\}\}', template):
        raise ValueError('Unresolved template value')
    return template

def template(name):
    return (ROOT / 'templates' / name).read_text()

def chart():
    values = [12, 30, 21, 44, 26, 58, 49, 70, 111, 78, 81, 219, 248, 285, 509, 945]
    points = ' '.join(f'{10+i*20},{110-v/945*95:.1f}' for i,v in enumerate(values))
    return f'<svg class="growth-chart" viewBox="0 0 330 140" role="img" aria-label="原稿记录的连续 16 个观测值：日新增从 12 人起步，经历起伏后达到 945 人"><path d="M10 110H310" stroke="#d6d9ce"/><polygon points="10,110 {points} 310,110" fill="#e2e6d6"/><polyline points="{points}" fill="none" stroke="#385448" stroke-width="2.5"/><circle cx="310" cy="15" r="4" fill="#ae4b35"/><text x="10" y="135">首日 12 人</text><text x="310" y="135" text-anchor="end">峰值 945 人</text></svg>'

raw = (ROOT / 'source/le-bobing.md').read_text()
blocks = raw.strip().split('\n\n')
title = blocks[0].removeprefix('# ')
intro = blocks[1]
content, toc = [], []
for block in blocks[2:]:
    if block.startswith('## '):
        heading = block[3:]
        anchor = f'section-{len(toc)+1}'
        content.append(f'<h2 id="{anchor}">{html.escape(heading)}</h2>')
        if heading == '中秋临近，增长加快了':
            content.append('<figure class="article-chart">' + chart() + '<figcaption>日新增用户的起伏与增长 · 按原稿 16 个观测值绘制</figcaption></figure>')
        toc.append(f'<a href="#{anchor}">{html.escape(heading)}</a>')
    else:
        content.append('<p>' + html.escape(block).replace('\n', '<br>') + '</p>')
read_time = max(1, round(len(raw) / 320))
display_title = re.sub(r'(\d+ 人)', r'<span class="title-value">\1</span>', html.escape(title))
shared = {'TITLE': display_title, 'INTRO': html.escape(intro), 'READ_TIME': read_time, 'CHART': chart(), 'TOC': ''.join(toc), 'CONTENT': '\n'.join(content)}
for name, path, prefix in [('home.html', 'index.html', './'), ('article.html', 'stories/le-bobing/index.html', '../../')]:
    body = fill(template(name), shared)
    page = fill(template('base.html'), {'PAGE_TITLE': '小迈讲故事' if name == 'home.html' else html.escape(title)+' · 小迈讲故事', 'DESCRIPTION': html.escape(intro), 'OG_TYPE': 'website' if name == 'home.html' else 'article', 'ROOT': prefix, 'BODY': body})
    (ROOT / path).write_text(page)
print('Built homepage and story article.')
