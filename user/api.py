
# Create your views here.
from urllib import response
from django.contrib.auth.models import User
from rest_framework import exceptions

from django.conf import settings
from django.core.mail  import send_mail
import random

from requests import request



from .serializer import UserRegistrationSerializer,VerifyUserOtpSerializer,ResendOtpSerializer,UserLoginSerializer,resetpasswordSerializer,ResetPasswordSer,UserListSerializer
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework import viewsets
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User



# funtion to send otp

def send_mail_otp(email):
        subject = 'bigwig'
        otp =  random.randint(100000 ,999999)
        # user = User.objects.get(username = )

        message = f'Your  OTP is - {otp}' 
        email_from = settings.EMAIL_HOST
        # recipient_list = [User.email, ]
        send_mail( subject, message, email_from, [email] )
        user_obj = User.objects.get(email= email)

        user_obj.otp = otp
        # user_obj.password = otp

        user_obj.save()



# access_url = config('BASE_API_URL') + 'token/'
# access_response = requests.post(access_url, data=data)
# access_token = access_response.json().get('access')
# refresh_token = access_response.json().get('refresh')


# user registration 
from rest_framework.response import Response
from rest_framework.decorators import api_view






@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)
























from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .serializer import UserSerializer


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


    def create(self, request):
        # data = request.data
        # serializeremail = UserSerializer(data=data)
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        # serializeremail.is_valid(raise_exception=True)
        serializer.save()
        send_mail_otp(serializer.data['email'])

        return Response({'staus' : 200 , 'data' : serializer.data} ,status.HTTP_200_OK )












# class UserRegistrationView(APIView):


#     def post(self, request):

#         try:


#             data = request.data
#             serializer = UserRegistrationSerializer(data=data)
            
#             if serializer.is_valid():
#                 serializer.save()
#                 send_mail_otp(serializer.data['email'])

#                 status_code = status.HTTP_201_CREATED

#                 response = {
#                     'success': True,
#                     'statusCode': status_code,
#                     'message': 'User successfully registered!',

#                     'data': serializer.data,

#                 }

#                 return Response(response)

#             else:

#                 return Response({
#                     'statusCode': status_code,
#                     'message': 'something went wrong',
#                     'data': serializer.errors,

#                 })

#         except Exception as e:
#             return Response(e)







class UserRegistrationView(APIView):
    # serializer_class = UserRegistrationSerializer
    # permission_classes = (AllowAny, )


    def post(self, request):
        # serializer = self.serializer_class(data=request.data)
        # valid = serializer.is_valid(raise_exception=True)
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            # serializer.is_active == False
            serializer.save()
            # send_mail_otp(serializer.data['email'])


            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                # 'data': {'id':serializer.data["id"],'email':serializer.data["email"]}
                'data': serializer.data
            }
            # print(serializer.data["id"])
            return Response(response)

        else:
            return JsonResponse({"message":"email/username already exists"})






































# user verify by email otp

class UserVerifyView(APIView):


    def post(self, request):

        data = request.data
        serializer = VerifyUserOtpSerializer(data=data)

        if serializer.is_valid():
            email = serializer.data['email'] 
            otp = serializer.data['otp'] 
            

            user = User.objects.filter(email = email)
            otpcheck =  User.objects.filter(otp = otp)
            if not user.exists():
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'invalid email',
                }
                return Response(response)

            if user[0].otp != otp:
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'Wrong Otp',
                }
                return Response(response)
            
            user = user.first()
            user.is_verified = True
            user.save()
            return HttpResponse("verified")
            # response = {
            #     'success': True,
            #     'statusCode':200,
            #     'message': 'verified',
            #     'data':'Otp and email matched',
            # }


# class CustomThrottle(throttling.BaseThrottle):
#     def allow_request(self, request, view):
#          """
#          Return `True` if the request should be allowed, `False` otherwise.
#          """
#          return random.randint(1, 10) != 1

#     def wait(self):
#         """
#         Optionally, return a recommended number of seconds to wait before
#         the next request.
#         """
#         cu_second = 600
#         return cu_second

# class UserSecThrottle(CustomThrottle,UserRateThrottle):   # or AnonRateThrottle
#     scope = 'user_sec'

# class ExampleView(APIView):
#     throttle_classes = [UserSecThrottle]

class ResendOtpView(APIView):

    def post(self, request):

        data = request.data
        serializer = ResendOtpSerializer(data=data)

        if serializer.is_valid():
            email = serializer.data['email'] 
            # otp = serializer.data['otp'] 
            

            user = User.objects.filter(email = email)

            if not user.exists():
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'invalid email',
                }
                return Response(response)
            user = user.first()
            send_mail_otp(email)
        return HttpResponse("otp resend")






