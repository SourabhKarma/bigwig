from dataclasses import field
from encodings import utf_8
from re import A
from rest_framework import serializers
from .models import area,ward
import base64
from drf_extra_fields.fields import Base64ImageField,Base64FieldMixin




# class LibrarySerializer(serializers.ModelSerializer):

#     address = AddressSerializer()
#     specific_information = SpecificSerializer(many=True)
#     register_rules = RegisterRulesSerialzers(many=True)

#     class Meta:
#         model = Library
#         fields = ('id', 'name', 'address', 'reading_room', 'reading_room_start_time'
#                   , 'reading_room_end_time', 'library_start_time', 'library_end_time'
#                   , 'specific_information', 'register_rules', 'gender_days_in_week'
#                   , 'manager_of_library', 'tel_number', 'email', 'from_user')

#     def create(self, validated_data):
#         address_data = validated_data.pop('address')
#         address = Address.objects.create(**validated_data)

#         register_rules_data = validated_data.pop('register_rules')
#         register_rules = RegisterRule.objects.create(**validated_data)

#         specific_information_data = validated_data.pop('specific_information')
#         specific_information = SpecificInformatin.objects.create(**validated_data)

#         library = Library.objects.create(**validated_data)

#         library.address(address=address, **address_data)

#         for data in register_rules_data:
#             library.register_rules.add(register_rules=register_rules, **data)
#         for data in specific_information_data:
#             library.specific_information.add(specific_information=specific_information, **data)

#         return library







class area_serializerward(serializers.ModelSerializer):


    class Meta:
        # area = base64.b64decode(area)
        model = area
        fields = "__all__"
        
    def create(self, validated_data):
        area_name_data = validated_data.pop('area_name',None)
        area_name = base64.b64encode(area_name_data)
        return area_name






class ward_serializer(serializers.ModelSerializer):
    user  = area_serializerward()
    class Meta:
        model = ward
        # fields = (
        #     'ward_name',
        #     'pincode',
        #     # 'area_id',
        # )
        # fields = "__all__"
        depth = 1






# class area_serializer(serializers.ModelSerializer):
#     # ward = ward_serializer(source ='ward_set',allow_null = True,many=True,read_only=True)
#     class Meta:
#         model = area
#         fields = (
#             # 'id',
#             'area_name',
#             # 'ward',
#         )
#     def create(self, validated_data,):
#         area_name_data = validated_data.pop('area_name',None)
#         area_name = base64.b64encode(bytes(str(area_name_data),'utf_8'))
#         # area_name.save()
#         return area_name


class area_serializer(serializers.ModelSerializer):

    class Meta:
        model = area
        fields = (
            'id',
            'area_name',
        )

    # area_names = base64.b64encode(bytes(str(area_names),'utf_8'))

    # def create(self, validated_data):
    #     return area(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.area_name = validated_data.get('area_name', instance.area_name)
    #     return instance




# class area_serializer(serializers.Serializer):

#     area_name = serializers.CharField()

#     def save(self):
#         area_name = self.validated_data['area_name']























































# class areaser(serializers.ModelSerializer):

#     area_name = serializers.CharField(write_only=True)


#     def create(self, validated_data):

#         Area = area.objects.create_user(
#             # username=validated_data['username'],
#             area_name=validated_data['area_name'],
#         )

#         return Area
        
#     class Meta:
#         model = area
#         # Tuple of serialized model fields (see link [2])
#         fields = ( "area_name",)