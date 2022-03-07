from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Campaign, QRCode, Question, Response
from .serializers import UserSerializer


# Returns the survey data and stores the survey response
@api_view(["GET", "POST"])
def survey(request) -> Response:
    if request.method == "GET":
        user_id = request.query_params.get("user_id", None)
        result_id = request.query_params.get("result_id", None)
        if result_id:
            try:
                result = Result.objects.get(pk=int(result_id))
                serializer = ResultSerializer(result)
                return Response(serializer.data)
            except Result.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif user_id:
            try:
                results = Result.objects.filter(user_id=int(user_id))
                serializer = ResultSerializer(results, many=True)
                return Response(serializer.data)
            except Exception:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "POST":
        data = JSONParser().parse(request)
        sequence = data.get("dna_sequence")
        user_id = int(data.get("user_id"))
        sequence = sequence.upper()
        find_protein_and_location.apply_async(
            kwargs={"sequence": sequence, "user_id": user_id}
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
