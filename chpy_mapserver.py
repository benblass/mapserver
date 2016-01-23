import cherrypy
import time
import os, os.path
import simplejson

host_ip = '0.0.0.0'
host_port = 8081

local_path = os.path.dirname(os.path.abspath(__file__))

configFile = "map.config"

cherrypy_conf = {
	'/': {
		'tools.sessions.on': False,
		'tools.staticdir.root': local_path
	},
	'/static': {
		'tools.staticdir.on': True,
		'tools.staticdir.dir': './static'
	}
}

class MapServer(object):
    def __init__(self, mapconfig={}):
     self.displayoptions = mapconfig['displayoptions']
     self.area = mapconfig['name']
     self.areapath = mapconfig['path']
     pass

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_map_params(self):
        return dict(area=self.area, areapath=self.areapath, displayoptions = self.displayoptions)

def loadMapConfig(filename=''):
	json_data = open(filename).read()
	return simplejson.loads(json_data)

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

mapserver = MapServer(loadMapConfig(configFile));

cherrypy.tree.mount(mapserver, '/', config = cherrypy_conf)

cherrypy.config.update({
	'server.socket_port': host_port,
	'server.socket_host': host_ip,
	'tools.CORS.on': True
	})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.engine.start()
cherrypy.engine.block()
