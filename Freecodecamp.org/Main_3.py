#Build an RPG Character
#https://www.freecodecamp.org/learn/python-v9/lab-rpg-character/build-an-rpg-character

full_dot = '●'
empty_dot = '○'

#cara panjang
def cara_panjang():
    print ('--- Hasil Cara Panjang ---')

    def create_character (name,strength,intelligence,charisma):
        # Validasi nama
        if not isinstance (name,str):
            return 'The character name should be a string'
            
        if name == '':
            return 'The character should have a name'
            
        if len(name) > 10:
            return 'The character name is too long'
            
        if ' ' in name:
            return 'The character name should not contain spaces'
            
        # Validasi stats
        if not (isinstance(strength,int) and isinstance(intelligence,int) and isinstance(charisma,int)):
            return 'All stats should be integers'
            
        if strength < 1 or intelligence < 1 or charisma < 1:
            return 'All stats should be no less than 1'
            
        if strength > 4 or intelligence > 4 or charisma > 4:
            return 'All stats should be no more than 4'
            
        if (strength + intelligence + charisma) != 7:
            return 'The character should start with 7 points'
        
        #generate bar stats
        str_bar = (strength*full_dot) + ((10 - strength)*empty_dot)
        int_bar = (intelligence*full_dot) + ((10 - intelligence)*empty_dot)
        cha_bar = (charisma*full_dot) + ((10 - charisma)*empty_dot)
        
        return f'{name}\n STR {str_bar}\n INT {int_bar}\n CHA {cha_bar}'
    
    #Test    
    print(create_character('ren',4,2,1))


#cara Pendek
def cara_pendek():
    print('--- Hasil Cara Pendek ---')

    # Buat fungsi untuk bar stats terlebih dahulu
    def make_bar(val):
        return (val * full_dot) + ((10 - val) * empty_dot)

    def create_character(name, strength, intelligence, charisma):
        # Validasi Nama
        if type(name) is not str: return 'The character name should be a string'
        if not name: return 'The character should have a name'
        if len(name) > 10: return 'The character name is too long'
        if ' ' in name: return 'The character name should not contain spaces'
        
        # Validasi Stats
        stats = (strength, intelligence, charisma)
        if any(type(s) is not int for s in stats): return 'All stats should be integers'
        if min(stats) < 1: return 'All stats should be no less than 1'
        if max(stats) > 4: return 'All stats should be no more than 4'
        if sum(stats) != 7: return 'The character should start with 7 points'
        
        # Cetak langsung panggil make_bar()
        return f"{name}\nSTR {make_bar(strength)}\nINT {make_bar(intelligence)}\nCHA {make_bar(charisma)}"

    # Test Run
    print(create_character('ren', 4, 2, 1))


cara_panjang()
cara_pendek()


'''Di Python, kamu bisa nulis 
pernyataan if dan return dalam 1 baris 
kalau instruksinya cuma satu (single statement).
cocok untuk code yg singkat dan tidak disarankan untuk
code yg panjang karena akan susah dibaca'''