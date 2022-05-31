from django.http import JsonResponse
def get_response(message="", data={}, error=[], success=False):
   return {

      "success" : success,
      "error": error,
      "data": data,
      "message" : message,
   }

class ExceptionMiddleware(object):
   def __init__(self, get_response):
       self.get_response = get_response
 
   def __call__(self, request):
 
       response = self.get_response(request)
 
       if response.status_code == 500:
           response = get_response(
               message="Internal server error, please try again later",
               error= response.status_code
           )
           return JsonResponse(response)
 
       if response.status_code == 404 and "Page not found" in str(response.content):
           response = get_response(
               message="Page not found, invalid url",
               error= response.status_code
           )
           return JsonResponse(response)
 
       return response