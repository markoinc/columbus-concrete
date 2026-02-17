#!/usr/bin/env python3
"""
Generate location pages for Columbus Concrete Contractor
Cities within 60-minute drive of Columbus, OH organized by county
"""

import os
import re
from datetime import datetime

# Phone number and company info
PHONE = "614-902-3793"
COMPANY = "Columbus Concrete Contractor"
DOMAIN = "columbusconcretecontractor.co"

# Cities within 60-min drive of Columbus, organized by county
# Format: (city_name, county_name)
LOCATIONS = [
    # Franklin County (Core - Columbus metro)
    ("Bexley", "Franklin"),
    ("Canal Winchester", "Franklin"),
    ("Dublin", "Franklin"),
    ("Gahanna", "Franklin"),
    ("Grandview Heights", "Franklin"),
    ("Grove City", "Franklin"),
    ("Groveport", "Franklin"),
    ("Hilliard", "Franklin"),
    ("New Albany", "Franklin"),
    ("Pickerington", "Franklin"),
    ("Reynoldsburg", "Franklin"),
    ("Upper Arlington", "Franklin"),
    ("Westerville", "Franklin"),
    ("Whitehall", "Franklin"),
    ("Worthington", "Franklin"),
    ("Obetz", "Franklin"),
    ("Minerva Park", "Franklin"),
    ("Marble Cliff", "Franklin"),
    ("Brice", "Franklin"),
    ("Lockbourne", "Franklin"),
    ("Harrisburg", "Franklin"),
    ("Urbancrest", "Franklin"),
    ("Valleyview", "Franklin"),
    ("Lincoln Village", "Franklin"),
    ("Blacklick Estates", "Franklin"),
    
    # Delaware County (North)
    ("Delaware", "Delaware"),
    ("Powell", "Delaware"),
    ("Sunbury", "Delaware"),
    ("Westerville", "Delaware"),
    ("Lewis Center", "Delaware"),
    ("Galena", "Delaware"),
    ("Ashley", "Delaware"),
    ("Ostrander", "Delaware"),
    ("Shawnee Hills", "Delaware"),
    ("Orange", "Delaware"),
    ("Genoa", "Delaware"),
    
    # Licking County (East)
    ("Newark", "Licking"),
    ("Heath", "Licking"),
    ("Granville", "Licking"),
    ("Johnstown", "Licking"),
    ("Pataskala", "Licking"),
    ("Hebron", "Licking"),
    ("Buckeye Lake", "Licking"),
    ("Utica", "Licking"),
    ("Alexandria", "Licking"),
    ("Hanover", "Licking"),
    ("Kirkersville", "Licking"),
    ("St. Louisville", "Licking"),
    
    # Fairfield County (Southeast)
    ("Lancaster", "Fairfield"),
    ("Pickerington", "Fairfield"),
    ("Canal Winchester", "Fairfield"),
    ("Baltimore", "Fairfield"),
    ("Carroll", "Fairfield"),
    ("Millersport", "Fairfield"),
    ("Rushville", "Fairfield"),
    ("Bremen", "Fairfield"),
    ("Amanda", "Fairfield"),
    ("Pleasantville", "Fairfield"),
    ("West Rushville", "Fairfield"),
    
    # Madison County (West)
    ("London", "Madison"),
    ("Plain City", "Madison"),
    ("West Jefferson", "Madison"),
    ("Mount Sterling", "Madison"),
    ("South Solon", "Madison"),
    ("Midway", "Madison"),
    ("Summerford", "Madison"),
    ("Choctaw Lake", "Madison"),
    
    # Pickaway County (South)
    ("Circleville", "Pickaway"),
    ("Ashville", "Pickaway"),
    ("South Bloomfield", "Pickaway"),
    ("Commercial Point", "Pickaway"),
    ("Williamsport", "Pickaway"),
    ("Orient", "Pickaway"),
    ("Darbyville", "Pickaway"),
    ("Harrisburg", "Pickaway"),
    ("New Holland", "Pickaway"),
    ("Tarlton", "Pickaway"),
    
    # Union County (Northwest)
    ("Marysville", "Union"),
    ("Dublin", "Union"),
    ("Plain City", "Union"),
    ("Richwood", "Union"),
    ("Milford Center", "Union"),
    ("Magnetic Springs", "Union"),
    ("Raymond", "Union"),
    ("Unionville Center", "Union"),
    
    # Knox County (Northeast)
    ("Mount Vernon", "Knox"),
    ("Fredericktown", "Knox"),
    ("Centerburg", "Knox"),
    ("Danville", "Knox"),
    ("Gambier", "Knox"),
    ("Martinsburg", "Knox"),
    ("Bladensburg", "Knox"),
    ("Howard", "Knox"),
    
    # Morrow County (North-Northeast)
    ("Mount Gilead", "Morrow"),
    ("Cardington", "Morrow"),
    ("Edison", "Morrow"),
    ("Marengo", "Morrow"),
    ("Sparta", "Morrow"),
    ("Chesterville", "Morrow"),
    
    # Marion County (North)
    ("Marion", "Marion"),
    ("Caledonia", "Marion"),
    ("Waldo", "Marion"),
    ("Prospect", "Marion"),
    ("La Rue", "Marion"),
    ("Morral", "Marion"),
    
    # Logan County (Northwest)
    ("Bellefontaine", "Logan"),
    ("West Liberty", "Logan"),
    ("DeGraff", "Logan"),
    ("Russells Point", "Logan"),
    ("Lakeview", "Logan"),
    ("Zanesfield", "Logan"),
    
    # Ross County (South-Southwest)
    ("Chillicothe", "Ross"),
    ("Kingston", "Ross"),
    ("Frankfort", "Ross"),
    ("Clarksburg", "Ross"),
    ("Adelphi", "Ross"),
    
    # Fayette County (Southwest)
    ("Washington Court House", "Fayette"),
    ("Jeffersonville", "Fayette"),
    ("Bloomingburg", "Fayette"),
    ("Good Hope", "Fayette"),
    
    # Perry County (Southeast)
    ("New Lexington", "Perry"),
    ("Somerset", "Perry"),
    ("Crooksville", "Perry"),
    ("Thornville", "Perry"),
    ("Shawnee", "Perry"),
    
    # Hocking County (Southeast)
    ("Logan", "Hocking"),
    ("Laurelville", "Hocking"),
    ("Rockbridge", "Hocking"),
    ("Murray City", "Hocking"),
    
    # Champaign County (West)
    ("Urbana", "Champaign"),
    ("Mechanicsburg", "Champaign"),
    ("St. Paris", "Champaign"),
    ("North Lewisburg", "Champaign"),
    ("Woodstock", "Champaign"),
    
    # Clark County (West-Southwest)
    ("Springfield", "Clark"),
    ("New Carlisle", "Clark"),
    ("South Vienna", "Clark"),
    ("Enon", "Clark"),
    ("Tremont City", "Clark"),
]

