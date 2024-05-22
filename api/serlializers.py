from django.db.models import fields
from rest_framework import serializers
from .models import Account,ServiceProvider,Partner,Service,Bill,PartnerEmploye,PartnerService,BillPartner

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
# 		fields = '__all__'
		fields = ['id','username','first_name','last_name','dob','gender','email','password','phone_number']
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = Account(
            email=validated_data['email'],
            username=validated_data['username'],
			first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            dob=validated_data['dob'],
            gender=validated_data['gender'],
            phone_number=validated_data['phone_number'],
            # profile_img=validated_data['profile_img'],
            # id_card_img=validated_data['id_card_img'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user
		
class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bill
		fields = '__all__'
		
class ServiceProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiceProvider
		fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Partner
		fields = '__all__'

class PartnerEmployeSerializer(serializers.ModelSerializer):
	class Meta:
		model = PartnerEmploye
		fields = '__all__'

class PartnerServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = PartnerService
		fields = '__all__'

class BillPartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = BillPartner
		fields = '__all__'
