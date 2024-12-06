from rest_framework import status
from rest_framework.response import Response


def forbidden_response():
    message = "You do not have permission to perform this action."
    return Response({"error": message}, status=status.HTTP_403_FORBIDDEN)