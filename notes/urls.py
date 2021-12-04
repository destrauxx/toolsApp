from django.urls import path

from .views import (
    CreateNoteView,
    ReadNotesView,
    UpdateNoteView,
    DeleteNoteView,
    create_collection,
    create_collection_form,
    delete_collection,
    mark_note_view,
)

urlpatterns = [
    path('read/', ReadNotesView.as_view(), name='read_notes'),
    path('create/', CreateNoteView.as_view(), name='create_note'),
    path('delete/<int:pk>/', DeleteNoteView.as_view(), name='delete_note'),
    path('edit/<int:pk>/', UpdateNoteView.as_view(), name='edit_note'),
    path('collection/create', create_collection, name='create_collection'),
    path('collection/create_form/', create_collection_form, name='create_collection_form'),
    path('collection/<pk>/delete/', delete_collection, name='delete_collection'),
    path('mark/<pk>/', mark_note_view, name='mark_note'),
]