from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from core.serializers import *
from core.models import *
import logging

# Create your views here.

class SongAPI(APIView):
    __doc__ = """
    API for create update get and delete 
    """
    def post(self, request):
        try:
            data = request.data
            if not "uploaded" in request.data:
            	return Response(
                        {"status": True, "message":"uploaded datetime is required", },
                        status=status.HTTP_201_CREATED,
                    )
            if data['uploaded'] < datetime.datetime.now():
           	    return Response(
                        {"status": True, "message":"make sure past datetime is not valid", },
                        status=status.HTTP_201_CREATED,
                    )
            if data['type'] == 'song':
                serializer_class = SongSerializer
            elif data['type'] == 'podcast':
                serializer_class = PodcastSerializer
            elif data['type'] == 'audiobook':
                serializer_class = AudiobookSerializer
            else:
                return Response(
                        {"status": True, "message":"please select valid songe type", },
                        status=status.HTTP_201_CREATED,
                    )

            logging.info(request.data)
            logging.info("===============song create =======================")
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                        {"status": True, "message":"You're sone create successfully", "data":serializer.data},
                        status=status.HTTP_201_CREATED,
                    )
        except Exception as e:
            return Response(
                {"status": False, "message":str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, id):
        try:
            data = request.data
            if data['type'] == 'song':
                serializer_class = SongSerializer()
                obj = SongModel.objects.filter(id=id)
            elif data['type'] == 'podcast':
                serializer_class = PodcastSerializer
                obj = PodcastModel.objects.filter(id=id)
            elif data['type'] == 'audiobook':
                serializer_class = AudiobookSerializer
                obj = AudiobookModel.objects.filter(id=id)
            else:
                return Response(
                        {"status": True, "message":"please select valid songe type", },
                        status=status.HTTP_201_CREATED,
                    )

            logging.info(request.data)
            logging.info("===============song create =======================")
            serializer = serializer_class(obj, many=True)
            return Response(
                        {"status": True, "message":"You're sone create successfully", "data":serializer.data},
                        status=status.HTTP_201_CREATED,
                    )
        except Exception as e:
            return Response(
                {"status": False, "message":str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id):
        try:
            data = request.data
            if data['type'] == 'song':
                serializer_class = SongSerializer()
                obj = SongModel.objects.filter(id=id).first()

            elif data['type'] == 'podcast':
                serializer_class = PodcastSerializer
                obj = PodcastModel.objects.filter(id=id).first()
                
            elif data['type'] == 'audiobook':
                serializer_class = AudiobookSerializer
                obj = AudiobookModel.objects.filter(id=id).first()
                
            else:
                return Response(
                        {"status": True, "message":"please select valid songe type", },
                        status=status.HTTP_201_CREATED,
                    )
            if obj:
	            obj.delete()
	            return Response(
	                        {"status": True, "message":"song delete successfully", },
	                        status=status.HTTP_201_CREATED,
	                    )
            else:
                return Response(
                        {"status": True, "message":"please enter a valid id", },
                        status=status.HTTP_201_CREATED,
                    )
        except Exception as e:
            return Response(
                {"status": False, "message":str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, id):
        try:
            data = request.data
            if "uploaded" in request.data:
            	if data['uploaded'] < datetime.datetime.now():
           	    return Response(
                        {"status": True, "message":"make sure past datetime is not valid", },
                        status=status.HTTP_201_CREATED,
                    )
            	return Response(
                        {"status": True, "message":"uploaded datetime is required", },
                        status=status.HTTP_201_CREATED,
                    )

            if data['type'] == 'song':
                serializer_class = SongSerializer()
                obj = SongModel.objects.filter(id=id).update(name=data['name'],duration=data['duration'])
                
                return Response(
	                        {"status": True, "message":"song update successfully", },
	                        status=status.HTTP_201_CREATED,
	                    )
            elif data['type'] == 'podcast':
                serializer_class = PodcastSerializer
                obj = PodcastModel.objects.filter(id=id).update(
                								name=data['name'],
                								duration=data['duration'],
                								host=data['host'],
                								participants=data['participants'],
                								)
                return Response(
	                        {"status": True, "message":"song update successfully", },
	                        status=status.HTTP_201_CREATED,
	                    )
            elif data['type'] == 'audiobook':
                serializer_class = AudiobookSerializer
                obj = AudiobookModel.objects.filter(id=id).update(
                								duration=data['duration'],
                								title_audiobook=data['title_audiobook'],
                								author_title=data['author_title'],
                								narrator=data['narrator'],
                								)
                return Response(
	                        {"status": True, "message":"song update successfully", },
	                        status=status.HTTP_201_CREATED,
	                    )
            else:
                return Response(
                        {"status": True, "message":"please select valid songe type", },
                        status=status.HTTP_201_CREATED,
                    )
         
        except Exception as e:
            return Response(
                {"status": False, "message":str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )