import os
import shutil

# Lista de las 14 apps faltantes con sus metadatos
apps = [
    {"id": "paes-lectora", "title": "PAES Competencia Lectora - Simulador", "desc": "Prepárate para la PAES de Lenguaje con ensayos DEMRE. IA local sin conexión.", "pkg": "com.wws.paeslectora", "cat": "EducationalApplication"},
    {"id": "paes-matematica-m1", "title": "PAES Matemática M1 - Simulador", "desc": "Ensaya la prueba M1 obligatoria con cronómetro y explicaciones paso a paso.", "pkg": "com.wws.paesmatematica1", "cat": "EducationalApplication"},
    {"id": "paes-matematica-m2", "title": "PAES Matemática M2 - Electiva", "desc": "Asegura tu puntaje en carreras STEM. Ensayos DEMRE actualizados.", "pkg": "com.wws.paesmatematica2", "cat": "EducationalApplication"},
    {"id": "ingles-1000", "title": "1000 Flashcards - Vocabulario Básico", "desc": "Expande tu vocabulario en inglés usando el sistema SRS. A2 Nivel CEFR.", "pkg": "com.wws.a1000flashcard", "cat": "EducationalApplication"},
    {"id": "ingles-1500", "title": "1500 Flashcards - Vocabulario B1", "desc": "Sube al nivel intermedio de inglés con 1500 palabras esenciales.", "pkg": "com.wws.a1500flashcard", "cat": "EducationalApplication"},
    {"id": "ingles-2000", "title": "2000 Flashcards - Vocabulario B1+", "desc": "Domina el inglés intermedio con repetición espaciada inteligente.", "pkg": "com.wws.a2000flashcard", "cat": "EducationalApplication"},
    {"id": "ingles-2500", "title": "2500 Flashcards - Vocabulario B2", "desc": "Preparación para el First Certificate (FCE) y nivel avanzado temprano.", "pkg": "com.wws.a2500flashcard", "cat": "EducationalApplication"},
    {"id": "ingles-3000", "title": "3000 Flashcards - Vocabulario B2+", "desc": "Entiende el 95% de las conversaciones cotidianas y series en inglés.", "pkg": "com.wws.a3000flashcard", "cat": "EducationalApplication"},
    {"id": "ingles-3500", "title": "3500 Flashcards - Vocabulario C1", "desc": "Vocabulario avanzado para IELTS, TOEFL y entornos corporativos.", "pkg": "com.wws.a3500flashcard", "cat": "EducationalApplication"},
    {"id": "ingles-4000", "title": "4000 Flashcards - Master C2", "desc": "El nivel de maestría final. Domina el idioma a nivel nativo culto.", "pkg": "com.wws.a4000flashcard", "cat": "EducationalApplication"},
    {"id": "wildcalm", "title": "WildCalm - Respiración Coherente", "desc": "Relaja tu mente con paisajes chilenos y ejercicios de coherencia cardíaca.", "pkg": "com.wws.wildcalmchile", "cat": "HealthAndFitnessApplication"},
    {"id": "sabores-de-chile", "title": "Sabores de Chile - Recetario Offline", "desc": "Aprende a cocinar los clásicos chilenos paso a paso sin conexión a internet.", "pkg": "com.wws.saboresdechile", "cat": "LifestyleApplication"},
    {"id": "preserva", "title": "Preserva - Guía de Supervivencia", "desc": "Manual de conservación y supervivencia en la naturaleza, totalmente offline.", "pkg": "com.wws.preserva", "cat": "LifestyleApplication"},
    {"id": "examen-conducir", "title": "Examen de Conducir Chile", "desc": "Simulador oficial con las últimas preguntas de CONASET para tu licencia.", "pkg": "com.wws.examenconducir", "cat": "EducationalApplication"},
]

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, "falcon")

# 1. GENERAR CARPETAS E INDEX.HTML
for app in apps:
    app_dir = os.path.join(base_dir, app["id"])
    os.makedirs(app_dir, exist_ok=True)
    
    # Copiar assets estáticos del template (CSS, JS si existen)
    for f in ["styles.css", "app.js"]:
        src = os.path.join(template_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(app_dir, f))
    
    # Leer template HTML
    with open(os.path.join(template_dir, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()
        
    # Reemplazar metaetiquetas dinámicamente
    html = html.replace("Falcon Speed Reader - Lee hasta 2.000 palabras por minuto", app["title"])
    html = html.replace("Multiplica tu velocidad de lectura y mejora tu comprensión con Falcon Speed Reader. 100% Offline, sin rastreos y 34 libros gratis incluidos.", app["desc"])
    html = html.replace("Falcon Speed Reader", app["title"].split("-")[0].strip())
    html = html.replace("com.falcontextreading", app["pkg"])
    
    # Pequeños ajustes en la UI para no repetir lo mismo
    html = html.replace("Desbloquea tu verdadero <span class=\"text-gradient\">potencial de lectura</span>", f"Descubre tu verdadero <span class=\"text-gradient\">potencial</span>")
    html = html.replace("Lee al doble de velocidad con la técnica RSVP. Soporte para PDF, ePub, y 34 libros clásicos gratuitos integrados. 100% offline y sin distracciones.", app["desc"])
    
    with open(os.path.join(app_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"✅ Generado: {app['id']}/index.html")

# 2. GENERAR ROBOTS.TXT
robots_content = """User-agent: *
Allow: /
Sitemap: https://wws.cl/sitemap.xml
"""
with open(os.path.join(base_dir, "robots.txt"), "w") as f:
    f.write(robots_content)
print("✅ Generado: robots.txt")

# 3. GENERAR SITEMAP.XML PARA LAS 26 APPS
all_apps = apps + [
    {"id": "falcon"}, {"id": "ingles-500"}, {"id": "paes-ciencias-biologia"},
    {"id": "paes-ciencias-fisica"}, {"id": "paes-ciencias-quimica"},
    {"id": "paes-ciencias-tp"}, {"id": "paes-historia"}, {"id": "brainignite"},
    {"id": "nutraorigin"}, {"id": "nutriva"}, {"id": "memory-quest"}, {"id": "lautaro-training"}
]

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_xml += '  <url>\n    <loc>https://wws.cl/</loc>\n    <priority>1.00</priority>\n  </url>\n'

for a in all_apps:
    sitemap_xml += f'  <url>\n    <loc>https://wws.cl/{a["id"]}/</loc>\n    <priority>0.80</priority>\n  </url>\n'

sitemap_xml += '</urlset>'

with open(os.path.join(base_dir, "sitemap.xml"), "w") as f:
    f.write(sitemap_xml)
print("✅ Generado: sitemap.xml")
