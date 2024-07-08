from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import ValidationError

class LoginSerialiazer (serializers.Serializer) :
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try :
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : 'invalid email'
            })
        
        if not self.user.check_password(password) : 
            raise ValidationError({
                'message' : 'invalid password'
            })
    
        return attrs
    

    @property
    def tokens (self) :
        if not hasattr(self, 'user'):
            raise ValidationError({
                'message' : 'an error accoured while getting user'
            })
        user_token = RefreshToken.for_user(self.user)
        data = {
            'refresh_token' : str(user_token),
            'access_token' : str(user_token.access_token),
        }
        return data