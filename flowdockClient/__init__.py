import pycurl, json, thread
from StringIO import StringIO
from time import gmtime, strftime

class flowdock_py:
    
    #default params
    API_TOKEN = ""
    CALL_BACK = ""
    DEBUG = None
    URL_PUSH = "https://api.flowdock.com/v1/messages/chat"
    URL_STREAM = "https://stream.flowdock.com/flows/?filter=web-eire/main"
    URL_USERS = "https://api.flowdock.com/flows/web-eire/main/users"
    USER = "webeire@gmail.com"
    USERS = {}
    USER_NAME = "Daithi"
    PASS = "chanman77"
    
    def __init__(self):
        if(self.DEBUG):
            print "flowdockClient: class constructed"
    
    def get_users(self):
        """
        Get list of users for flow
        """
        import pycurl
        url = self.URL_USERS
        conn = pycurl.Curl()
        
        #debug?
        if(self.DEBUG):
            print "flowdockClient: list of users..."
            print url
        
        #make request
        conn.setopt(pycurl.USERPWD, "%s:%s" % (self.USER, self.PASS))
        conn.setopt(pycurl.URL, url)
        #conn.setopt(pycurl.VERBOSE,  1)
        #conn.setopt(pycurl.DEBUGFUNCTION,  self.test)
        conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)  #send stream to self.on_receive
        conn.perform()
        pass
    
    def stream(self,  stream_callback):
        """
        @param method stream_callback A method to pass the stream stdOut to
        """
        if(self.DEBUG):
            print "flowdockClient: stream() method called"
        self.CALL_BACK = stream_callback
        self.stream_pycurl()

    def stream_pycurl(self):
        """
        method needs to be threaded
        """
        import pycurl
        if(self.DEBUG):
            print "flowdockClient: stream starting..."
        conn = pycurl.Curl()
        conn.setopt(pycurl.USERPWD, "%s:%s" % (self.USER, self.PASS))
        conn.setopt(pycurl.URL, self.URL_STREAM)
        conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)  #send stream to self.on_receive
        conn.perform()
        
    def test(debug_type, debug_code,  debug_msg):
        """@deprecated Debug function"""
        print "debug(%d): %s" % (debug_code, debug_msg)

    def stream_requests(self,  data):
        """
        Initiates the pycurl stream
        params = [{'content':'this is the content', 'external_user_name':self.USER}]
        """
        data = str(data)
        self.conn1 = pycurl.Curl()
        url = self.URL_PUSH + "/" + self.API_TOKEN
        
        #debug
        if(self.DEBUG):
            print "flowdockClient: request to "+  url +" ..."
            print data
            
        #format data, send request
        data = json.dumps({"content": data, "external_user_name": "Daithi"})
        self.conn1.setopt(pycurl.POST,  1)
        self.conn1.setopt(pycurl.VERBOSE,  1)
        self.conn1.setopt(pycurl.DEBUGFUNCTION,  self.test)
        self.conn1.setopt(pycurl.HTTPHEADER,  ['Content-Type: application/json'])
        self.conn1.setopt(pycurl.USERPWD, "%s:%s" % (self.USER, self.PASS))
        self.conn1.setopt(pycurl.POSTFIELDS,  data)
        self.conn1.setopt(pycurl.URL, url)
        self.conn1.setopt(pycurl.WRITEFUNCTION, self.on_receive)
        self.conn1.perform()
        
        #debug?
        if(self.DEBUG):
            print "request sent"
        
    def on_receive(self,  data):
        """
        Handles the stdout for the stream

        Processes and routes the stream responses
        """
        js = json.loads('[' + data + ']')
        if(self.DEBUG):
            print "received..."
            print data
        
        #users
        try:
            avatar = js[0][0]['avatar']
            if isinstance(avatar, basestring):
                for user in js[0]:
                    self.USERS[user['id']] = user['nick']
                print self.USERS
        except Exception, e:
            print e
            pass

        #chat message
        try:
            data = js[0]['content']
            user_id = int(js[0]['user'])
            user = self.USERS.get( user_id )
            time = strftime("%H:%M:%S", gmtime())
            message = "%s %s: %s" % (time,user,data)
            print "message:"
            print message
            if isinstance(data,  basestring):
                self.CALL_BACK( message )
        except Exception, e:
            print e
            pass
        
        #error messages
        try:
            data = js[0]['message']
            self.CALL_BACK( "<p style=\"color:red\">error: " + data  + "</p>")
        except:
            pass
    
