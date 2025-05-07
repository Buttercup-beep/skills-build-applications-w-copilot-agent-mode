
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from bson import ObjectId


# Connexion MongoDB utilitaire
def get_db():
    # Utilise le même host/port que settings.py DJONGO
    client = MongoClient('localhost', 27017)
    return client['octofit_db']

def serialize_id(obj):
    if '_id' in obj:
        obj['_id'] = str(obj['_id'])
    return obj

@api_view(['GET'])
def mongo_debug(request):
    try:
        db = get_db()
        collections = db.list_collection_names()
        stats = {}
        for coll in collections:
            stats[coll] = db[coll].count_documents({})
        # Récupère un échantillon de chaque collection
        sample = {}
        for coll in collections:
            sample[coll] = [serialize_id(doc) for doc in db[coll].find().limit(3)]
        return Response({
            'collections': collections,
            'stats': stats,
            'sample': sample
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)






@api_view(['GET'])
def api_root(request, format=None):
    base_url = "https://psychic-barnacle-5g56q7jj496qc7qwx-8000.app.github.dev"
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })

from rest_framework.viewsets import ViewSet

class UserViewSet(ViewSet):
    def list(self, request):
        db = get_db()
        users = list(db['users'].find())
        print(f"[DEBUG] users from MongoDB: {users}")
        return Response([serialize_id(u) for u in users])

class TeamViewSet(ViewSet):
    def list(self, request):
        db = get_db()
        teams = list(db['teams'].find())
        print(f"[DEBUG] teams from MongoDB: {teams}")
        for t in teams:
            t['members'] = [str(m) for m in t.get('members', [])]
        return Response([serialize_id(t) for t in teams])

class ActivityViewSet(ViewSet):
    def list(self, request):
        db = get_db()
        activities = list(db['activity'].find())
        print(f"[DEBUG] activities from MongoDB: {activities}")
        for a in activities:
            a['user'] = str(a.get('user'))
        return Response([serialize_id(a) for a in activities])

class LeaderboardViewSet(ViewSet):
    def list(self, request):
        db = get_db()
        leaderboard = list(db['leaderboard'].find())
        print(f"[DEBUG] leaderboard from MongoDB: {leaderboard}")
        for l in leaderboard:
            l['user'] = str(l.get('user'))
        return Response([serialize_id(l) for l in leaderboard])

class WorkoutViewSet(ViewSet):
    def list(self, request):
        db = get_db()
        workouts = list(db['workouts'].find())
        print(f"[DEBUG] workouts from MongoDB: {workouts}")
        return Response([serialize_id(w) for w in workouts])

