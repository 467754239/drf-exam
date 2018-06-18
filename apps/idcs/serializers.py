
from .models import Idc

from rest_framework import serializers



class IdcSerializer(serializers.Serializer):
    '''
        Idc 序列化类
    '''
    id                  = serializers.IntegerField(read_only=True)
    name                = serializers.CharField(required=True, max_length=32)
    address             = serializers.CharField(required=True, max_length=256)
    phone               = serializers.CharField(required=True, max_length=11)
    email               = serializers.EmailField(required=True, max_length=32)
    letter              = serializers.CharField(required=True, max_length=5)

    def create(self, validated_data):
        # 不传递id 要做创建
        # 传递id 要做修改
        # validated_data 非常干净的数据
        # create 验证
        print("-----Create Serializer-----", validated_data)
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 可做过滤修改
        print("-----Update Serializer-----", validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
