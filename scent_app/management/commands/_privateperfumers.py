from scent_app.models import Perfumer

PERFUMERS_LIST = ['Aaron Terence Hughes', 'Adilson Rato', 'Adriana Medina-Baez', 'Aime Guerlain', 'Akiko Kamei',
                  'Alain Alchenberger', 'Alain Allione', 'Alain Astori', 'Albert Hauck', 'Alberto Morillas',
                  'Alessandro Gualtieri', 'Alex Lee', 'Alexandra Carlin', 'Alexandra Jouet', 'Alexandra Kalle',
                  'Alexandra Kosinski', 'Alexandra Monet', 'Alexandre Illan', 'Alexis Dadier', 'Alexis Grugeon',
                  'Ali Aljaberi', 'Alienor Massenet', 'Amandine Clerc-Marie', 'Amelie Bourgeois', 'Amelie Jacquin',
                  'Anais Biguine', 'Anatole Lebreton', 'Andre Fraysse', 'Andre Fromentin', 'Andrea Casotti',
                  'Andrea Lupo', 'Andreas Wilhelm', 'Andy Tauer', 'Ane Ayo', 'Angela Ciampagna', 'Angela St.John',
                  'Angela Stavrevska', 'Angeline Poubeau Leporini', 'Angelo Orazio Pregoni', 'Ann Gottlieb',
                  'Anna Zworykina', 'Anne Flipo', 'Anne-Cecile Douveghan', 'Anne-Sophie Behaghel', 'Annick Goutal',
                  'Annick Menardo', 'Annie Buzantian', 'Antoine Lie', 'Antoine Maisondieu', 'Antonina Vitkovskaya',
                  'Antonio Alessandria', 'Antonio Gardoni', 'Antonio Visconti', 'Arnaud Poulain', 'Arturetto Landi',
                  'Auguste Michel', 'Aurelien Guichard', 'Barbara Zoebelein', 'Barnabe Fillion', 'Beatrice Piquet',
                  'Ben Gorham', 'Benoist Lapouza', 'Benoît Bergia', 'Bernard Chant', 'Bernard Ellena',
                  'Bertrand Duchaufour', 'Betty Busse', 'Beverley Bayne', 'Bob Aliano', 'Brent Leonesio',
                  'Brook Harvey-Taylor', 'Bruno Fazzolari', 'Bruno Herve', 'Bruno Jovanovic', 'Calice Becker',
                  'Camille Chemardin', 'Camille Goutal', 'Carina Chaz', 'Carlos Benaim', 'Carlos Viñals',
                  'Carmita Magalhães', 'Caroline Dumur', 'Caroline Sabas', 'Catherine Selig', 'Catherine Walsh',
                  'Cecile Hua', 'Cecile Matton', 'Cécile Zarokian', 'Celine Barel', 'Celine Ellena', 'Celine Perdriel',
                  'Celine Ripert', 'Charna Ethier', 'Chris Bartlett', 'Chris Maurice', 'Christelle Laprade',
                  'Christi Meshell', 'Christian Carbonnel', 'Christian Dussoulier', 'Christian Mathieu',
                  'Christian Petrovich', 'Christian Provenzano', 'Christian Vermorel', 'Christiane Plos',
                  'Christine Hassan', 'Christine Nagel', 'Christophe Laudamiel', 'Christophe Raynaud',
                  'Christopher Brosius', 'Christopher Sheldrake', 'Claire Cain', 'Claude Dir', 'Claudette Belnavis',
                  'Clement Gavarry', 'Corinne Cachen', 'Creations Aromatiques', 'Cristian Calabro', 'Cristiano Canali',
                  'Dalia Izem', 'Damien Stammers', 'Daniel Gallagher', 'Daniel Josier', 'Daniel Maurel',
                  'Daniel Moliere', 'Daniel Visentin', 'Daphné Bugey', 'David Apel', 'David Benedek', 'David Maruitte',
                  'David Seth Moltz', 'Delphine Jelk', 'Delphine Lebeau', 'Delphine Thierry', 'Dmitry Bortnikov',
                  'Dominique Moellhausen', 'Dominique Preyssas', 'Dominique Ropion', 'Donna Ramanauskas',
                  'Dora Baghriche', 'Dorothée Piot', 'Douglas Little', 'Edmond Roudnitska', 'Edouard Fléchier',
                  'Ekaterina Siordia', 'Elisabeth Maier', 'Elisabeth Vidal', 'Elise Benat', 'Ellen Covey',
                  'Ellen Molner', 'Emilie Bevierre-Coppermann', 'Emilie Bouge', 'Emilio Valeros', 'Emma Dick',
                  'Enrico Buccella', 'Ernest Beaux', 'Ernest Daltroff', 'Erwin Creed', 'Euan McCall', 'Eugene Au',
                  'Eurico Mazzini', 'Evelyne Boulanger', 'Fabrice Pellegrin', 'Fabrizio Tagliacarne', 'Fanny Bal',
                  'Fanny Grau', 'Fragrance Resources', 'Francesca Bianchi', 'Francis Bocris', 'Francis Camail',
                  'Francis Deleamont', 'Francis Fabron', 'Francis Kurkdjian', 'Francisco Marano', 'Francois Coty',
                  'François Demachy', 'Francois Merle-Baudoin', 'Francois Robert', 'Francoise Caron', 'Frank Voelkl',
                  'Fredrik Dalman', 'Gabriela Chelariu', 'Geoffrey Nejman', 'Gerald Ghislain', 'Gerard Anthony',
                  'Gerard Goupy', 'Gerard Haury', 'Gerard Pelpel', 'Germaine Cellier', 'Geza Schoen',
                  'Gian Luca Perris', 'Gil Clavien', 'Gilles Romey', 'Gino Percontino', 'Giovanni Di Massimo',
                  'Giuseppe Imprezzabile', 'Givaudan', 'Guillaume Flavigny', 'Guy Robert', 'Hamid Merati-Kashani',
                  'Hans Hendley', 'Hany Hafez', 'Harry Cutler', 'Harry Fremont', 'Henri Almeras', 'Henri Bergia',
                  'Henri Robert', 'Henry Creed', 'Hernan Fígoli', 'Hilde Soliani', 'Hiram Green', 'Honorine Blanc',
                  "Hubert d'Ornano", 'Hugo Lambert', 'Ilias Ermenidis', 'Ineke Ruhland', 'Irene Farmachidi',
                  'Isaac Sinclair', "Isabelle d'Ornano", 'Isabelle Doyen', 'Jacqueline Couturier', 'Jacques Cavallier',
                  'Jacques Fleury', 'Jacques Flori', 'Jacques Guerlain', 'Jacques Huclier', 'Jacques Polge',
                  'James Heeley', 'James Krivda', 'Jarekhye Covarrubias', 'Jean Amic', 'Jean Carles',
                  'Jean Claude Delville', 'Jean Desprez', 'Jean Guichard', 'Jean Jacques', 'Jean Kerleo', 'Jean Martel',
                  'Jean-Charles Niel', 'Jean-Christophe Hérault', 'Jean-Claude Astier', 'Jean-Claude Ellena',
                  'Jean-Claude Gigodot', 'Jean-Claude Niel', 'Jean-Francois Laporte', 'Jean-Francois Latty',
                  'Jean-Jacques Diener', 'Jean-Louis Grauby', 'Jean-Louis Sieuzac', 'Jean-Marc Chaillan',
                  'Jean-Michel Duriez', 'Jean-Paul Guerlain', 'Jean-Pierre Bethouart', 'Jean-Pierre Mary',
                  'Jeanne Sandra Rance', 'Jeanne-Marie Faugier', 'Jeannine Mongin', 'Jeffrey Dame', 'Jérôme di Marino',
                  'Jérôme Epinette', 'Jimmy Bodin', 'Jo Malone', 'Joachim Correl', 'JoAnne Bassett', 'Joelle Nealy',
                  'John Biebel', 'John Gamba', 'John Pegg', 'John Stephen', 'John Varvatos', 'Jordi Fernández',
                  'Jorge Lee', 'Josephine Catapano', 'Josh Lobb', 'Josh Meyer', 'Juan Perez', 'Julian Bedel',
                  'Julie Dunkley', 'Julie Masse', 'Julie Pluchet', 'Julien Rasquinet', 'Juliette Karagueuzoglou',
                  'Kamila Lelakova', 'Karine Chevallier', 'Karine Dubreuil-Sereni', 'Kedra Hart', 'Laura Santander',
                  'Laurent Bruyere', 'Laurie Erickson', 'Leandro Petit', 'Leslie Girard', 'Linda Song', 'Liz Moores',
                  'Liz Zorn', 'Loc Dong', 'Lorenzo Pazzaglia', 'Lorenzo Villoresi', 'Louise Turner', 'Luca Gritti',
                  'Luca Maffei', 'Lucas Sieuzac', 'Lucien Ferrero', 'Lucien Piquet', 'Lyn Harris', 'Mackenzie Reilly',
                  'Magali Lara', 'Magali Senequier', 'Mahsam Raza', 'Maïa Lernout', 'Mandy Aftel', 'Manuel Cross',
                  'Marc-Antoine Corticchiato', 'Margot Elena', 'Maria Candida Gentile', 'Marie Duchêne',
                  'Marie Hugentobler', 'Marie Salamagne', 'Marie Schnirer', 'Marie-Aude Couture', 'Marina Stepanova',
                  'Marine Ipert', 'Mário Torri Neto', 'Marion Costero', 'Mark Buxton', 'Mark Constantine',
                  'Mark Knitowski', 'Martin Gras', 'Martine Pallix', 'Marypierre Julien', 'Mathieu Nardin',
                  'Mathilde Bijaoui', 'Mathilde Laurent', 'Maurice Maurin', 'Maurice Roger', 'Maurice Roucel',
                  'Maurizio Cerizza', 'Maurizio Lembo', 'Max Gavarry', 'Mélanie Carestia', 'Melanie Leroux',
                  'Michael Boadi', 'Michael Pickthall', 'Michel Almairac', 'Michel Girard', 'Michel Hy',
                  'Michel Morsetti', 'Michel Roudnitska', 'Michèle Saramito', 'Miguel Matos', 'Miroslav Petkov',
                  'Mylène Alran', 'Napoleão Bastos', 'Natalie Gracia-Cetto', 'Natasha Côté', 'Nathalie Benareau',
                  'Nathalie Feisthauer', 'Nathalie Lorson', 'Nazir Ajmal', 'Neil Morris', 'Nejla Barbir',
                  'Nelly Hachem-Ruiz', 'Nicholas Calderone', 'Nicholas Nilsson', 'Nicolas Beaulieu',
                  'Nicolas Bonneville', 'Nicolas Mamounas', 'Nicole Mancini', 'Nikolay Eremin', 'Norbert Bijaoui',
                  'Olaf Larsen', 'Oliver Valverde', 'Olivia Giacobetti', 'Olivier Creed', 'Olivier Cresp',
                  'Olivier Gillotin', 'Olivier Pescheux', 'Olivier Polge', 'Paolo Cerizza', 'Paolo Terenzi',
                  'Pascal Gaurin', 'Patrice Martin', 'Patrice Revillard', 'Patricia Bilodeau', 'Patricia Choux',
                  'Patricia de Nicolai', 'Paul Emilien', 'Paul Kiler', 'Paul Leger', 'Paul Vacher', 'Pauline Zanoni',
                  'Philippe Bousseton', 'Philippe Paparella-Paris', 'Philippe Romano', 'Philippe Roques',
                  'Philippine Courtière', 'Phillippe Romano', 'Pierre Aulas', 'Pierre Bourdon', 'Pierre Guillaume',
                  'Pierre Montale', 'Pierre Negrin', 'Pierre Wargnye', 'Pierre-Constantin Guéros', 'Pissara Umavijani',
                  'Prin Lomros', 'Quentin Bisch', 'Ralf Schwieger', 'Ramon Monegal', 'Randa Hammami', 'Rania Jouaneh',
                  'Raphael Haury', 'Rasei Fort', 'Raymond Chaillan', 'Raymond Matts', 'René Morgenthaler',
                  'Richard Fraysse', 'Richard Herpin', 'Richard Ibanez', 'Richard Wirtz', 'Robert Bienaimé',
                  'Robert Gonnon', 'Robert Slattery', 'Robertet', 'Rodrigo Flores-Roux', 'Roger Pellegrino',
                  'Roja Dove', 'Romano Ricci', 'Ron Winnegrad', 'Rosa Vaia', 'Rosendo Mateu', 'Russian Adam',
                  'Sabine De Tscharner', 'Sanderson Santana', 'Sarah Horowitz', 'Sarah McCartney', 'Sebastien Cresp',
                  'Serena Ava Franco', 'Serge de Oliveira', 'Serge Kalouguine', 'Serge Lutens', 'Serge Majoullier',
                  'Shadi Samra', 'Sharra Lamoureaux', 'Shelley Waddington', 'Shyamala Maisondieu', 'Sidonie Lancesseur',
                  'Silvana Casoli', 'Silvia Martinelli', 'Simon Constantine', 'Simone Andreoli', 'Sofia Bardelli',
                  'Sonia Constant', 'Sophia Grojsman', 'Sophie Chabaud', 'Sophie Labbé', 'Spyros Drosopoulos',
                  'Stephanie Bakouche', 'Stephen Nilsen', 'Steve DeMercado', 'Sultan Pasha', 'Sven Pritzkoleit',
                  'Sylvain Cara', 'Sylvaine Delacourte', 'Sylvie Fischer', 'Symrise', 'Tamara Soboleva',
                  'Tanja Bochnig', 'Tanya Petrakov', 'Teone Reinthal', 'Terri Bozzo', 'Theodoros Kalotinis',
                  'Thierry Bessard', 'Thierry Wasser', 'Thomas Fontaine', 'Thomas Kosmala', 'Tomoo Inaba',
                  'Trudi Loren', 'Ursula Wandel', 'V Ryzhova', 'Valeria Karmanova', 'Vanina Muracciole', 'Vero Kern',
                  'Verônica Casanova', 'Verônica Kato', 'Véronique Nyberg', 'Viktoria Minya', 'Vincent Kuczinski',
                  'Vincent Marcello', 'Vincent Micotti', 'Vincent Ricord', 'Vincent Roubert', 'Vincent Schaller',
                  'Violaine Collas', 'Violaine David', 'Wilhelm Muelhens', 'Xavier Renard', 'Yann Vasnier',
                  'Yves Cassar', 'Yves de Chirin', 'Yves Tanguy']


def perfumers_convert(array):
    new_list = []
    for i in array:
        j = i.split(" ")
        if len(j) == 3:
            j[1] = " ".join((j[1], j[2]))
            del j[2]
        new_list.append(j)
    return new_list


def delete_perfumers():
    Perfumer.objects.all().delete()


def create_perfumers():
    perfumers_list = perfumers_convert(PERFUMERS_LIST)
    for name in perfumers_list:
        if len(name) == 2:
            if not Perfumer.objects.filter(first_name=name[0], last_name=name[-1]).exists():
                Perfumer.objects.create(first_name=name[0], last_name=name[-1])
