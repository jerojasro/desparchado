from django.views.generic import DetailView

from django.contrib.auth import get_user_model

from events.models import Event

User = get_user_model()


class UserDetailView(DetailView):
    context_object_name = 'user_object'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmarked_events'] = Event.objects.filter(
            is_published=True,
            is_approved=True,
            user_relation__user=self.get_object(),
            user_relation__is_bookmarked=True,
        ).distinct().all()
        context['visited_events'] = Event.objects.filter(
            is_published=True,
            is_approved=True,
            user_relation__user=self.get_object(),
            user_relation__is_visited=True,
        ).distinct().all()
        return context