# ------------ firebase token replace login start ---------------------------------------


class UserLoginViewFirebaseTokenReplace(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        # User = serializer.data['email']
        if valid:
            status_code = status.HTTP_200_OK



            em = serializer.data['email']
            userf = User.objects.filter(email = em)
            print(userf)
            print(request.data["email"])
            # userf = userf.first()
            # userf.firebasetoken = True
            # userf.save()
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    # 'id':User.pk
                    # 'id': self.request.user.id
                    'role_id': serializer.data['role_id'], 
                    'user_id': serializer.data['user_id'], 
                    'is_verified':serializer.data['is_verified'],
                    'user_photo':serializer.data['user_photo'],

                }
            }

            return Response(response, status=status_code)






# ------------ firebase token replace login end ---------------------------------------














# login ------------------------------------------------------------------------






class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        # User = serializer.data['email']
        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    # 'id':User.pk
                    # 'id': self.request.user.id
                    'role_id': serializer.data['role_id'], 
                    'user_id': serializer.data['user_id'], 
                    'is_verified':serializer.data['is_verified'],
                    'user_photo':serializer.data['user_photo'],

                }
            }

            return Response(response, status=status_code)





# class UserLoginView(APIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:
#             status_code = status.HTTP_200_OK

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User logged in successfully',
#                 'access': serializer.data['access'],
#                 'refresh': serializer.data['refresh'],
#                 'authenticatedUser': {
#                     # 'email': serializer.data['email'],
#                 }
#             }

#             return Response(response, status=status_code)
            



################## RESET PASSWORD ###################################



class ResetPasswordView(APIView):
    def post(self,request):
        serializer=resetpasswordSerializer(data=request.data)
        # alldatas={}
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # alldatas['data']='successfully registered
            # print(alldatas)
            # return Response(alldatas)
            return JsonResponse({"data":"successfully registered"})
        return Response('failed retry after some time')


class ResetPasswordView2(APIView):


    def post(self, request):

        data = request.data
        serializer = ResetPasswordSer(data=data)

        if serializer.is_valid():
            email = serializer.data['email'] 
            otp = serializer.data['otp'] 
            password = serializer.data['password']
            

            user = User.objects.filter(email = email)
            otpcheck =  User.objects.filter(otp = otp)
            if not user.exists():
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'invalid email',
                }
                return Response(response)

            if user[0].otp != otp:
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'Wrong Otp',
                }
                return Response(response)
            
            user = user.first()
            # user.is_verified = True
            user.set_password(password)

            user.save()
            return HttpResponse("verified")

############################## RESET PASSWORD END ########################














#---------------------------------------logout ---------------------------------------


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return JsonResponse({"message":"logout"},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return JsonResponse({"message":"invalid token"},status=status.HTTP_400_BAD_REQUEST)










#---------------------------------------logout end -------------------------------------







#---------------------- user list view ------------------------


class UserListView(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserListSerializer

    def list(self, request):
        queryset = User.objects.filter(id = self.request.user.id)
        # queryset = EventlikeModel.objects.filter()

        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # not permitted check
        if instance.id != self.request.user.id:
            print(instance.id)
            print(self.request.user)
            raise exceptions.PermissionDenied()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



#-----------------------user list view end --------------------





































#################################################################################################


# class UserRegistrationView(APIView):
#     # serializer_class = UserRegistrationSerializer
#     # permission_classes = (AllowAny, )


#     def post(self, request):

#         try:


#             data = request.data
#             serializer = UserRegistrationSerializer(data=data)
            
#             if serializer.is_valid():
#                 serializer.save()
#                 send_mail_otp(serializer.data['email'])

#                 status_code = status.HTTP_201_CREATED
#                 # response_data = serializer.data
#                 # user = User.objects.get(username = response_data['username'])
#                 # refresh = RefreshToken.for_user(user)
#                 # response_data['refresh'] = str(refresh)
#                 # response_data['access'] = str(refresh.access_token)
#                 response = {
#                     'success': True,
#                     'statusCode': status_code,
#                     'message': 'User successfully registered!',
#                     # "access_token": str(refresh),
#                     # "refresh_token" : str(refresh.access_token),
#                     'data': serializer.data,

#                 }

#                 return Response(response)



#             return Response({
#                 'statusCode': status_code,
#                 'message': 'something went wrong',
#                 'data': serializer.errors,

#             })

#         except Exception as e:
#             print(e)

