import re

def rewrite_css(css_content):
    # Base replacements for root
    new_root = """    :root {
      --blue-main:    #0B3D91;
      --blue-accent:  #1E5AB6;
      --panel-bg:     rgba(255, 255, 255, 0.6);
      --panel-border: rgba(255, 255, 255, 0.5);
      --text-main:    #1E293B;
      --text-muted:   #475569;
      --transition:   0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }"""
    css_content = re.sub(r':root\s*\{[^}]+\}', new_root, css_content)

    # Body replacements
    new_body = """    body {
      font-family: 'Inter', -apple-system, sans-serif;
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      background: linear-gradient(-45deg, #F0F4FF, #E2EAFD, #FAFBFF, #E8F0FA);
      background-size: 400% 400%;
      animation: ambientGradient 15s ease infinite;
      position: relative;
    }
    body::before, body::after {
      content: '';
      position: fixed; width: 600px; height: 600px;
      border-radius: 50%; z-index: 0; filter: blur(100px); opacity: 0.6;
      animation: floatOrbs 20s infinite ease-in-out alternate; pointer-events: none;
    }
    body::before { background: rgba(74, 144, 226, 0.22); top: -150px; left: -100px; }
    body::after { background: rgba(255, 180, 0, 0.1); bottom: -150px; right: -100px; animation-delay: -10s; }

    @keyframes ambientGradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    @keyframes floatOrbs {
      0% { transform: translate(0, 0) scale(1); }
      100% { transform: translate(120px, 150px) scale(1.15); }
    }"""
    css_content = re.sub(r'body\s*\{[^}]+\}', new_body, css_content)
    
    # Update panel class properties
    css_content = css_content.replace('backdrop-filter: blur(12px);', 'backdrop-filter: blur(20px) saturate(160%); -webkit-backdrop-filter: blur(20px) saturate(160%); box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);')
    css_content = css_content.replace('backdrop-filter: blur(16px);', 'backdrop-filter: blur(24px) saturate(160%); -webkit-backdrop-filter: blur(24px) saturate(160%); box-shadow: 0 8px 40px rgba(0, 0, 0, 0.08);')
    
    # Add glassmorphism to form container
    if '.container {' in css_content:
        css_content = re.sub(r'\.container\s*\{[^}]+\}', 
                             r'.container { width: 100%; background: var(--panel-bg); padding: 40px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); border: 1px solid var(--panel-border); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); position: relative; z-index: 1; }', 
                             css_content)

    return css_content

files = ['f:/DAV UNI PROJECT/index.html', 'f:/DAV UNI PROJECT/register.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'<style>(.*?)</style>', content, flags=re.DOTALL)
    if match:
        old_css = match.group(1)
        new_css = rewrite_css(old_css)
        content = content[:match.start(1)] + new_css + content[match.end(1):]
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
