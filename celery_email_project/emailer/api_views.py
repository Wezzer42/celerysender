from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer
from .tasks import send_email_task

class SendEmailAPIView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            send_email_task.delay(email, subject, message)
            return Response({"message": "Email queued successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
