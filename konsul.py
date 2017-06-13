import time
from http.server import HTTPServer, BaseHTTPRequestHandler

class ConsulOfTheDay():
  def __init__(self):
    self.konsuln = self.get_all_consuls()

  def get_all_consuls(self):
    with open("konsuln.txt", "r") as datei:
      return datei.readlines()

  def get_consul_of_the_day(self):
    unix_tage = int( time.time() / (60*60*24) )
    return self.konsuln[ unix_tage % len(self.konsuln)]

class KonsulHandler(BaseHTTPRequestHandler):
  c = ConsulOfTheDay()

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/plain')
    self.end_headers()
    self.wfile.write(self.c.get_consul_of_the_day().encode("utf-8"))
    return
  
def main():
  print(KonsulHandler.c.get_consul_of_the_day())
  server_address = ('', 15344)
  httpd = HTTPServer(server_address, KonsulHandler)
  httpd.serve_forever()
  
main()