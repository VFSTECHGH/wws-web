import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Reemplazar Falcon
html = re.sub(r'href="#"([\s\S]*?)Descargar Gratis', r'href="https://play.google.com/store/apps/details?id=com.falcontextreading"\1Descargar en Google Play', html, count=1)

# Reemplazar Memoria de Elefante (el segundo Descargar Gratis)
html = re.sub(r'href="#"([\s\S]*?)Descargar Gratis', r'href="/memory-quest/"\1Más Información', html, count=1)

# Reemplazar Respira con Animales
html = re.sub(r'href="#"([\s\S]*?)Descargar en Google Play', r'href="/wildcalm/"\1Más Información', html)

# Nutricion
html = re.sub(r'<h3 class="text-2xl font-bold mb-3">Nutriva</h3>([\s\S]*?)href="#"([\s\S]*?)Descargar Gratis', r'<h3 class="text-2xl font-bold mb-3">Nutriva</h3>\1href="/nutriva/"\2Más Información', html)
html = re.sub(r'<h3 class="text-2xl font-bold mb-3">NutraOrigin</h3>([\s\S]*?)href="#"([\s\S]*?)Descargar Gratis', r'<h3 class="text-2xl font-bold mb-3">NutraOrigin</h3>\1href="/nutraorigin/"\2Más Información', html)
html = re.sub(r'<h3 class="text-2xl font-bold mb-3">Sabores de Chile</h3>([\s\S]*?)href="#"([\s\S]*?)Descargar Gratis', r'<h3 class="text-2xl font-bold mb-3">Sabores de Chile</h3>\1href="/sabores-de-chile/"\2Más Información', html)

# Ingles
html = re.sub(r'<h3 class="text-2xl font-bold">Inglés Básico 500</h3>([\s\S]*?)<button\n                            class="w-full bg-white text-blue-900 py-4 rounded-xl font-black text-lg hover:bg-blue-50 transition">DESCARGAR\n                            BETA</button>', 
              r'<h3 class="text-2xl font-bold">Inglés Básico 500</h3>\1<a href="/ingles-500/"\n                            class="block text-center w-full bg-white text-blue-900 py-4 rounded-xl font-black text-lg hover:bg-blue-50 transition">VER CURSO COMPLETO</a>', html)

# PAES
html = re.sub(r'<h3 class="text-xl font-bold mb-2">Competencia Lectora</h3>([\s\S]*?)<button\n                        class="w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold opacity-50 cursor-not-allowed">Inscripción\n                        Beta</button>',
              r'<h3 class="text-xl font-bold mb-2">Competencia Lectora</h3>\1<a href="/paes-lectora/" class="block text-center w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold hover:bg-slate-700">Ver Detalles</a>', html)
html = re.sub(r'<h3 class="text-xl font-bold mb-2">Matemática M1</h3>([\s\S]*?)<button\n                        class="w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold opacity-50 cursor-not-allowed">Inscripción\n                        Beta</button>',
              r'<h3 class="text-xl font-bold mb-2">Matemática M1</h3>\1<a href="/paes-matematica-m1/" class="block text-center w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold hover:bg-slate-700">Ver Detalles</a>', html)
html = re.sub(r'<h3 class="text-xl font-bold mb-2">Matemática M2</h3>([\s\S]*?)<button\n                        class="w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold opacity-50 cursor-not-allowed">Inscripción\n                        Beta</button>',
              r'<h3 class="text-xl font-bold mb-2">Matemática M2</h3>\1<a href="/paes-matematica-m2/" class="block text-center w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold hover:bg-slate-700">Ver Detalles</a>', html)
html = re.sub(r'<h3 class="text-xl font-bold mb-2">Ciencias – Biología</h3>([\s\S]*?)<button\n                        class="w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold opacity-50 cursor-not-allowed">Inscripción\n                        Beta</button>',
              r'<h3 class="text-xl font-bold mb-2">Ciencias – Biología</h3>\1<a href="/paes-ciencias-biologia/" class="block text-center w-full py-2 bg-slate-800 text-white rounded-lg text-sm font-bold hover:bg-slate-700">Ver Detalles</a>', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("✅ Enlaces actualizados en temp_github_web")
