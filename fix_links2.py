import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'<h3 class="text-lg font-bold mb-1">BrainIgnite Pro</h3>([\s\S]*?)<a href="#" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver en Play Store →</a>',
              r'<h3 class="text-lg font-bold mb-1">BrainIgnite Pro</h3>\1<a href="/brainignite/" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver Detalles →</a>', html)

html = re.sub(r'<h3 class="text-lg font-bold mb-1">Memory Quest</h3>([\s\S]*?)<a href="#" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver en Play Store →</a>',
              r'<h3 class="text-lg font-bold mb-1">Memory Quest</h3>\1<a href="/memory-quest/" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver Detalles →</a>', html)

html = re.sub(r'<h3 class="text-lg font-bold mb-1">Preserva</h3>([\s\S]*?)<a href="#" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver en Play Store →</a>',
              r'<h3 class="text-lg font-bold mb-1">Preserva</h3>\1<a href="/preserva/" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver Detalles →</a>', html)

html = re.sub(r'<h3 class="text-lg font-bold mb-1">WildCalm</h3>([\s\S]*?)<a href="#" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver en Play Store →</a>',
              r'<h3 class="text-lg font-bold mb-1">WildCalm</h3>\1<a href="/wildcalm/" class="text-blue-600 hover:text-blue-700 text-sm font-bold">Ver Detalles →</a>', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
