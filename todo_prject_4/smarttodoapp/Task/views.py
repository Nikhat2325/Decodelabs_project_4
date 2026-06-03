from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer

# TASK LIST + CREATE


class TaskListCreateView(generics.ListCreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Task.objects.filter(
            user=self.request.user
        )

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            user=self.request.user
        )


# ==================================
# TASK DETAIL
# GET SINGLE TASK
# UPDATE TASK
# DELETE TASK
# ==================================

class TaskDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Task.objects.filter(
            user=self.request.user
        )


# ==================================
# COMPLETE TASK
# ==================================

class CompleteTaskView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(
        self,
        request,
        pk
    ):

        try:

            task = Task.objects.get(
                id=pk,
                user=request.user
            )

            task.completed = True
            task.status = "Completed"

            task.save()

            return Response(
                {
                    "success": True,
                    "message":
                    "Task marked as completed"
                },
                status=status.HTTP_200_OK
            )

        except Task.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message":
                    "Task not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )


# ==================================
# DASHBOARD API
# ==================================

class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(
        self,
        request
    ):

        tasks = Task.objects.filter(
            user=request.user
        )

        total_tasks = tasks.count()

        completed_tasks = tasks.filter(
            completed=True
        ).count()

        pending_tasks = tasks.filter(
            completed=False
        ).count()

        high_priority = tasks.filter(
            priority='High'
        ).count()

        medium_priority = tasks.filter(
            priority='Medium'
        ).count()

        low_priority = tasks.filter(
            priority='Low'
        ).count()

        completion_rate = 0

        if total_tasks > 0:

            completion_rate = round(
                (
                    completed_tasks
                    /
                    total_tasks
                ) * 100,
                2
            )

        return Response({

            "total_tasks":
            total_tasks,

            "completed_tasks":
            completed_tasks,

            "pending_tasks":
            pending_tasks,

            "high_priority":
            high_priority,

            "medium_priority":
            medium_priority,

            "low_priority":
            low_priority,

            "completion_rate":
            completion_rate

        })


# ==================================
# SEARCH TASK
# ==================================

class SearchTaskView(
    generics.ListAPIView
):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        search = self.request.GET.get(
            'search'
        )

        queryset = Task.objects.filter(
            user=self.request.user
        )

        if search:

            queryset = queryset.filter(
                title__icontains=search
            )

        return queryset


# ==================================
# FILTER BY PRIORITY
# ==================================

class PriorityFilterView(
    generics.ListAPIView
):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        priority = self.request.GET.get(
            'priority'
        )

        queryset = Task.objects.filter(
            user=self.request.user
        )

        if priority:

            queryset = queryset.filter(
                priority=priority
            )

        return queryset


# ==================================
# FILTER BY STATUS
# ==================================

class StatusFilterView(
    generics.ListAPIView
):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        status_value = self.request.GET.get(
            'status'
        )

        queryset = Task.objects.filter(
            user=self.request.user
        )

        if status_value:

            queryset = queryset.filter(
                status=status_value
            )

        return queryset
    
    
from .serializers import (
    TaskSerializer,
    RegisterSerializer
)

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(
    generics.CreateAPIView
):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
from django.shortcuts import render


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')


def dashboard_page(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')