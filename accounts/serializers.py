from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import User,Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    phone_number=serializers.CharField(max_length=13)
    short_info=serializers.CharField()
    password=serializers.CharField(write_only=True,validators=[
        RegexValidator(
            regex='^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w@#$%^&+=]{8,}$',
            message='пароль должен содержать цифру и спецсимвол и он должен быть не менее 8 символов'
        )])
    password_2=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["username","password","profile_image",'phone_number','short_info','password_2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_2 = attrs.get('password_2')
        if password != password_2:
            raise serializers.ValidationError("пароли не совпадают")
        return attrs

    def create(self,validated_data):
        user=User(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        profile_image = validated_data.get('profile_image')
        if profile_image:
            user.profile_image=profile_image
        user.set_password(validated_data['password'])
        user.save()
        try:
            profile=Profile.objects.create(
                user=user,
                phone_number=validated_data['phone_number'],
                short_info=validated_data['short_info']
            )
        except Exception as e:
            user.delete()
            raise e
        else:
            profile.username=user.username
            profile.profile_image=user.profile_image
        return profile

