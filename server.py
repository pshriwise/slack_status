
import SimpleHTTPServer
import SocketServer
import urllib2
import requests
from threading import Thread
import argparse

from status import aliases, locations
from tokens import tokens

status_str = '{"status_text":{text},"status_emoji":{token}}'

base_url = 'https://slack.com/api/users.profile.set?token={token}'

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()
        self.set_status()

    def set_status(self):
        """ Expects format /location """
        location = self.path.split("/")[-1]

        # ignore if asking for icon
        if location == "favicon.ico":
            return

        try:
            status_dict = locations[location]
        except:
            print("Failed to find {} in location dicionary.".format(location))

        # check aliases and insert new entry as needed
        for k,v in aliases.items():
            # if that alias is in our status dict
            if v in status_dict.keys():
                # add a new entry identical to it's alias entry
                status_dict[k] = status_dict[v]

        self.wfile.write(status_dict)

        for k,v in status_dict.items():
            token = tokens[k]
            emoji = v[0]
            status = v[1]

            url_str = base_url.format(token=token)
            url_str += '&profile={"status_text":"' + status + '",'
            url_str += '"status_emoji":":' + emoji + ':"}'
            requests.get(url_str, verify=False)

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--IP', dest = 'IP', required=False, type=str, default="")
    parser.add_argument('--PORT', dest = 'PORT',
                        help="List of ports on which the server will be generated.",
                        required=False, type=int, default="8000")
 
    args = parser.parse_args()

    try:
        server = SocketServer.ThreadingTCPServer((args.IP, args.PORT), Handler)
        server.request_queue_size = 100
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == "__main__":
    main()
