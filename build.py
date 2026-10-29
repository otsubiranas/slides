# Genera totes les pàgines. Canvia DOMAIN i executa: python3 build.py
import json, urllib.parse
DOMAIN = "https://www.stepupfigueres.com"
MAPS = "https://www.google.com/maps/place/Acad%C3%A8mia+StepUp+Figueres+-+Refor%C3%A7+escolar+i+t%C3%A8cniques+d%E2%80%99estudi/@42.2653494,2.9574993,17z/data=!3m1!4b1!4m6!3m5!1s0x12ba8df77e86be69:0xd10e5f0b00756602!8m2!3d42.2653455!4d2.9600742!16s%2Fg%2F11m7rr919g"
import os
PH = [("aula-1","Aula de reforç escolar de Step Up a Figueres"),("aula-2","Alumnes fent reforç escolar en un grup reduït"),("aula-3","Aula de Step Up amb grup reduït d'alumnes"),("biblioteca","Biblioteca de l'acadèmia Step Up"),("espai","Espai de treball de l'acadèmia Step Up")]
SUB = next((p for p in ("assets/logos-subvencio.png","assets/logos subvenció.png") if os.path.exists(p)), None)
def subv():
    return '<section aria-label="Entitats que ens donen suport" style="background:#fff;padding:1.5rem 0"><div class="wrap"><img src="%s" alt="Logotips de les entitats que subvencionen Step Up" loading="lazy" width="1200" style="width:100%%;height:auto;display:block"></div></section>' % SUB.replace(" ","%20") if SUB else ""
def herofoto():
    return '<div class="wrap" style="padding-top:2rem"><img src="assets/hero.png" alt="Aula de reforç escolar de Step Up a Figueres amb un grup reduït d\'alumnes" width="1200" height="480" style="width:100%%;height:min(30rem,50vw);min-height:14rem;object-fit:cover;border-radius:6px;display:block"></div>' if os.path.exists("assets/hero.png") else ""
def gallery():
    im="".join('<img src="assets/fotos/%s.jpeg" alt="%s" loading="lazy" style="border-radius:6px;width:100%%;height:14rem;object-fit:cover">'%(n,a) for n,a in PH if os.path.exists("assets/fotos/%s.jpeg"%n))
    return '<section class="block"><div class="wrap"><h2>L\'acadèmia per dins</h2><div class="grid">%s</div></div></section>'%im if im else ""
def exterior():
    return '<img src="assets/fotos/exterior.jpeg" alt="Façana de l\'acadèmia Step Up, al carrer Sant Josep de Figueres" loading="lazy" style="border-radius:6px;max-width:34rem;width:100%">' if os.path.exists("assets/fotos/exterior.jpeg") else ""
TEL = "677 62 55 34"; WA = "34677625534"
def wa(t="Hola! Voldria informació sobre Step Up."):
    return "https://wa.me/%s?text=%s" % (WA, urllib.parse.quote(t))
