import os
import torch
import base64
from PIL import Image
import torchvision.transforms as transforms
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Informationdrug, UrlImgUser
from .serializers import Informationdrug_Serializer
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@csrf_exempt
@api_view(['POST'])
def classify_drug(request):
    if 'image' not in request.FILES:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

    image_file = request.FILES['image']
    image_url = save_image(image_file)

    try:
        drug_name = detect_drug(image_file)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    try:
        drug_info = Informationdrug.objects.get(namedrug=drug_name) # Lấy thông tin thuốc từ cơ sở dữ liệu
    except Informationdrug.DoesNotExist:
        return Response({'error': 'Drug not found in database'}, status=status.HTTP_404_NOT_FOUND)

    serializer = Informationdrug_Serializer(drug_info) # Serialize thông tin thuốc
    
    response_data = { # Trả về thông tin thuốc và ảnh gốc
        'drug_info': serializer.data,
        'image': image_url
    }

    return Response(response_data, status=status.HTTP_200_OK)

def save_image(image_file):
    # Lưu file ảnh vào default storage
    image_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
    # Tạo URL cho ảnh đã lưu
    image_url = default_storage.url(image_name)
    
    # Lưu URL vào bảng dữ liệu UrlImgUser
    # url_img_user = UrlImgUser.objects.create(imgUser=image_url)
    # url_img_user.save()

    return image_url

def detect_drug(image):
    model_path = os.path.join(os.path.dirname(__file__), 'ResNet18.pth')
    resnet = torch.load(model_path, map_location=torch.device('cpu'))
    resnet.eval()

    transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                 std=[0.229, 0.224, 0.225]),
        ])

    # Đọc nội dung file ảnh và mở nó bằng PIL
    # Read image data
    image_data = Image.open(image)
    image = transform(image_data).unsqueeze(0)

    output = resnet(image)
    _, predicted_idx = torch.max(output, 1)
    classes = ['3B-Medi', 'Agifamcin', 'Agifovir', 'Alpha-Choay',
               'Alprazolam-Mylam', 'Ambron', 'Ameflu-Daytime',
               'Amlodipin', 'Apha-Bevagyl', 'Arcalion']
    drug_name = classes[predicted_idx]
    return drug_name