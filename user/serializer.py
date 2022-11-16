
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
# from django.contrib.auth import  get_user_model
# from django.contrib.auth.models import User
from .managers import UserManager








# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         # The default result (access/refresh tokens)
#         data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
#         # Custom data you want to include
#         data.update({'user': self.user.username})
#         data.update({'id': self.user.id})
#         # and everything else you want to send in the response
#         return data



# from django.contrib.auth import get_user_model # If used custom user model
# UserModel = get_user_model()

from django.conf import settings
import random
from django.core.mail  import send_mail





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











class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()


    def create(self, validated_data):

        user = User.objects.create_user(
            # username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],

        )

        return user
        
    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "password", "email","is_verified")




class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'role_id',
            'user_photo',
            'area',
            'ward',
            'pincode',
            'profession',
            'mobile',
            'is_verified',
        )
    # def create(self, validated_data):
    #     auth_user = User.objects.create_user(**validated_data)
    #     return auth_user

    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user












class VerifyUserOtpSerializer(serializers.Serializer):
    email  = serializers.EmailField()
    otp =  serializers.CharField()


class ResendOtpSerializer(serializers.Serializer):
    email  = serializers.EmailField()








# login


class UserLoginSerializer(serializers.Serializer):
    # username = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role_id = serializers.CharField(read_only=True)
    user_id = serializers.CharField(read_only=True)
    is_verified = serializers.CharField(read_only=True)
    user_photo = serializers.FileField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        # username = data['username']
        email = data['email']
        password = data['password']
        print(email)
        print(password)
        User = authenticate(email= email, password=password)

        if User is None:
            raise serializers.ValidationError("Invalid login")

        try:
            refresh = RefreshToken.for_user(User)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, User)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': User.email,
                'role_id': User.role_id,
                'user_id':User.id,
                'is_verified':User.is_verified,
                'user_photo':User.user_photo,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")






#########################################   RESET PASSWORD ##############################




class resetpasswordSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)


    class Meta:
        model=User
        fields='__all__'
        def save(self):
            username=self.validated_data['username']
            password=self.validated_data['password']


            if User.objects.filter(username=username).exists():
              user=User.objects.get(username=username)
              user.set_password(password)
              user.save()
              return user


            else:
                raise serializers.ValidationError({'error':'please enter valid crendentials'})





class ResetPasswordSer(serializers.Serializer):
    email  = serializers.EmailField()
    otp =  serializers.CharField()
    password = serializers.CharField()









#########################################   RESET PASSWORD END ##############################




#-------------------------------------- user list -----------------------------------


class UserListSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model=User
    #     fields= ("id")
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'role_id',
            'user_photo',
            'area',
            'ward',
            'pincode',
            'profession',
            'mobile',
            'is_verified',
        )








#--------------------------------------user list end --------------------------------












# class ResendOtpView(APIView):

#     def post(self, request):

#         data = request.data
#         serializer = ResendOtpSerializer(data=data)

#         if serializer.is_valid():
#             email = serializer.data['email'] 
#             # otp = serializer.data['otp'] 
            

#             user = User.objects.filter(email = email)

#             tm = th.Timer(3600, 'hello')
    
#             if request.method == 'POST' and not tm.is_alive():
        
#                 tm.start()
#                 if not user.exists():
#                     response = {
#                         'success': True,
#                         'statusCode':400,
#                         'message': 'something went worng',
#                         'data':'invalid email',
#                     }
#                     return Response(response)
#                 user = user.first()
#                 send_mail_otp(email)
#             # return HttpResponse("wait for 60 sec")

#         return HttpResponse("otp resend")