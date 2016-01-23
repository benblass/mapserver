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

class mapServer(object):
	def __init__(self):
		pass

	@cherrypy.expose
	def index(self):
		return "<html>Running</html>"

cherrypy.tree.mount(mapServer(), '/', config = cherrypy_conf)

cherrypy.config.update({
	'server.socket_port': host_port,
	'server.socket_host': host_ip
	})

cherrypy.engine.start()
cherrypy.engine.block()