#ramail.py

Send the contents of an html file as a request to the Mailgun API. 
A recipient email address using the -a flag and a subject using the
-s flag must be set. 

'''bash
python ramail.py -a "example@email.com" -s "Subject"
'''

I need a way to create an html/txt file for each email I want to send and I want to store it in a folder locally. The kind of thing I want to have is similar the following structure: 

_dir: 

	_drafts:
		draft-someone@-site-com.html

	_ready:
		2015-04-26-someone@-site-com.txt

	_sent:
		2015-04-26-someone@-site-com.html
	
	_received:
		2015-04-26-someone@-site-com.html

Basically what would happen above is markdown would be converted into a string and stored in a single line text file. That file would then used to send the actual message. Once the file is sent it would be converted back into either markdown or an html file. Incoming message are in the form of text and would need to be converted into either markdown or html as well. This would also make it so that the html files can be used to interfact with this graphically, but I wouldn't want that personally. Finally there would need to be a way to check for new messages and I would love to have something in the terminal that alerts me when new messages arrive and even let me view them, reply to them, delete them or just save them for later; all from the command line. 