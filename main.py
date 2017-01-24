#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
def fortuneTell():
	fortune = [
		'All you need is happiness in life and it is not tied to anything else',
		'Sweet times may sound lasting but they might turn sour',
		'You ate a good lunch buddy',
		'You are headed for a break up so toughen up your feelings'
	]

	index = random.randint(0, len(fortune)-1)
	return fortune[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	luck = fortuneTell()
    	lucky_number = random.randint(1,999)
    	header = '<h1>Fortune Cookies</h1>'
    	final_luck = '<p>Your fortune: '+str(luck)+'</p>'
    	your_number = '<p>Your lucky number: '+str(lucky_number)+'</p>'
    	checkagain = "<a href='.'><button>Check Again</button></a>"
    	
    	content = header+final_luck+your_number+checkagain

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