NAV = [("index.html","Inici"),("reforc-escolar.html","Reforç escolar"),("preparacio-examens.html","Preparació d'exàmens"),("extraescolars.html","Escoles i extraescolars"),("contacte.html","Contacte")]
def url(f): return DOMAIN + ("/" if f=="index.html" else "/"+f)
def page(f, title, desc, body, extra=""):
    nav = "".join('<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if h==f else "", t) for h,t in NAV)
    return f'''<!doctype html>
<html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url(f)}"><link rel="icon" href="assets/favicon.png">
<meta property="og:type" content="website"><meta property="og:locale" content="ca_ES"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url(f)}"><meta property="og:image" content="{DOMAIN}/assets/logo-cercle.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">{extra}</head><body>
<header class="site"><div class="wrap"><a href="index.html"><img src="assets/logo.png" alt="Step Up, formació & english school" width="116" height="44"></a>
<nav aria-label="Menú principal"><ul>{nav}</ul></nav></div></header>
<main>{body}</main>
{subv()}
<a class="btn wa-float" href="{wa()}" rel="noopener">Demana informació per WhatsApp</a>
<footer class="site"><div class="wrap">
<div><h2>Step Up, formació &amp; english school</h2><p>Acadèmia de reforç escolar a Figueres (Alt Empordà). Més de 30 anys ensenyant.</p></div>
<div><h2>Contacte</h2><p>C/ Sant Josep, 23, Figueres<br>WhatsApp i telèfon: <a href="tel:+{WA}">{TEL}</a><br><a href="{wa()}">Escriu-nos per WhatsApp</a></p></div>
<div><h2>Serveis</h2><p><a href="reforc-escolar.html">Reforç escolar</a><br><a href="preparacio-examens.html">Preparació d'exàmens</a><br><a href="extraescolars.html">Extraescolars i cursos</a></p></div>
</div></footer></body></html>'''
def cta(t="Vols saber quin grup t'encaixa?", p="Explica'ns el curs i les assignatures per WhatsApp i t'informem sense compromís."):
    return f'<section class="cta-band"><div class="wrap"><h2>{t}</h2><p>{p}</p><a class="btn" href="{wa()}" rel="noopener">Demana informació per WhatsApp</a></div></section>'
def hero(h1, lead): return f'<section class="page-hero"><div class="wrap"><h1>{h1}</h1><p class="lead">{lead}</p><a class="btn" href="{wa()}" rel="noopener">Demana informació</a></div></section>'
pages = {}

ld = json.dumps({"@context":"https://schema.org","@type":"EducationalOrganization","name":"Step Up formació & english school","url":DOMAIN+"/","logo":DOMAIN+"/assets/logo-cercle.png","telephone":"+"+WA,"description":"Acadèmia de reforç escolar a Figueres amb grups de màxim 4 alumnes.","address":{"@type":"PostalAddress","streetAddress":"Carrer de Sant Josep, 23","postalCode":"17600","addressLocality":"Figueres","addressRegion":"Girona","addressCountry":"ES"},"areaServed":{"@type":"AdministrativeArea","name":"Alt Empordà"},"foundingDate":"1996"}, ensure_ascii=False)
pages["index.html"] = page("index.html","Reforç escolar a Figueres | Grups de màxim 4 alumnes | Step Up","Acadèmia de reforç escolar a Figueres (Alt Empordà): màxim 4 alumnes per aula, primària, ESO i batxillerat, tot el currículum. Més de 30 anys d'experiència.", f'''
<section class="hero"><div class="wrap"><div>
<h1>Reforç escolar a Figueres, en grups de màxim 4 alumnes</h1>
<p class="lead">Totes les assignatures de primària, ESO i batxillerat, amb professors especialitzats en llengües, humanitats, matemàtiques, física i química.</p>
<div class="cta"><a class="btn" href="{wa()}" rel="noopener">Demana informació per WhatsApp</a><a class="btn alt" href="reforc-escolar.html">Veure el reforç escolar</a></div></div>
<div class="steps" aria-label="Step Up en xifres"><div class="step">Màxim 4 alumnes<small>per aula</small></div><div class="step">Més de 30 anys<small>ensenyant a Figueres</small></div><div class="step">5 centres de la comarca<small>treballen amb nosaltres</small></div></div></div></section>
{herofoto()}
<section class="block"><div class="wrap"><h2>Què fem a Step Up</h2><div class="grid">
<div><h3>Reforç escolar</h3><p>Suport en totes les assignatures, de primària a batxillerat, amb atenció gairebé individual.</p><a href="reforc-escolar.html">Més informació</a></div>
<div><h3>Preparació d'exàmens</h3><p>Exàmens de català, proves d'accés a la universitat, PAP i oposicions.</p><a href="preparacio-examens.html">Més informació</a></div>
<div><h3>Escoles i extraescolars</h3><p>Anglès, francès, àrab, mecanografia, dansa i més, a escoles i instituts de la comarca.</p><a href="extraescolars.html">Més informació</a></div></div></div></section>
{gallery()}<section class="block tint"><div class="wrap"><h2>Per què les famílies d'Alt Empordà ens trien</h2>
<p>Amb un màxim de quatre alumnes per aula, el professor veu què entén cada nen i cada jove, i què no. Fa més de 30 anys que ensenyem a Figueres, i avui treballem amb escoles i instituts de la comarca, com l'Escola Carme Guasch i l'Institut Ramon Muntaner.</p></div></section>
{cta()}''', f'<script type="application/ld+json">{ld}</script>')

pages["reforc-escolar.html"] = page("reforc-escolar.html","Reforç escolar a Figueres: primària, ESO i batxillerat | Step Up","Classes de reforç escolar a Figueres per a primària, ESO i batxillerat. Grups de màxim 4 alumnes i professors especialitzats en matemàtiques, llengües, física i química.", hero("Reforç escolar a Figueres per a primària, ESO i batxillerat","Grups de màxim 4 alumnes perquè ningú es quedi sense resoldre els dubtes.")+f'''
<section class="block"><div class="wrap"><h2>Totes les assignatures, tots els cursos</h2>
<p>Donem suport a l'alumnat de primària, ESO i batxillerat en qualsevol assignatura. Els grups són de màxim quatre alumnes, de manera que el professor pot adaptar el ritme a cada un.</p>
<div class="grid"><div><h3>Llengües</h3><p>Català, castellà i anglès.</p></div><div><h3>Humanitats</h3><p>Història, filosofia, geografia i ciències socials.</p></div><div><h3>Matemàtiques</h3><p>Des del càlcul de primària fins a les matemàtiques de batxillerat.</p></div><div><h3>Física i química</h3><p>Professors especialitzats en ciències per a ESO i batxillerat.</p></div></div></div></section>
<section class="block tint faq"><div class="wrap"><h2>Preguntes freqüents</h2>
<details><summary>Quants alumnes hi ha per aula?</summary><p>Com a màxim quatre.</p></details>
<details><summary>Quins cursos atenem?</summary><p>Primària, ESO i batxillerat.</p></details>
<details><summary>Quines assignatures puc reforçar?</summary><p>Totes, anglès inclòs. Tenim professors especialitzats en llengües, humanitats, matemàtiques, física i química.</p></details>
<details><summary>Com puc demanar informació?</summary><p>Escriu-nos per WhatsApp al {TEL} i t'ho expliquem.</p></details></div></section>
{cta()}''')

pages["preparacio-examens.html"] = page("preparacio-examens.html","Preparació d'exàmens a Figueres: català, selectivitat, PAP i oposicions | Step Up","Preparació d'exàmens de català, proves d'accés a la universitat, PAP i oposicions a Figueres, amb grups reduïts i professors especialitzats.", hero("Preparació d'exàmens a Figueres","Català, accés a la universitat, PAP i oposicions, en grups reduïts.")+f'''
<section class="block"><div class="wrap"><div class="grid">
<div><h3>Exàmens de català</h3><p>Preparació per als exàmens de llengua catalana.</p></div>
<div><h3>Accés a la universitat</h3><p>Preparació de les proves d'accés a la universitat (selectivitat).</p></div>
<div><h3>PAP</h3><p>Preparació de la prova d'accés als cicles formatius de grau superior.</p></div>
<div><h3>Oposicions</h3><p>Suport en la preparació d'oposicions.</p></div></div>
<p style="margin-top:2rem">Treballem en grups de màxim quatre persones amb professors especialitzats. Si no ets segur de quina preparació necessites, pregunta-ho per WhatsApp.</p></div></section>
{cta("Tens un examen a la vista?","Digue'ns quin i quan, i t'expliquem com et podem ajudar.")}''')

pages["extraescolars.html"] = page("extraescolars.html","Extraescolars per a escoles, AFA i ajuntaments de l'Alt Empordà | Step Up","Organitzem activitats extraescolars a escoles i instituts de l'Alt Empordà: anglès, francès, àrab, mecanografia, dansa. Cursos de català A1 i tallers de deures. Demana pressupost.", hero("Activitats extraescolars per a escoles, instituts, AFA i ajuntaments","Portem l'activitat, els professors i la gestió. Vosaltres només heu de triar què voleu.")+f'''
<section class="block"><div class="wrap"><h2>Què podem organitzar</h2><div class="grid">
<div><h3>Extraescolars a l'escola</h3><p>Anglès, francès, àrab, mecanografia, dansa i més, dins del centre.</p></div>
<div><h3>Cursos de català A1</h3><p>Cursos de català per a persones adultes.</p></div>
<div><h3>Tallers de deures</h3><p>Tallers de deures en espais joves.</p></div>
<div><h3>Formacions a mida</h3><p>Dissenyem la formació que necessiteu.</p></div></div>
<p style="margin-top:2rem">Treballem amb cinc escoles i instituts de la comarca, com l'Escola Carme Guasch i l'Institut Ramon Muntaner.</p></div></section>
<section class="block tint"><div class="wrap"><h2>Demana pressupost</h2><p>Omple el formulari i s'obrirà un missatge de WhatsApp preparat per enviar-nos.</p>
<form id="pres"><label>Entitat<input name="e" required placeholder="AFA, ajuntament o institut"></label>
<label>Tipus<select name="t"><option>AFA</option><option>Ajuntament</option><option>Institut</option><option>Escola</option><option>Altres</option></select></label>
<label>Activitat<input name="a" required placeholder="Per exemple, anglès o mecanografia"></label>
<label>Nombre aproximat d'alumnes<input name="n" inputmode="numeric"></label>
<button class="btn" type="submit">Demana pressupost per WhatsApp</button></form></div></section>
<script>document.getElementById("pres").addEventListener("submit",function(ev){{ev.preventDefault();var d=new FormData(ev.target);var m="Hola! Voldria un pressupost. Entitat: "+d.get("e")+" ("+d.get("t")+"). Activitat: "+d.get("a")+(d.get("n")?". Alumnes aprox.: "+d.get("n"):"")+".";window.open("https://wa.me/{WA}?text="+encodeURIComponent(m),"_blank","noopener")}})</script>''')

pages["contacte.html"] = page("contacte.html","Contacte | Step Up, reforç escolar a Figueres","Contacta amb Step Up, acadèmia de reforç escolar a Figueres, per WhatsApp o telèfon al 677 62 55 34.", hero("Contacta amb Step Up","Respon'ns per WhatsApp i t'informem de grups, horaris i cursos.")+f'''
<section class="block"><div class="wrap"><h2>Com trobar-nos</h2>
<p>WhatsApp i telèfon: <a href="tel:+{WA}">{TEL}</a></p>
<p>Adreça: c/ Sant Josep, 23, Figueres (Alt Empordà). <a href="{MAPS}" rel="noopener">Veure al mapa de Google</a></p>
{exterior()}
<p style="margin-top:1.5rem"><a class="btn" href="{wa()}" rel="noopener">Escriu-nos per WhatsApp</a></p></div></section>''')

for f,h in pages.items(): open(f,"w",encoding="utf-8").write(h)
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join("<url><loc>%s</loc></url>\n"%url(f) for f in pages)+"</urlset>\n")
open("CNAME","w").write("www.stepupfigueres.com\n")
open("robots.txt","w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n"%DOMAIN)
