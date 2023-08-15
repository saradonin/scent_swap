from scent_app.models import Note

NOTES_LIST = ['Absinth', 'African amber', 'African violet', 'Agarwood', 'Agave', 'Aglaia', 'Aldambre™', 'Aldehydes',
              'Alder', 'Algae', 'Algae', 'Allspice', 'Aloe', 'Amaryllis', 'Amber', 'Amber', 'Amber Core',
              'Amber Xtreme™', 'Amber absolute', 'Amber notes', 'Ambergris', 'Amberketal', 'Amberlyn®', 'Ambermax®',
              'Ambertonic®', 'Amberwood', 'Ambramone™', 'Ambranum', 'Ambre 83 accord', 'Ambre 84 accord', 'Ambrette',
              'Ambrocenide®', 'Ambroxan', 'Amyris', 'Angelica', 'Animalic notes', 'Aniseed', 'Aniseed', 'Aquatic notes',
              'Arabian amber', 'Arnica', 'Artemisia', 'Ashoka', 'Aspen', 'Aster', 'Atlas cedar', 'Australian amber',
              'Azalea', 'Balsam fir', 'Balsam poplar', 'Balsam poplar', 'Balsamic notes', 'Balsams', 'Balsams',
              'Baltic amber', 'Bamboo', 'Bark', 'Bark', 'Barley', 'Basil', 'Bay rum', 'Bean', 'Beech', 'Beeswax',
              'Begonia', 'Bellflower', 'Benzoin', 'Benzoin', 'Bergamot', 'Berries', 'Beverages', 'Birch',
              'Bitter orange', 'Bitter orange blossom', 'Bitter orange blossom', 'Black amber', 'Black caraway',
              'Blood orange', 'Blue amber', 'Boronia', 'Brazilian amber', 'Broom', 'Buchu', 'Buckwheet', 'Butter',
              'Cabrueva', 'Cactus', 'Calamus', 'Calla', 'Calycanthus', 'Camellia', 'Camomile', 'Camomile',
              'Camphor tree', 'Cannabis', 'Caramel', 'Caraway', 'Cardamom', 'Carnation', 'Cashmere wood',
              'Cashmere wood', 'Cassia', 'Castoreum', 'Cedar', 'Cedramber', 'Celery', 'Celery', 'Cetalox®', 'Chestnut',
              'Chili', 'Chocolate', 'Chrysanthemum', 'Cigar', 'Cinnamon', 'Cistus', 'Citric notes', 'Citron',
              'Citrus fruits', 'Civet', 'Clary sage', 'Clay', 'Clementine', 'Clove', 'Clover', 'Coal', 'Coca', 'Cocoa',
              'Coniferous trees', 'Coniferous trees', 'Copaiva balsam', 'Coriander', 'Cornflower', 'Costus', 'Cotton',
              'Cream', 'Cress', 'Crocus', 'Crystal amber', 'Cuban amber', 'Cucumber', 'Cumarin', 'Cumin', 'Curry',
              'Cyclamen', 'Cypress', 'Dahlia', 'Daisy', 'Dandelion', 'Daphne', 'Datura', 'Davana', 'Deer musk',
              'Dianthus', 'Dill', 'Dish', 'Dogwood', "Dragon's blood", 'Driftwood', 'Dynamone', 'Earthy notes', 'Ebony',
              'Egyptian amber', 'Elder', 'Elder', 'Elemi', 'Elm tree', 'Eucalyptus', 'Fennel', 'Fennel', 'Fenugreek',
              'Fern', 'Fig', 'Fir balsam', 'Firmenich', 'Floral notes', 'Floralozone', 'Floralozone', 'Flowers',
              'Fragrance ingredients', 'Frangipani', 'Freesia', 'Fruits', 'Fruity notes', 'Gaiac wood', 'Galbanum',
              'Gardenia', 'Gentian', 'Geranium', 'Ginger', 'Ginseng', 'Givaudan', 'Gladiolus', 'Glycyrrhiza',
              'Gourmandy notes', 'Grain', 'Grapefruit', 'Grasses', 'Green notes', 'Gunpowder', 'Gurjum', 'Hamamelis',
              'Hawthorn', 'Hedychium', 'Heliotrope', 'Hellebore', 'Hemp', 'Henna', 'Herbaceous notes', 'Herbs', 'Herbs',
              'Hibiscus', 'Hibiscus', 'Hinoki', 'Holly', 'Honey', 'Honeysuckle', 'Hyacinth', 'Hydrangea', 'Hyraceum',
              'IFF', 'Ice cream', 'Immortelle', 'Incense', 'Incense', 'Incense', 'Incense', 'Ink', 'Ink', 'Ipomoea',
              'Iris', 'Iris', 'Ivy', 'Jacaranda', 'Jasmine', 'Jojoba', 'Juices', 'Juices', 'Juices', 'Juniper',
              'Kaffir lime', 'Katsura tree', 'Kaō', 'Kelp', 'Kelp', 'Khyphi', 'Kumquat', 'Labdanum',
              'Lapsang souchong tea', 'Laurel', 'Laurel', 'Lavender', 'Lavender', 'Leather', 'Leaves', 'Leaves',
              'Lemon', 'Lemon grass', 'Lemon grass', 'Lemon vervain', 'Liatrix', 'Lichen', 'Lilac', 'Lily',
              'Lily-of-the-valley', 'Lime', 'Linden blossom', 'Linden tree', 'Linen', 'Liquorice', 'Litsea cubeba',
              'Lotus', 'Lovage', 'Lovage', 'Magnolia', 'Mahagony', 'Mallow', 'Malt', 'Mandarin', 'Mandevilla', 'Mane',
              'Manuka', 'Maple', 'Marigold', 'Marine notes', 'Marjoram', 'Marshmallow', 'Massoia', 'Mastic', 'Matcha',
              'Maté tea', 'Meat', 'Melissa', 'Metallic notes', 'Milk', 'Mimosa', 'Mineral notes', 'Minneola', 'Mint',
              'Mistletoe', 'Mock-orange', 'Monarda', 'Moss', 'Mossy notes', 'Mountain ash', 'Mugwort', 'Muhuhu',
              'Mushrooms', 'Musk', 'Musk rose', 'Mustard', 'Myrrh', 'Myrrh', 'Myrtle', 'Narcissus', 'Nectar', 'Nectar',
              'Neroli', 'Neroli', 'Nettle', 'Not classified', 'Nutmeg', 'Nuts', 'Oak', 'Oakmoss', 'Oat', 'Okoumé',
              'Oleander', 'Olive', 'Opoponax', 'Orange', 'Orange blossom', 'Orchid', 'Oregano', 'Oriental notes',
              'Osmanthus', 'Osmanthus', 'Ozone', 'Pagoda tree', 'Palisander', 'Palm tree', 'Palmarosa', 'Pandanus',
              'Pansy', 'Paper', 'Paprika', 'Papyrus', 'Papyrus', 'Parsley', 'Passion flower', 'Pastry', 'Patchouli',
              'Patchouli', 'Pea', 'Peat', 'Pelargonium', 'Peony', 'Pepper', 'Peppermint', 'Peru balm', 'Petitgrain',
              'Pfizer', 'Phlox', 'Pine balsam', 'Pittosporum', 'Plants', 'Plants', 'Plants', 'Plants', 'Pomelo',
              'Popcorn', 'Poplar', 'Poppy', 'Powdery notes', 'Praliné', 'Preserves', 'Primrose', 'Pumpkin', 'Reseda',
              'Resinous notes', 'Resins', 'Resins', 'Rhododendron', 'Rhubarb', 'Rhubarb', 'Rice', 'Robertet', 'Robinia',
              'Rose', 'Rose hip', 'Rosemary', 'Rosewood', 'Saffron', 'Sage', 'Salt', 'Salty notes', 'Sandalwood',
              'Satsuma', 'Seed', 'Seed', 'Sesame', 'Sherbet', 'Shiso', 'Shiso', 'Show more', 'Silk', 'Skin', 'Skin',
              'Smilax', 'Smoky notes', 'Soapy notes', 'Soapy notes', 'Spearmint', 'Spices', 'Spicy notes', 'Spikenard',
              'Spread', 'Star anise', 'Stephanotis', 'Storax', 'Sugar', 'Sunflower', 'Surinam cherry', 'Sweet corn',
              'Sweet dishes', 'Sweet pea', 'Sweet potato', 'Sweets', 'Symrise', 'Synarome', 'Syrup', 'Tagetes',
              'Tamarind', 'Tansy', 'Tansy', 'Tar', 'Tar', 'Tarragon', 'Tea', 'Tea tree', 'Teak', 'Textile notes',
              'Thujopsis (Hiba)', 'Thyme', 'Tiaré', 'Tobacco', 'Tobacco flower', 'Tolu balm', 'Tomato', 'Tonka bean',
              'Tree moss', 'Truffle', 'Tuberose', 'Tulip', 'Tulip tree', 'Turmeric', 'Valerian', 'Vanilla', 'Varnish',
              'Vegetables', 'Velvet', 'Vervain', 'Vetiver', 'Vetiver', 'Vigon', 'Violet', 'Violet leaf',
              'Virginia cedar', 'Water lily', 'Wax', 'Wenge', 'West Indian lantana', 'Wheet', 'White flowers', 'Willow',
              'Wisteria', 'Woods', 'Woody notes', 'Wool', 'Yams', 'Yarrow', 'Ylang-ylang', 'Yuzu']


def delete_notes():
    Note.objects.all().delete()


def create_notes():
    for note in NOTES_LIST:
        if not Note.objects.filter(name=note).exists():
            Note.objects.create(name=note)
