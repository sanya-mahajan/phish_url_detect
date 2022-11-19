from rest_framework import serializers
from home.models import *
import uuid
import shutil
from numpy import require

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'



class files_list_serializer(serializers.Serializer):
    files=serializers.ListField(
        child=serializers.FileField(max_length=100000,allow_empty_file=False,use_url=False)
    )
    folder=serializers.CharField(required=False)


    def zip_files(self,folder):
        shutil.make_archive(f'public/media/static/zip/{folder}', 'zip',f'public/media/static/{folder}')    




    def create(self,validated_data):
        folder=Folder.objects.create()
        files=validated_data.pop('files')
        file_objs=[]
        for file in files:
            file_obj=Files.objects.create(folder=folder,file=file)
            file_objs.append(file_obj)
        

        self.zip_files(folder.uid)
        return {'files':{},'folder':str(folder.uid)} 


    