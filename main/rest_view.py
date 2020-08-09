from main.models import Record
from main.serializers import RecordSerialize
from rest_framework import generics



class RecordAllGetter(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerialize



class RecordGetter(generics.RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerialize


class RecordSetter(generics.UpdateAPIView):

    queryset = Record.objects.all()
    serializer_class = RecordSerialize

# @api_view(["GET"])
# def get_record(request,st,pk):
#     if request.method == "GET":
#         if st:
#             records = Record.objects.filter(pk=self.kwargs["pk"])
#             records_serializer = RecordSerialize(records, many=True)
#             return Response(records_serializer.data)
#         records = Record.objects.filter(seen=False)
#         records_serializer = RecordSerialize(records, many=True)
#         return Response(records_serializer.data)  

# class PutRecord(View):
#     """This class releases put method to update model data"""

#     def put(self, request, *args, **kwargs) -> JsonResponse:
#         """Updates data and returns JsonResponse with a confirming about updated data"""

#         data = JSONParser().parse(request)
#         model = Record.objects.get(pk=self.kwargs["pk"])
#         serializer = RecordSerialize(model, data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
