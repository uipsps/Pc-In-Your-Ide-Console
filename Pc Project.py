import wikipedia
import time
import random
Songs = ['Money In The Grave','Drip To Hard','Lets Go']
Note = ''


def home():
   global Note
   while True:
    Program = input('what program do you want to use ')
    if Program == 'notepad':
     Pro = input('Do You Want To Make A New Note Or View Your Saved Note ')
     if Pro == 'saved note':
            print('Loading Saved Note')
            print('Done')
            print (Note)
            time.sleep(0.2)
     elif Pro == 'new':
         Note = input('##################################### \n')
         print('Note Saved')
    
    if Program == 'browser':
       search = input('What Do You Want To Search ')
       if search == 'am i adopted':
         print('Yes')
       else:
        result = wikipedia.page(search)
        print(result.summary, '\n')
         
    if Program == 'discord':
        StorSize = random.randint(0,130)
        print('you have',StorSize,'messages' )
        Mesager = input('who do you want to text ')
        if Mesager == 'uips':
            print('E')
            
    if Program == 'storage':
      c = random.randint(20,700)
      print('Drive:C',c,'GB')
      Format = input('Do You Want To Format Your Drive!')
      if Format == 'yes':
        print('Formating....')
        time.sleep(30)
        print('Done Formating')
        print('Drive:C 0 GB')
        
    if Program == 'spotfiy':
       print('Playist:cheese')
       print(Songs)
       WhatSTP = input('')
       if WhatSTP == Songs[0] or WhatSTP == Songs[1] or WhatSTP == Songs[2]:
         print("Playing:",WhatSTP)
       
      
          
        
    
   
#boot
def boot():
  print("Loading Gpu....")  
  time.sleep(3)
  print('Done Loading Gpu')
  print('Loading Cpu....')
  time.sleep(4)
  print('Done Loading Cpu')
  print("Booting....")
  time.sleep(2)
  print ('Booted')
  home()
  
boot()