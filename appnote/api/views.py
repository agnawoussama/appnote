from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

#Get all notes
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updated_at')
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)

#Get a single note
@api_view(['GET'])
def getNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)

#Create a new note
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        title=data['title'],
        body=data['body']
    )
    
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


#Update a note
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#Delete a note
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response("Deleted")
