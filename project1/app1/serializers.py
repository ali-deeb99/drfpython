from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator
from django.contrib.auth.password_validation import validate_password
from . models import Student,Company,Teacher,Obada,ApplicationForm
class RegisterUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(
        write_only=True,required=True,validators=[validate_password]
    )
    confirm_password=serializers.CharField(write_only=True,required=True) 
    account_type=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','confirm_password','account_type']
    def validate(self, attrs):
        if attrs['password']!=attrs['confirm_password']:
            raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
        
        return  attrs
    def create(self, validated_data):
        user1=User.objects.create(username=validated_data['username'],email=validated_data['email'],)
        user1.set_password(validated_data['password'])
        user1.save()
        account_type =validated_data['account_type']
        if account_type=="Student":
            student=Student.objects.create(user=user1)
            student.save()
        elif account_type=="Company":
            company=Company.objects.create(user=user1)
            company.save()
        
        


        return user1
    

class ApplicationFormSerailizer(serializers.ModelSerializer):
    class Meta:
        model=ApplicationForm
        fields="__all__"
        


class ObadaSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Obada
        fields=['name']