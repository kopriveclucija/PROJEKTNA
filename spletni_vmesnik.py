import bottle
import os
from osnovno import Model, Naloga

@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.html')

bottle.run(reloader=True)


