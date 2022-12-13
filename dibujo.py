#Función que recibe el número de errores cometidos hasta el momento e imprime un dibujo de acuerdo a la cantidad de errores
def dibujo(errores):
    if(errores==0):                                         #En caso de no haber cometido errores
        print("""

            JUEGO DEL AHORCADO
                   ________________          
                  | ___________    |         
                  |            |   |         
                  |            |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
        _______________________|___|_________
        /////////////////////////////////////

        """)
    if(errores==1):                                         #En caso de haber cometido 1 error
        print("""

            JUEGO DEL AHORCADO
                   ________________          
                  | ___________    |         
                  |            |   |         
                  |            |   |         
                 ()            |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
        _______________________|___|_________
        /////////////////////////////////////

        """)
    if(errores==2):                                         #En caso de haber cometido 2 errores
        print("""

            JUEGO DEL AHORCADO
                   ________________          
                  | ___________    |         
                  |            |   |         
                  |            |   |         
                 ()            |   |         
                 ||            |   |         
                 ||            |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
        _______________________|___|_________
        /////////////////////////////////////

        """)
    if(errores==3):                                         #En caso de haber cometido 3 errores
        print("""

            JUEGO DEL AHORCADO
                   ________________          
                  | ___________    |         
                  |            |   |         
                  |            |   |         
                 ()            |   |         
                /||            |   |         
               / ||            |   |         
              ^                |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
        _______________________|___|_________
        /////////////////////////////////////

        """)
    if(errores==4):                                         #En caso de haber cometido 4 errores
        print("""

            JUEGO DEL AHORCADO
                   ________________          
                  | ___________    |         
                  |            |   |         
                  |            |   |         
                 ()            |   |         
                /||\           |   |         
               / || \          |   |         
              ^      ^         |   |         
                               |   |         
                               |   |         
                               |   |         
                               |   |         
        _______________________|___|_________
        /////////////////////////////////////

        """)
    if(errores==5):                                         #En caso de haber cometido 5 errores
        print("""

            JUEGO DEL AHORCADO
                   ________________          
                  | ___________    |         
                  |            |   |         
                  |            |   |         
                 ()            |   |         
                /||\           |   |         
               / || \          |   |         
              ^  /   ^         |   |         
                /              |   |         
              _/               |   |         
                               |   |         
                               |   |         
        _______________________|___|_________
        /////////////////////////////////////

        """)
    if(errores==6):                                         #En caso de haber cometido 6 errores
        print("""

            JUEGO DEL AHORCADO
                   ________________          
                  | ___________    |         
                  |            |   |         
                  |            |   |         
                 ()            |   |         
                /||\           |   |         
               / || \          |   |         
              ^  /\  ^         |   |         
                /  \           |   |         
              _/    \_         |   |         
                               |   |         
                               |   |         
        _______________________|___|_________
        /////////////////////////////////////

        """)