def slugify(text):
    """Convert text to URL-friendly slug"""
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug)
    return slug.strip('-')

def create_location_page(city, county):
    """Create HTML content for a location page"""
    slug = slugify(city)
    
    # Create unique content for SEO
    services = [
        "Concrete Driveways",
        "Stamped Concrete Patios",
        "Concrete Foundations",
        "Sidewalks & Walkways",
        "Concrete Pool Decks",
        "Decorative Concrete",
        "Concrete Repair & Resurfacing",
        "Commercial Concrete Work"
    ]
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Concrete Contractor {city}, OH | {COMPANY}</title>
    <meta name="description" content="Professional concrete contractor serving {city}, {county} County, OH. Quality driveways, patios, foundations & more. Free estimates. Call {PHONE}!">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://{DOMAIN}/locations/{slug}/">
    <style>
        :root {{
            --primary: #f59e0b;
            --dark: #111827;
            --light: #f9fafb;
            --text: #374151;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body {{ max-width: 100%; overflow-x: hidden; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background: var(--light);
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        
        /* Header */
        header {{
            background: var(--dark);
            color: white;
            padding: 15px 0;
        }}
        .header-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }}
        .logo {{ font-size: 1.5rem; font-weight: 700; color: var(--primary); text-decoration: none; }}
        .phone-cta {{
            background: var(--primary);
            color: var(--dark);
            padding: 12px 24px;
            text-decoration: none;
            font-weight: 700;
            border-radius: 5px;
        }}
        .phone-cta:hover {{ background: #d97706; }}
        
        /* Hero */
        .hero {{
            background: linear-gradient(135deg, var(--dark) 0%, #1f2937 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
        }}
        .hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 20px;
            line-height: 1.2;
        }}
        .hero h1 span {{ color: var(--primary); }}
        .hero p {{
            font-size: 1.25rem;
            max-width: 700px;
            margin: 0 auto 30px;
            opacity: 0.9;
        }}
        .cta-btn {{
            display: inline-block;
            background: var(--primary);
            color: var(--dark);
            padding: 15px 40px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.1rem;
            border-radius: 5px;
            transition: transform 0.2s;
        }}
        .cta-btn:hover {{ transform: scale(1.05); background: #d97706; }}
        
        /* Services Section */
        .services {{
            padding: 80px 0;
            background: white;
        }}
        .section-title {{
            text-align: center;
            font-size: 2rem;
            margin-bottom: 50px;
            color: var(--dark);
        }}
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }}
        .service-card {{
            background: var(--light);
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            border: 2px solid transparent;
            transition: all 0.3s;
        }}
        .service-card:hover {{
            border-color: var(--primary);
            transform: translateY(-5px);
        }}
        .service-card h3 {{
            color: var(--dark);
            margin-bottom: 10px;
        }}
        
        /* About Section */
        .about {{
            padding: 80px 0;
            background: var(--dark);
            color: white;
        }}
        .about-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }}
        .about h2 {{
            font-size: 2rem;
            margin-bottom: 20px;
            color: var(--primary);
        }}
        .about ul {{
            list-style: none;
            margin-top: 20px;
        }}
        .about li {{
            padding: 10px 0;
            padding-left: 30px;
            position: relative;
        }}
        .about li:before {{
            content: "✓";
            color: var(--primary);
            position: absolute;
            left: 0;
            font-weight: bold;
        }}
        
        /* Areas Section */
        .areas {{
            padding: 80px 0;
            background: white;
        }}
        .areas-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
            margin-top: 30px;
        }}
        .areas-list a {{
            background: var(--light);
            color: var(--dark);
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            border: 1px solid #e5e7eb;
            transition: all 0.2s;
        }}
        .areas-list a:hover {{
            background: var(--primary);
            color: var(--dark);
            border-color: var(--primary);
        }}
        
        /* CTA Section */
        .cta-section {{
            padding: 80px 0;
            background: var(--primary);
            text-align: center;
        }}
        .cta-section h2 {{
            font-size: 2rem;
            color: var(--dark);
            margin-bottom: 20px;
        }}
        .cta-section p {{
            font-size: 1.25rem;
            color: var(--dark);
            margin-bottom: 30px;
        }}
        .cta-section .cta-btn {{
            background: var(--dark);
            color: white;
        }}
        .cta-section .cta-btn:hover {{ background: #374151; }}
        
        /* Footer */
        footer {{
            background: var(--dark);
            color: white;
            padding: 40px 0 20px;
        }}
        .footer-content {{
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 30px;
            margin-bottom: 30px;
        }}
        .footer-section h4 {{
            color: var(--primary);
            margin-bottom: 15px;
        }}
        .footer-section a {{
            color: #9ca3af;
            text-decoration: none;
            display: block;
            padding: 5px 0;
        }}
        .footer-section a:hover {{ color: var(--primary); }}
        .footer-bottom {{
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid #374151;
            color: #9ca3af;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 1.8rem; }}
            .about-content {{ grid-template-columns: 1fr; }}
            .header-content {{ justify-content: center; text-align: center; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="container header-content">
            <a href="/" class="logo">{COMPANY}</a>
            <a href="tel:{PHONE}" class="phone-cta">📞 {PHONE}</a>
        </div>
    </header>
    
    <section class="hero">
        <div class="container">
            <h1>Professional <span>Concrete Contractor</span> in {city}, OH</h1>
            <p>Serving {city} and {county} County with top-quality concrete work. From driveways to patios, foundations to decorative concrete — we deliver exceptional results.</p>
            <a href="tel:{PHONE}" class="cta-btn">Get Your Free Estimate</a>
        </div>
    </section>
    
    <section class="services">
        <div class="container">
            <h2 class="section-title">Our Concrete Services in {city}</h2>
            <div class="services-grid">
                <div class="service-card">
                    <h3>🚗 Concrete Driveways</h3>
                    <p>Durable, long-lasting driveways designed to handle Ohio weather and daily use.</p>
                </div>
                <div class="service-card">
                    <h3>🏡 Stamped Concrete Patios</h3>
                    <p>Beautiful decorative patios that enhance your outdoor living space.</p>
                </div>
                <div class="service-card">
                    <h3>🏗️ Concrete Foundations</h3>
                    <p>Solid foundations for residential and commercial construction projects.</p>
                </div>
                <div class="service-card">
                    <h3>🚶 Sidewalks & Walkways</h3>
                    <p>Safe, attractive walkways that improve your property's curb appeal.</p>
                </div>
                <div class="service-card">
                    <h3>🏊 Pool Decks</h3>
                    <p>Non-slip, stylish pool deck surfaces for your backyard oasis.</p>
                </div>
                <div class="service-card">
                    <h3>🔧 Concrete Repair</h3>
                    <p>Expert repair and resurfacing to extend the life of your concrete.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section class="about">
        <div class="container">
            <div class="about-content">
                <div>
                    <h2>Why Choose Us for Your {city} Concrete Project?</h2>
                    <p>We've been serving {county} County and the greater Columbus area with exceptional concrete work. Our team combines years of experience with modern techniques to deliver results that last.</p>
                    <ul>
                        <li>Licensed & Insured Professionals</li>
                        <li>Free, No-Obligation Estimates</li>
                        <li>Quality Materials & Craftsmanship</li>
                        <li>On-Time Project Completion</li>
                        <li>Competitive, Transparent Pricing</li>
                        <li>5-Star Customer Reviews</li>
                    </ul>
                </div>
                <div>
                    <h2>Serving {city} & Surrounding Areas</h2>
                    <p>As a local concrete contractor, we understand the unique needs of {city} homeowners and businesses. Whether you're in downtown {city} or the surrounding {county} County communities, we're here to help with all your concrete needs.</p>
                    <p style="margin-top: 20px;">Ready to start your project? Call us today at <strong style="color: var(--primary);">{PHONE}</strong> for a free estimate.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section class="areas">
        <div class="container">
            <h2 class="section-title">Other Areas We Serve Near {city}</h2>
            <div class="areas-list" id="nearby-areas">
                <!-- Will be populated with nearby locations -->
            </div>
            <p style="text-align: center; margin-top: 30px;"><a href="/locations/" style="color: var(--primary); font-weight: 600;">View All Service Areas →</a></p>
        </div>
    </section>
    
    <section class="cta-section">
        <div class="container">
            <h2>Ready to Start Your Concrete Project in {city}?</h2>
            <p>Get a free, no-obligation estimate from our experienced team.</p>
            <a href="tel:{PHONE}" class="cta-btn">📞 Call {PHONE} Now</a>
        </div>
    </section>
    
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>{COMPANY}</h4>
                    <p>Professional concrete services for {city}, OH and the greater Columbus area.</p>
                    <p style="margin-top: 15px;"><strong>📞 {PHONE}</strong></p>
                </div>
                <div class="footer-section">
                    <h4>Services</h4>
                    <a href="/">Concrete Driveways</a>
                    <a href="/">Stamped Concrete</a>
                    <a href="/">Foundations</a>
                    <a href="/">Commercial Concrete</a>
                </div>
                <div class="footer-section">
                    <h4>Service Areas</h4>
                    <a href="/locations/">All Locations</a>
                    <a href="/">Columbus, OH</a>
                    <a href="/locations/{slug}/">{city}, OH</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; {datetime.now().year} {COMPANY}. All rights reserved. | Serving {city}, {county} County & Central Ohio</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    return html

def create_locations_index():
    """Create the main locations index page organized by county"""
    # Organize locations by county
    counties = {}
    for city, county in LOCATIONS:
        if county not in counties:
            counties[county] = []
        if city not in [c for c, _ in counties[county]]:
            counties[county].append((city, slugify(city)))
    
    # Sort counties alphabetically
    sorted_counties = sorted(counties.keys())
    
    # Build county sections HTML
    county_sections = ""
    for county in sorted_counties:
        cities = sorted(counties[county], key=lambda x: x[0])
        city_links = "\n".join([
            f'                    <li><a href="/locations/{slug}/">{city}, OH</a></li>'
            for city, slug in cities
        ])
        county_sections += f'''
            <div class="county-section">
                <h2>{county} County</h2>
                <ul class="city-list">
{city_links}
                </ul>
            </div>'''
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Areas | {COMPANY} | Columbus, OH</title>
    <meta name="description" content="View all areas we serve. Professional concrete services throughout Central Ohio including Franklin, Delaware, Licking, Fairfield, and surrounding counties.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://{DOMAIN}/locations/">
    <style>
        :root {{
            --primary: #f59e0b;
            --dark: #111827;
            --light: #f9fafb;
            --text: #374151;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body {{ max-width: 100%; overflow-x: hidden; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background: var(--light);
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        
        header {{
            background: var(--dark);
            color: white;
            padding: 15px 0;
        }}
        .header-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }}
        .logo {{ font-size: 1.5rem; font-weight: 700; color: var(--primary); text-decoration: none; }}
        .phone-cta {{
            background: var(--primary);
            color: var(--dark);
            padding: 12px 24px;
            text-decoration: none;
            font-weight: 700;
            border-radius: 5px;
        }}
        
        .hero {{
            background: linear-gradient(135deg, var(--dark) 0%, #1f2937 100%);
            color: white;
            padding: 60px 0;
            text-align: center;
        }}
        .hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 15px;
        }}
        .hero h1 span {{ color: var(--primary); }}
        .hero p {{ font-size: 1.2rem; opacity: 0.9; }}
        
        .locations-grid {{
            padding: 60px 0;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }}
        
        .county-section {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        .county-section h2 {{
            color: var(--dark);
            font-size: 1.3rem;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 3px solid var(--primary);
        }}
        .city-list {{
            list-style: none;
            columns: 2;
            column-gap: 15px;
        }}
        .city-list li {{
            padding: 5px 0;
        }}
        .city-list a {{
            color: var(--text);
            text-decoration: none;
            transition: color 0.2s;
        }}
        .city-list a:hover {{
            color: var(--primary);
        }}
        
        .cta-section {{
            padding: 60px 0;
            background: var(--primary);
            text-align: center;
        }}
        .cta-section h2 {{
            font-size: 2rem;
            color: var(--dark);
            margin-bottom: 20px;
        }}
        .cta-btn {{
            display: inline-block;
            background: var(--dark);
            color: white;
            padding: 15px 40px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.1rem;
            border-radius: 5px;
        }}
        
        footer {{
            background: var(--dark);
            color: white;
            padding: 40px 0 20px;
            text-align: center;
        }}
        footer a {{
            color: var(--primary);
            text-decoration: none;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 1.8rem; }}
            .city-list {{ columns: 1; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="container header-content">
            <a href="/" class="logo">{COMPANY}</a>
            <a href="tel:{PHONE}" class="phone-cta">📞 {PHONE}</a>
        </div>
    </header>
    
    <section class="hero">
        <div class="container">
            <h1>Our <span>Service Areas</span></h1>
            <p>Professional concrete services throughout Central Ohio</p>
        </div>
    </section>
    
    <main>
        <div class="container locations-grid">
{county_sections}
        </div>
    </main>
    
    <section class="cta-section">
        <div class="container">
            <h2>Don't See Your City? Call Us Anyway!</h2>
            <p style="margin-bottom: 20px; color: var(--dark);">We serve all of Central Ohio. Give us a call to discuss your project.</p>
            <a href="tel:{PHONE}" class="cta-btn">📞 Call {PHONE}</a>
        </div>
    </section>
    
    <footer>
        <div class="container">
            <p><a href="/">{COMPANY}</a> | Columbus, OH | {PHONE}</p>
            <p style="margin-top: 10px; color: #9ca3af;">&copy; {datetime.now().year} All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''
    return html

def generate_sitemap():
    """Generate sitemap.xml with all pages"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    urls = [
        (f"https://{DOMAIN}/", "1.0", "weekly"),
        (f"https://{DOMAIN}/locations/", "0.9", "weekly"),
    ]
    
    # Add all location pages
    seen = set()
    for city, county in LOCATIONS:
        slug = slugify(city)
        if slug not in seen:
            urls.append((f"https://{DOMAIN}/locations/{slug}/", "0.7", "monthly"))
            seen.add(slug)
    
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url, priority, changefreq in urls:
        sitemap += f'''    <url>
        <loc>{url}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>{changefreq}</changefreq>
        <priority>{priority}</priority>
    </url>
'''
    
    sitemap += '</urlset>'
    return sitemap

def generate_robots():
    """Generate robots.txt"""
    return f'''User-agent: *
Allow: /

Sitemap: https://{DOMAIN}/sitemap.xml
'''

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    locations_dir = os.path.join(base_dir, 'locations')
    
    # Create locations directory
    os.makedirs(locations_dir, exist_ok=True)
    
    # Generate location pages
    seen_slugs = set()
    count = 0
    for city, county in LOCATIONS:
        slug = slugify(city)
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        
        city_dir = os.path.join(locations_dir, slug)
        os.makedirs(city_dir, exist_ok=True)
        
        html = create_location_page(city, county)
        with open(os.path.join(city_dir, 'index.html'), 'w') as f:
            f.write(html)
        count += 1
        print(f"Created: locations/{slug}/index.html")
    
    # Create locations index
    index_html = create_locations_index()
    with open(os.path.join(locations_dir, 'index.html'), 'w') as f:
        f.write(index_html)
    print("Created: locations/index.html")
    
    # Create sitemap
    sitemap = generate_sitemap()
    with open(os.path.join(base_dir, 'sitemap.xml'), 'w') as f:
        f.write(sitemap)
    print("Created: sitemap.xml")
    
    # Create robots.txt
    robots = generate_robots()
    with open(os.path.join(base_dir, 'robots.txt'), 'w') as f:
        f.write(robots)
    print("Created: robots.txt")
    
    print(f"\n✅ Generated {count} location pages + index + sitemap + robots.txt")
    return count

if __name__ == "__main__":
    main()
