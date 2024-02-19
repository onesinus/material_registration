# auth_utils.py

from odoo.http import request, Response
from odoo.exceptions import AccessError

def authenticate(func):
    def wrapper(*args, **kwargs):
        try:
            # Check if the request includes a valid authentication token
            token = request.httprequest.headers.get('Authorization')
            user = authenticate_user(token)

            # Add the authenticated user to the kwargs
            kwargs['user'] = user

            # Call the original function with the authenticated user
            return func(*args, **kwargs)

        except AccessError:
            return Response("Unauthorized: Invalid or missing authentication token", status=401)
        except Exception as e:
            # Handle other exceptions and return a bad request response
            return Response(f"Bad Request: {str(e)}", status=400)

    return wrapper

def authenticate_user(token):
    # Your logic to authenticate the user based on the token
    # Example: Find the user with the provided token
    user = request.env['res.users'].sudo().search([('auth_token', '=', token)])

    if not user:
        raise AccessError("Invalid authentication token")

    return user
