from django.shortcuts import get_object_or_404
from .models import Account,ServiceProvider,Partner,Service,Bill,PartnerEmploye,PartnerService,BillPartner
from .serlializers import AccountSerializer,ServiceProviderSerializer,PartnerSerializer,ServiceSerializer,BillSerializer,PartnerEmployeSerializer,PartnerServiceSerializer,BillPartnerSerializer
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

###
#	Account
###
@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration_view(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login_view(request):
	if request.method == 'POST':
		username = request.data.get('username')
		password = request.data.get('password')
		staff=request.data.get('staff')
		user = authenticate(request, username=username, password=password)
		if staff:
			if user and user.is_staff==staff:
				login(request, user)
				token, created = Token.objects.get_or_create(user=user)
				return Response({'token': token.key,'id':user.id}, status=status.HTTP_200_OK)
			return Response({'detail': 'Invalid credentials Or not Staff'}, status=status.HTTP_401_UNAUTHORIZED)
		else:
			if user:
				login(request, user)
				token, created = Token.objects.get_or_create(user=user)
				return Response({'token': token.key,'id':user.id}, status=status.HTTP_200_OK)
			return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_accounts(request, pk):
	item = Account.objects.get(pk=pk)
	data = AccountSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def view_account(request):
	# checking for the parameters from the URL
	if request.query_params:
		account = Account.objects.filter(**request.query_params.dict())
	else:
		account = Account.objects.all()
	# if there is something in service else raise error
	if account:
		serializer = AccountSerializer(account, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

###
#	ServiceProvider
###

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_service_provider(request):
	# checking for the parameters from the URL
	if request.query_params:
		service_provider = ServiceProvider.objects.filter(**request.query_params.dict())
	else:
		service_provider = ServiceProvider.objects.all()
	# if there is something in service else raise error
	if service_provider:
		serializer = ServiceProviderSerializer(service_provider, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

# @permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_service_provider(request):
	item = ServiceProviderSerializer(data=request.data)
	# validating for already existing data
	if ServiceProvider.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_service_provider(request, pk):
	item = ServiceProvider.objects.get(pk=pk)
	data = ServiceProviderSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_service_provider(request, pk):
	item = get_object_or_404(ServiceProvider, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

###
#	Partner
###

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_partner(request):
	# checking for the parameters from the URL
	if request.query_params:
		partner = Partner.objects.filter(**request.query_params.dict())
	else:
		partner = Partner.objects.all()
	# if there is something in service else raise error
	if partner:
		serializer = PartnerSerializer(partner, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_partner(request):
	item = PartnerSerializer(data=request.data)
	# validating for already existing data
	if Partner.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_partner(request, pk):
	item = Partner.objects.get(pk=pk)
	data = PartnerSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_partner(request, pk):
	item = get_object_or_404(Partner, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

###
#	Service
###

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_service(request):
	# checking for the parameters from the URL
	if request.query_params:
		service = Service.objects.filter(**request.query_params.dict())
	else:
		service = Service.objects.all()
	# if there is something in service else raise error
	if service:
		serializer = ServiceSerializer(service, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_service(request):
	item = ServiceSerializer(data=request.data)
	# validating for already existing data
	if Service.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_service(request, pk):
	item = Service.objects.get(pk=pk)
	data = ServiceSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_service(request, pk):
	item = get_object_or_404(Service, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

###
#	Bill
###

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_bill(request):
	# checking for the parameters from the URL
	if request.query_params:
		bill = Bill.objects.filter(**request.query_params.dict())
	else:
		bill = Bill.objects.all()
	# if there is something in service else raise error
	if bill:
		serializer = BillSerializer(bill, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bill(request):
	item = BillSerializer(data=request.data)
	# validating for already existing data
	if Bill.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_bill(request, pk):
	item = Bill.objects.get(pk=pk)
	data = BillSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_bill(request, pk):
	item = get_object_or_404(Bill, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

###
#	PartnerEmploye
###

# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def view_partner_employe(request):
	# checking for the parameters from the URL
	if request.query_params:
		partnerEmploye = PartnerEmploye.objects.filter(**request.query_params.dict())
	else:
		partnerEmploye = PartnerEmploye.objects.all()
	# if there is something in service else raise error
	if partnerEmploye:
		serializer = PartnerEmployeSerializer(partnerEmploye, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_partner_employe(request):
	item = PartnerEmployeSerializer(data=request.data)
	# validating for already existing data
	if PartnerEmploye.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_partner_employe(request, pk):
	item = PartnerEmploye.objects.get(pk=pk)
	data = PartnerEmployeSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_partner_employe(request, pk):
	item = get_object_or_404(PartnerEmploye, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

###
#	PartnerService
###

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_partner_service(request):
	# checking for the parameters from the URL
	if request.query_params:
		partnerService = PartnerService.objects.filter(**request.query_params.dict())
	else:
		partnerService = PartnerService.objects.all()
	# if there is something in service else raise error
	if partnerService:
		serializer = PartnerServiceSerializer(partnerService, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_partner_service(request):
	item = PartnerServiceSerializer(data=request.data)
	# validating for already existing data
	if PartnerService.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_partner_service(request, pk):
	item = PartnerService.objects.get(pk=pk)
	data = PartnerServiceSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_partner_service(request, pk):
	item = get_object_or_404(PartnerService, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

###
#	BillPartner
###

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_bill_partner(request):
	# checking for the parameters from the URL
	if request.query_params:
		billPartner = BillPartner.objects.filter(**request.query_params.dict())
	else:
		billPartner = BillPartner.objects.all()
	# if there is something in service else raise error
	if billPartner:
		serializer = BillPartnerSerializer(billPartner, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bill_partner(request):
	item = BillPartnerSerializer(data=request.data)
	# validating for already existing data
	if BillPartner.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_bill_partner(request, pk):
	item = BillPartner.objects.get(pk=pk)
	data = BillPartnerSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_bill_partner(request, pk):
	item = get_object_or_404(BillPartner, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
