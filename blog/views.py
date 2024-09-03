from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, About, Contact, Announcement
from .forms import PostForm, AboutForm, ContactForm, AnnouncementForm, CommentForm

# Helper function to check if the user is staff
def staff_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('not_required')  # Redirect to the custom page
    return _wrapped_view

def not_required(request):
    return render(request, 'blog/not_required.html')

# Home view
def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required
@staff_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
@staff_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
@staff_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

# About Views
def about_detail(request):
    about = About.objects.first()  # Retrieve the first About object if it exists
    return render(request, 'blog/about_detail.html', {'about': about})

@login_required
@staff_required
def about_edit(request):
    about = About.objects.first()  # Retrieve the first About object if it exists
    if about is None:
        about = About()  # Create a new About object if none exists
    if request.method == "POST":
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about_detail')
    else:
        form = AboutForm(instance=about)
    return render(request, 'blog/page_form.html', {'form': form, 'page': 'Edit About Us'})

@login_required
@staff_required
def about_delete(request):
    about = About.objects.first()  # Retrieve the first About object if it exists
    if about and request.method == "POST":
        about.delete()
        return redirect('home')
    return render(request, 'blog/page_confirm_delete.html', {'page': 'About Us'})

# Contact Views
def contact_detail(request):
    contact = Contact.objects.first()  # Retrieve the first Contact object if it exists
    return render(request, 'blog/contact_detail.html', {'contact': contact})

@login_required
@staff_required
def contact_edit(request):
    contact = Contact.objects.first()  # Retrieve the first Contact object if it exists
    if contact is None:
        contact = Contact()  # Create a new Contact object if none exists
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'blog/page_form.html', {'form': form, 'page': 'Edit Contact Us'})

@login_required
@staff_required
def contact_delete(request):
    contact = Contact.objects.first()  # Retrieve the first Contact object if it exists
    if contact and request.method == "POST":
        contact.delete()
        return redirect('home')
    return render(request, 'blog/page_confirm_delete.html', {'page': 'Contact Us'})

# Announcement Views
def announcement_list(request):
    announcements = Announcement.objects.order_by('-published_date')
    return render(request, 'blog/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'blog/announcement_detail.html', {'announcement': announcement})

@login_required
@staff_required
def announcement_create(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm()
    return render(request, 'blog/page_form.html', {'form': form, 'page': 'Create Announcement'})

@login_required
@staff_required
def announcement_edit(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == "POST":
        form = AnnouncementForm(request.POST, request.FILES, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'blog/page_form.html', {'form': form, 'page': 'Edit Announcement'})

@login_required
@staff_required
def announcement_delete(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == "POST":
        announcement.delete()
        return redirect('announcement_list')
    return render(request, 'blog/page_confirm_delete.html', {'announcement': announcement})
