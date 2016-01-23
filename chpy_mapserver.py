import cherrypy
import time
import os, os.path
from jinja2 import Environment, FileSystemLoader

host_ip = '0.0.0.0'
host_port = 8081

local_path = os.path.dirname(os.path.abspath(__file__))

cherrypy_conf = {
	'/': {
		'tools.sessions.on': False,
		'tools.staticdir.root': local_path
		}
	}

class MapServer(object):
    def __init__(self):
        self.maptiles = Map()

    @cherrypy.expose
    def index(self):
        return 'Running tout court'

@cherrypy.popargs('fz','z','x','y')
class Map(object):
    @cherrypy.expose
    def index(self, fz, z,x,y):
        return '%s/%s/%s/%s' % (fz,z,x,y)


mapserver = MapServer();

cherrypy.tree.mount(mapserver, '/', config = cherrypy_conf)

cherrypy.config.update({
	'server.socket_port': host_port,
	'server.socket_host': host_ip
	})

cherrypy.engine.start()
cherrypy.engine.block()
