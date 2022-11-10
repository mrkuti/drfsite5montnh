from rest_framework import status # импортировал для вывода статуса запроса
from rest_framework.decorators import api_view, permission_classes  # импортировал декотратор для проверки на валидность проверки
from rest_framework.response import Response #  импортирвал для выдачи запроса
from rest_framework.permissions import IsAuthenticated # импортировал класс для проверки  для авторирзованных пользователей
from movie_app.models import Director, Movie, Review # импортировал модели из главного приложения
from movie_app.serializers import DirectorSerializer, \
    MovieSerializer, \
    ReviewSerializer,\
    DirectorValidateSerializers,\
    MovieValidateSerializers,\
    ReviesValidateSerializers # импортировал сериалиаторы и валидаторы




@api_view(['GET', 'POST'])
def directors(request):
    if request.method == "GET":
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializers = DirectorValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        name = request.data.get('name')
        Director.objects.create(
            name=name
        )
        return Response()

#  ^- метод для вывода директора гет и пост запроса так же присутствует валидатор и создание директора




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movies(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializers = MovieValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response()

# ^- тот же метод только для фильмов только здесь присутствует приоверка на правльность пароля для пользователей и доступ коньента авторизованным позльховаеттелям




@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializers = ReviesValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id,
        )
        return Response()

#
@api_view(["GET", "PUT", "DELETE"])
def director_item(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = DirectorValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorSerializer(director).data)







@api_view(["GET","PUT", ])
def movie_item(request, id):
    try:
         movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serialzers = ReviesValidateSerializers(data=request.data)
        if not serialzers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serialzers.errors})
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        title.save()
        description.save()
        duration.save()
        director_id.save()
        return Response(data=MovieSerializer(movie).data)






@api_view(["GET"])
def review_item(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = ReviesValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        text.save()
        stars.save()
        movie_id.save()
        return Response(data=ReviewSerializer(review).data)
