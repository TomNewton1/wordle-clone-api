from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from ..services.word_service import WordService

WORD_LENGTH = 5


class WordSerializer(serializers.Serializer):
    word = serializers.CharField(min_length=WORD_LENGTH, max_length=WORD_LENGTH)


class ValidateWordView(APIView):
    """
    API view to validate a posted word against the word of the day.
    """

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            word_service = WordService()
            word_of_the_day = word_service.get_word_for_today()
            if not word_of_the_day:
                return Response(
                    {"error": "Word of the day not found"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            posted_word = serializer.validated_data["word"].strip().lower()

            response_data = []
            for index, letter in enumerate(posted_word):
                letter_status = {"letter": letter.upper(), "status": ""}
                if letter == word_of_the_day[index]:
                    letter_status["status"] = "correct"
                elif letter in word_of_the_day:
                    letter_status["status"] = "present"
                else:
                    letter_status["status"] = "incorrect"
                response_data.append(letter_status)

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
