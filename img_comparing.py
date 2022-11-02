from cv2 import ORB_create, BFMatcher, NORM_HAMMING
from config import SIMILARITY_VAL

"""
Se comparan las dos imagenes y devuelde si las imagenes son similares,
usando el un detector ORB
"""
def comparing_image(img1:str, img2:str) -> bool:
    """En la funcion se reciben dos imagenes que se desea comparar y esta devolvera un resultado
    True si estas imagenes resultan ser similares, el valor a tomar en cuenta de la comparacion esta
    en el archivo config.py en la constante SIMILARITY_VAL

    Args:
        img1 (str): _description_
        img2 (str): _description_

    Returns:
        bool: _description_
    """    
    # Cosntructor de objeto ORB
    orb_class = ORB_create()

    # Detectar puntos claves y descriptores
    kp1, desc1 = orb_class.detectAndCompute(img1, None)
    kp2, desc2 = orb_class.detectAndCompute(img2, None)

    # Definir el bruteforce matcher object
    bruteforce = BFMatcher(NORM_HAMMING, crossCheck=True)

    #Comprobar similitud 
    matches = bruteforce.match(desc1, desc2)
    #Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
    similar_regions = [i for i in matches if i.distance < 50]
    sim = len(similar_regions) / len(matches)

    if len(matches) == 0 or sim < SIMILARITY_VAL:
        return False
    return True