from django.http import HttpResponseForbidden

class WhiteLists:

    REST_SAFE_LIST_IPS= [
        '127.0.0.1',
        '123.45.67.89',   # example IP
        '192.168.0.',     # the local subnet, stop typing when subnet is filled out
        '175.181.211.',
    ] 
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        remote_addr = request.META['REMOTE_ADDR']

        hasPermission = False
        for valid_ip in self.REST_SAFE_LIST_IPS:
            # if remote_addr == valid_ip or remote_addr.startswith(valid_ip):
            if remote_addr.startswith(valid_ip):
                hasPermission = True 

        if not hasPermission:
            return HttpResponseForbidden() 


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
