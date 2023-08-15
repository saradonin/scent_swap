from scent_app.models import Brand

BRAND_LIST = ['Aaron Terence Hughes', 'Abdul Samad Al Qurashi', 'Abercrombie & Fitch', 'Acca Kappa', 'Acqua di Parma',
              'Adidas', 'Adolfo Dominguez', 'Aedes de Venustas', 'Aerin', 'Aēsop', 'Afnan Perfumes',
              'Agent Provocateur', 'Agonist', 'Aigner', 'Ajmal', 'Al Haramain', 'Al Rehab', 'Alexandre.J',
              'Alexandria Fragrances', 'Alfred Sung', 'Alkemia', 'AllSaints', 'Alyssa Ashley', 'Amouage Oman',
              'Amouroud', 'Anfas', 'Angel Schlesser', 'Anna Sui', 'Annayake', 'Annette Neuffer', 'Antonio Banderas',
              'Arabian Ouda', 'Aramis', 'Ard Al Zaafaran', 'Areej Le Doré', 'Argos', 'Ariana Grande', 'Armaf',
              'Atelier Cologne', 'Atelier des Ors', 'Atkinsons', 'Attar Collection', 'Avon', 'Axe / Lynx', 'Azzaro',
              'Azzedine Alaïa', 'Baldessarini', 'Balenciaga', 'Balmain', 'Banana Republic', 'Bath & Body Works',
              'bdk Parfums', 'Beaufort', 'Benetton', 'Bentley', 'Berdoues', 'Betty Barclay', 'Beyoncé', 'Bijan',
              'Billie Eilish', 'Biotherm', 'Birkholz', 'Black Phoenix Alchemy Lab', 'Blend Oud',
              'Boadicea the Victorious', 'Bogner', 'Bogue', 'Bohoboco', 'Bois 1920', 'Bon Parfumeur', 'Bond No. 9',
              'Bortnikoff', 'Bottega Veneta', 'Boucheron', 'Bourjois', 'Brecourt', 'Britney Spears', 'Brocard',
              'Bruno Banani', 'Brut (Unilever)', 'Burberry', 'Bvlgari', 'By Terry', 'Byredo', 'Cacharel', 'Câline',
              'Calvin Klein', 'Carner', 'Carolina Herrera', 'Caron', 'Carthusia', 'Cartier', 'Carven', 'Caudalie',
              'Celine', 'Cerruti', 'Chanel', 'Chloé', 'Chopard', 'Christian Lacroix', 'Christina Aguilera', 'Clarins',
              'Clean', 'Clinique', 'Clive Christian', 'Coach', 'Comme des Garçons', 'Commodity',
              'Comptoir Sud Pacifique', 'Costume National', 'Coty', 'Courrèges', 'Crabtree & Evelyn', 'Création Lamis',
              'Creed', 'Cristiano Ronaldo', 'Cuba', 'Curve / Liz Claiborne', 'Cyrus', "d'Orsay", 'D.S. & Durga',
              'Dana', 'Daniel Josier', 'David Beckham', 'Davidoff',
              'Demeter Fragrance Library / The Library Of Fragrance', 'Diesel', 'Dior', 'Diptyque', 'Dita von Teese',
              'DKNY / Donna Karan', 'Dolce & Gabbana', 'Douglas', 'Dsquared²', 'Duftanker MGO Duftmanufaktur',
              'Dunhill', 'Dusita', 'E. Coudray', 'Ed Hardy', 'Editions de Parfums Frédéric Malle', 'Eight & Bob',
              'Eisenberg', 'El Nabil', 'Electimuss', 'Elie Saab', 'Elizabeth and James', 'Elizabeth Arden',
              'Elizabeth Taylor', 'Ella K Parfums', 'Ellis Brooklyn', 'Emanuel Ungaro', 'English Laundry',
              'Ensar Oud / Oriscent', 'Ermenegildo Zegna', 'Escada', 'Escentric Molecules', 'Esprit', 'essence',
              'Essential Garden', 'Essential Parfums', 'Estēe Lauder', "Etat Libre d'Orange", 'Etro',
              'Evody Ex Nihilo', 'Farmacia SS. Annunziata', 'Federico Mahora', 'Fendi', 'Ferrari',
              'Filippo Sorcinelli', 'Floraïku', 'Floris', 'Fort & Manlé', 'Fragonard', 'Fragrance Du Bois',
              'Fragrance One', 'sca Bianchi', 'Franck Boclet', 'Franck Olivier', 'Frapin', 'Frau Tonis Parfum',
              'Gabriela Sabatini', 'Galimard', 'Gallagher Fragrances', 'Geo. F. Trumper', 'Geoffrey Beene',
              'George Gina & Lucy', 'Georges Rech', 'Ghost', 'Gianfranco Ferré', 'Giardino Benessere',
              'Giorgio Armani', 'Giorgio Beverly Hills', 'Gisada', 'Givenchy', 'Gloria Vanderbilt',
              'Goldfield & Banks', 'Goutal', 'Grès', 'Gritti', 'Grossmith', 'Gucci', 'Guerlain', 'Guess',
              'Guy Laroche', 'H&M', 'Halloween', 'Halston', 'Hanae Mori', 'Haute Fragrance Company', 'Heeley',
              'Helmut Lang', 'Henry Jacques', 'Hermès', 'Hilde Soliani Profumi', 'Hiram Green', 'Histoires de Parfums',
              'Hollister', 'Houbigant', 'House of Matriarch', 'House of Sillage', 'Hugo Boss', 'Humiecki & Graef',
              'Iceberg', 'ID Parfums / Isabel Derroisné', 'Il Profvmo', 'Imaginary Authors', 'Initio', 'Isabey',
              'Issey Miyake', 'J.F. Schwarzlose Berlin', 'Jacomo', 'Jacques Bogart', 'Jacques Fath', 'Jacques Zolty',
              'Jaguar', 'James Bond 007', 'Jean Patou', 'Jean Paul Gaultier', 'Jean-Charles Brosseau',
              'Jean-Louis Scherrer', 'Jeanne Arthes', 'Jeanne en Provence', 'Jennifer Lopez', 'Jeroboam',
              'Jessica Simpson', 'Jesus del Pozo', 'Jette Joop', 'Jil Sander', 'Jimmy Choo', 'Jo Malone',
              'John Galliano', 'John Varvatos', 'Joop!', 'Jōvan', 'Jovoy', 'Judith Williams', 'Juicy Couture',
              'Jul et Mad', 'Juliette Has A Gun', 'Kajal', 'Karl Lagerfeld', 'KatyPerry', 'Kayali', 'Keiko Mecheri',
              'Kelsey Berwin', 'Kemi / Al Kimiya', 'Kenneth Cole', 'Kenzo', 'Kerosene', "Kiehl's", 'Kilian', 'Kiton',
              'KKW Fragrance / Kim Kardashian', 'Knize', 'Korloff', 'Korres', 'Krizia', "L'Artisan Parfumeur",
              "L'Erbolario", "L'Occitane en Provence", 'L.T. Piver', 'La Maison de la Vanille', 'La Martina',
              'La Perla', 'La Prairie', 'La Rive', 'Laboratorio Olfattivo', 'Lacoste', 'Lady Gaga', 'Lalique',
              'Lancaster', 'Lancôme', 'Lanvin', 'Lattafa', 'Laura Biagiotti', 'Laura Mercier', 'Le Couvent',
              'Le Galion', 'Le Labo', 'Léonard', 'Les Indémodables', 'Les Parfums de Rosine',
              'Les Senteurs Gourmandes', 'Lidl', 'Ligne St Barth', 'Liquides Imaginaires', 'LM Parfums', 'Loewe',
              'Lolita Lempicka', 'Lomani', 'Lorenzo Pazzaglia', 'Lorenzo Villoresi', 'Louis Varel', 'Louis Vuitton',
              'LPDO', 'LR / Racine', 'Lubin', 'Lush / Cosmetics To Go', 'M. Asam', 'M. Micallef', 'Madonna',
              'Maison Anthony Marmin / Abdul Karim Al Faransi', 'Maison Crivelli', 'Maison Francis Kurkdjian',
              'Maison Margiela', 'Maison Mona di Orio', 'Maison Tahité', 'Maître Parfumeur et Gantier',
              'Majda Bekkali', 'Malizia', 'Mancera', 'Mandarina Duck', 'Marbert', 'Marc Gebauer', 'Marc Jacobs',
              'Marc-Antoine Barrois', 'Maria Candida Gentile', 'Mariah Carey', 'Masakï Matsushïma', 'Masque',
              'Matière Première', 'Mauboussin', 'Mäurer & Wirtz', 'Mazzolari', 'MCM', 'Memo Paris', 'Mendittorosa',
              'Mercedes-Benz', 'Mexx', 'Michael Kors', 'Michalsky', 'Miller Harris',
              'Milton-Lloyd / Jean Yves Cosmetics', 'Miro', 'Missoni', 'Mizensir', 'Molinard', 'Molton Brown',
              'Monotheme', 'Montale', 'Montana', 'Montblanc', 'Moresque', 'Moschino', 'Mugler', 'Mülhens', 'Myrurgia',
              'M∙A∙C', 'N', 'Nabeel', 'Naomi Campbell', 'Naomi Goodsir', 'Narciso Rodriguez', 'Nasomatto', 'Natura',
              'Nature Blossom / Juniper Lane', 'Nautica', 'Navitus Parfums', 'Nest', 'Nikos', 'Nina Ricci', 'Nishane',
              'NIVEA', 'Nobile 1942', 'Nóvaya Zaryá', 'Nuxe', 'O Boticário', 'Odin New York', 'Ojar',
              'Olfactive Studio', 'Olympic Orchids Artisan Perfumes', 'Omerta', 'Omnia Profumi', 'Orientica',
              'Oriflame', 'Oriza L. Legrand', 'Ormonde Jayne', 'Orodion', 'Orto Parisi', 'Oscar de la Renta',
              'Otto Kern', 'Pacifica', 'Paco Rabanne', 'Paloma Picasso', 'Pana Dora', 'Papillon Artisan Perfumes',
              "Parfum d'Empire", 'Parfum-Individual Harry Lehmann', 'Parfums de Marly', 'Parfums de Nicolaï',
              'Parfums MDCI', 'Parfums Vintage', 'Paris Hilton', 'Parle Moi de Parfum', 'Pascal Morabito',
              'Paul Smith', "Penhaligon's", 'pernoire', 'Perris Monte Carlo Monaco', 'Perry Ellis', 'Phaedon',
              'Philosophy', 'Pierre Cardin', 'Pierre Guillaume', 'Pineward', 'Pink Sugar', 'Pino Silvestre', 'Playboy',
              'Police', 'Prada', 'Prin', 'Procter & Gamble', 'Profumi del Forte', 'Profumum Roma', 'Puig', 'Puma',
              'Puredistance Netherlands', 'R', 'Ralph Lauren', 'Rammstein', 'Ramón Monegal', 'Rancé 1795', 'Rasasi',
              'Real Time Netherlands', 'Réminiscence Monaco', 'Replay', 'Revlon / Charles Revson', 'Reyane Tradition',
              'Rihanna', 'Rituals Netherlands', 'Robert Piguet', 'Roberto Capucci', 'Roberto Cavalli',
              'Roberto Ugolini', 'Rochas', 'Roger & Gallet', 'Rogue', 'Roja Parfums', 'Room 1015',
              'Rosendo Mateu - Olfactive Expressions', 'Royal Crown', 'RP', 'Rue Broca', 'S', 's.Oliver',
              'S.T. Dupont', 'Salvador Dali', 'Salvatore Ferragamo', 'Santa Maria Novella', 'Sarah Jessica Parker',
              'ScentStory', 'Sean John', 'Serge Lutens', 'Shay & Blue', 'Shiseido / 資生堂 Japan', 'Simone Andreoli',
              'Sisley', 'Slava Zaïtsev Russia', 'Slumberhouse', 'Sol de Janeiro Brazil', 'Solinotes', 'soOud',
              'Sora Dora', 'Spirit', 'Stella McCartney', 'Stéphane Humbert Lucas', 'Strangers Parfumerie',
              'Sultan Pasha Attars', 'Swiss Arabian', 'Sylvaine Delacourte', 'T', 'Taif Al-Emarat / طيف الإمارات',
              'Tauer Perfumes', 'Tauerville', 'Ted Lapidus', 'Téo Cabanel', 'Teone Reinthal Natural Perfume',
              "Tesori d'Oriente", 'Thameen', 'The Body Shop', 'The Different Company',
              'The Dua Brand / Dua Fragrances', 'The House of Oud', 'The Merchant Of Venice', 'The Nose Behind',
              'The Woods Collection', 'Theodoros Kalotinis', 'Tiffany & Co.', 'Tiziana Terenzi', 'Tokyomilk',
              'Tom Ford', 'Tom Tailor', 'Tommy Bahama', 'Tommy Hilfiger', 'Toni Gard', 'Tous', 'Trussardi',
              'Ulric de Varens', 'Une Nuit Nomade', 'Unic', "Unique'e Luxury", 'V Canto', 'Valentino',
              'Van Cleef & Arpels', 'Vera Wang', 'Versace', "Victoria's Secret", 'Viktor & Rolf', 'Vilhelm Parfumerie',
              'Vince Camuto', 'Vivienne Westwood', 'Weil', 'What We Do Is Secret / A Lab on Fire',
              'Widian / AJ Arabia', 'Worth', 'XerJoff', 'Yardley', 'Yohji Yamamoto', 'Yves de Sistelle', 'Yves Rocher',
              'Yves Saint Laurent', 'Zadig & Voltaire', 'Zaharoff', 'Zara', 'Zarkoperfume', 'Zoologist']


def delete_brands():
    Brand.objects.all().delete()


def create_brands():
    for brand in BRAND_LIST:
        if not Brand.objects.filter(name=brand).exists():
            Brand.objects.create(name=brand)
