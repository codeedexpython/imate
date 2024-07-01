from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Phone
from .serializers import PhoneSerializer


@api_view(['GET'])
def phone_list(request):
    phones = Phone.objects.all()
    serializer = PhoneSerializer(phones, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def phone_create(request):
    serializer = PhoneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def phone_detail(request, pk):
    phone = Phone.objects.get(pk=pk)
    serializer = PhoneSerializer(phone)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
def phone_update(request, pk):
    try:
        phone = Phone.objects.get(pk=pk)
    except Phone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PhoneSerializer(phone, data=request.data, partial=request.method == 'PATCH')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def phone_delete(request, pk):
    try:
        phone = Phone.objects.get(pk=pk)
    except Phone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    phone.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def phone_search(request):
    phone_name = request.GET.get('name', None)
    if not phone_name:
        return Response({'error': 'Parameter "name" is required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        phones = Phone.objects.filter(name__icontains=phone_name)
        if not phones.exists():
            return Response({'error': 'No phones found with the provided name.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PhoneSerializer(phones, many=True)
        response_data = []
        for phone in serializer.data:
            response_data.append({
                'phone_name': phone['name'],
                'availability': phone['location'],
            })
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def phone_search_stock(request):
    try:
        phones = Phone.objects.filter(quantity=1)
        if not phones.exists():
            return Response({'message': 'No phones with quantity 1 found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PhoneSerializer(phones, many=True)
        response_data = []
        for phone in serializer.data:
            if phone['quantity'] == 1:
                message = f"Only 1 unit left of {phone['name']}. Limited stock!"
            else:
                message = f"{phone['name']} is available."

            response_data.append({
                'phone_name': phone['name'],
                'message': message,
            })

        return Response(response_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def filter_location(request):
    location = request.GET.get('location', None)
    if not location:
        return Response({'error': 'Parameter "location" is required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        phones = Phone.objects.filter(location__iexact=location)
        if not phones.exists():
            return Response({'message': f'No phones found in location: {location}.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PhoneSerializer(phones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)