from flask import render_template
from pkg import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pharmacist')
def pharmacist():
    return render_template('pharmacist.html')

@app.route('/investors')
def investors():
    return render_template('investors.html')

@app.route('/inventory')
def inventory():
    # Pre-curated A-Z list of common pharmacy and store items
    store_items = {
        'A': ['Aspirin', 'Antacids', 'Allergy Relief', 'Antibiotic Ointment', 'Aloe Vera Gel', 'Alcohol Swabs'],
        'B': ['Band-Aids', 'Body Wash', 'Blood Pressure Monitors', 'Baby Formula', 'Baby Wipes', 'Batteries'],
        'C': ['Cough Syrup', 'Cold Medicine', 'Cotton Swabs', 'Contact Lens Solution', 'Conditioner'],
        'D': ['Deodorant', 'Dental Floss', 'Diapers', 'Dietary Supplements', 'Digestive Aids'],
        'E': ['Eye Drops', 'Ear Drops', 'Epsom Salt', 'Energy Drinks', 'Essential Oils'],
        'F': ['First Aid Kits', 'Face Wash', 'Feminine Hygiene Products', 'Foot Care', 'Flu Medicine'],
        'G': ['Glucose Meters', 'Gauze Pads', 'Glycerin', 'Greeting Cards', 'Gum & Mints'],
        'H': ['Hand Sanitizer', 'Hair Care', 'Heating Pads', 'Humidifiers', 'Homeopathic Remedies'],
        'I': ['Ibuprofen', 'Ice Packs', 'Incontinence Products', 'Insect Repellent', 'Inhalers (Over-the-counter)'],
        'J': ['Joint Supplements', 'Jelly Beans (Glucose)', 'Juice (Healthy Options)'],
        'K': ['Knee Braces', 'Ketosis Strips', 'Kids Vitamins'],
        'L': ['Laxatives', 'Lip Balm', 'Lozenges', 'Lotions', 'Liquid Bandages'],
        'M': ['Multivitamins', 'Mouthwash', 'Muscle Rubs', 'Medical Masks', 'Makeup Remover'],
        'N': ['Nasal Spray', 'Nail Care', 'Nursing Pads', 'Nutrition Shakes', 'Nicotine Patches'],
        'O': ['Oral Rehydration Salts', 'Omega-3 Oils', 'Orthopedic Supports', 'Over-the-counter Pain Relief'],
        'P': ['Pain Relievers', 'Pregnancy Tests', 'Probiotics', 'Protein Powder', 'Pet Care (Basic)'],
        'Q': ['Q-Tips', 'Quitting Smoking Aids', 'Quick-Read Thermometers'],
        'R': ['Reading Glasses', 'Rubbing Alcohol', 'Razor Blades', 'Rash Creams', 'Rehydration Solutions'],
        'S': ['Sunscreen', 'Shampoo', 'Syringes (Insulin)', 'Sleep Aids', 'Snacks & Beverages'],
        'T': ['Thermometers', 'Toothpaste', 'Toothbrushes', 'Tissues', 'Throat Sprays'],
        'U': ['Ulcer Medication (OTC)', 'Urea Creams', 'Urinalysis Test Strips'],
        'V': ['Vitamins', 'Vapor Rub', 'Vaginal Creams', 'Veterinary Supplies (Basic)'],
        'W': ['Water (Bottled/Distilled)', 'Wart Removers', 'Weight Loss Supplements', 'Wound Care'],
        'X': ['Xylitol Mints/Gum'],
        'Y': ['Yeast Infection Treatments', 'Yoga Mats (Wellness)'],
        'Z': ['Zinc Supplements', 'ZzzQuil (Sleep Aids)']
    }
    
    # Sort the dictionary strictly by letter just in case
    sorted_inventory = dict(sorted(store_items.items()))

    return render_template('inventory.html', inventory=sorted_inventory)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/legal')
def legal():
    return render_template('legal.html')

# Custom Error Handling for Production
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
