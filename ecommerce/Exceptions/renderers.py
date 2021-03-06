import json


from rest_framework.renderers import JSONRenderer

from shopstar import settings



class EcommerceJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (such as the user can't be authenticated)
        # `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        errors = data.get('errors', None)

        if errors is not None:
            # As mentioned above, we will let the default JSONRenderer handle
            # rendering errors.
            return super(EcommerceJSONRenderer, self).render(data)

        return json.dumps({
            self.object_label: data
        })

class UserJSONRenderer(EcommerceJSONRenderer):
    charset = 'utf-8'
    object_label = 'user'
    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.

        # If we receive a `token` key in the response, it will be a
        # byte object. Byte objects don't serializer well, so we need to
        # decode it before rendering the User object.
        token = data.get('token', None)
        print ("tokrn = ")
        print (token)
        print (data)


        if token is not None and isinstance(token, bytes):
            # We will decode `token` if it is of type
            # bytes.
            data['token'] = token.decode('utf-8')

        # Finally, we can render our data under the "user" namespace.
        return super (UserJSONRenderer, self).render (data)

class CategoryJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        #errors = data.get ('errors', None)
        print (data)
        # If we receive a `token` key in the response, it will be a
        # byte object. Byte objects don't serializer well, so we need to
        # decode it before rendering the User object.
        #token = data.get ('token', None)
        print("tokrn = ")
        #print(token)
        print(data)

        #if errors is not None:
            # As mentioned about, we will let the default JSONRenderer handle
            # rendering errors.
            #return super (CategoryJSONRenderer, self).render (data)

       # if token is not None and isinstance (token, bytes):
            # We will decode `token` if it is of type
            # bytes.
           # data['token'] = token.decode ('utf-8')

        # Finally, we can render our data under the "user" namespace.
        return json.dumps ({
            'category': data
        })



class ProfileJSONRenderer (EcommerceJSONRenderer):
        object_label = 'profile'