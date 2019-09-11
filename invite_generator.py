import requests
import base64
import json

RED = '\033[31m'
END = '\033[0m'
art = RED \
    + """

    )                                                        (
 ( /(                )   *   )    )          (               )\ )                                 )
 )\())    )       ( /( ` )  /( ( /(    (   ( )\          )  (()/(     (      (    (            ( /(      (
((_)\  ( /(   (   )\()) ( )(_)))\())  ))\  )((_)  (   ( /(   /(_))   ))\  (  )(   )\ )  `  )   )\()) (   )(
 _((_) )(_))  )\ ((_)\ (_(_())((_)\  /((_)((_)_   )\  )\()) (_))_   /((_) )\(()\ (()/(  /(/(  (_))/  )\ (()\
| || |((_)_  ((_)| |(_)|_   _|| |(_)(_))   | _ ) ((_)((_)\   |   \ (_))  ((_)((_) )(_))((_)_\ | |_  ((_) ((_)
| __ |/ _` |/ _| | / /   | |  | ' \ / -_)  | _ \/ _ \\ \ /   | |) |/ -_)/ _|| '_|| || || '_ \)|  _|/ _ \| '_|
|_||_|\__,_|\__| |_\_\   |_|  |_||_|\___|  |___/\___//_\_\   |___/ \___|\__||_|   \_, || .__/  \__|\___/|_|
                                                                                  |__/ |_|
""" \
    + END
print(art)

url = "https://www.hackthebox.eu/api/invite/generate"

headers = {'User-Agent': 'My User Agent 1.0'}

r = requests.post(url,headers=headers)
data = json.loads(r.text)
encoded_data = data['data']['code'].encode("utf-8")
print "Encoded Code is : " + encoded_data
invite_code = base64.b64decode(encoded_data)
print "Your invite code is : " + invite_code
print "\nHappy Hacking"
