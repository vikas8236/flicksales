
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Organization, User
from .serializers import OrganizationSerializer, UserSerializer

class RegisterOrganization(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        org_data = request.data.get("organization")
        admin_data = request.data.get("admin_user")

        # Create the organization
        org_serializer = OrganizationSerializer(data=org_data)
        if org_serializer.is_valid():
            organization = org_serializer.save()
        else:
            return Response(org_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create the admin user
        admin_data["organization"] = organization.id
        admin_data["is_org_admin"] = True
        user_serializer = UserSerializer(data=admin_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"organization": org_serializer.data, "admin_user": user_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
