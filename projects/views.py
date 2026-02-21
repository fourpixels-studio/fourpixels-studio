from .forms import ProjectForm
from django.contrib import messages
from blogs.utils import update_views
from .models import Project, Category
from website.forms import TestimonialForm
from django.db.models import Count, Q, Prefetch
from website.get_items import get_recent_projects
from django.shortcuts import render, get_object_or_404, redirect


def projects_list(request):
    categories = (
        Category.objects
        .annotate(
            visible_projects=Count(
                "projects",
                filter=Q(projects__show_in_portfolio=True)
            )
        )
        .filter(visible_projects__gt=0)
        .prefetch_related(
            Prefetch(
                "projects",
                queryset=Project.objects.filter(show_in_portfolio=True)
            )
        )
        .order_by("-pk")
    )
    
    context = {
        'title_tag': "Projects",
        'categories': categories,
        'all_projects': Project.objects.filter(show_in_portfolio=True).order_by("-pk"),
        'meta_description': "Explore our portfolio of innovative websites and web applications. Discover how we help freelancers, creative professionals, and small businesses elevate their online presence with custom designs, user-centric development, and ongoing support.",
    }
    return render(request, 'projects_list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
        'title_tag': project.name,
        'meta_keywords': project.category,
        'projects': get_recent_projects(),
        'meta_thumbnail': project.logo.url,
        'testimonial_form': TestimonialForm(),
        'meta_description': project.description,
    }
    update_views(request, project)
    return render(request, 'project_detail.html', context)


def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f"Succesfully updated '{project.name}'")
            return redirect("project_detail", slug=project.slug)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = ProjectForm(instance=project)

    context = {
        "form": form,
        "project": project,
        'title_tag': f"Updating {project.name} Project",
    }
    return render(request, "update_project.html", context)
