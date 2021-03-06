from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import ArtifactDetail
import os
from django.conf import settings
from django.http import HttpResponse
from details.forms import FeedbackForm

#if a new artifact is added to an already present room... we haven't considered that.....yet

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'numbers.txt')
f = open(file_path,'r')
no_of_rooms = f.read()
f.close()

room_template = """
{% load static %}
<html>
    <head>
    <title>Artifact List {{artif}}</title>

      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <link rel="stylesheet" href="{% static 'css/details.css' %}">
      <link href="https://fonts.googleapis.com/css?family=Patrick+Hand" rel="stylesheet">

<style>
/* Style the navbar */
#navbar {
overflow: hidden;
background-color: #333;
}

/* Navbar links */
#navbar a {
float: left;
display: block;
color: #f2f2f2;
text-align: center;
padding: 14px;
text-decoration: none;
}

/* Page content */
.content {
padding: 16px;
}

/* The sticky class is added to the navbar with JS when it reaches its scroll position */
.sticky {
position: fixed;
top: 0;
width: 100%;
}

/* Add some top padding to the page content to prevent sudden quick movement (as the navigation bar gets a new position at the top of the page (position:fixed and top:0) */
.sticky + .content {
padding-top: 60px;
}
/* Add a black background color to the top navigation bar */
.navbar {
overflow: hidden;
background-color: #e9e9e9;
}

/* Style the links inside the navigation bar */
.navbar a {
float: left;
display: block;
color: black;
text-align: center;
padding: 14px 16px;
text-decoration: none;
font-size: 17px;
}

/* Change the color of links on hover */
.navbar a:hover {
background-color: #ddd;
color: black;
}

/* Style the "active" element to highlight the current page */
.navbar a.active {
background-color: #2196F3;
color: white;
}

/* Style the search box inside the navigation bar */
.navbar input[type=text] {
float: right;
padding: 6px;
border: none;
margin-top: 8px;
margin-right: 16px;
font-size: 17px;
}

/* When the screen is less than 600px wide, stack the links and the search field vertically instead of horizontally */
@media screen and (max-width: 600px) {
.navbar a, .navbar input[type=text] {
float: none;
display: block;
text-align: left;
width: 100%;
margin: 0;
padding: 14px;
}
.navbar input[type=text] {
border: 1px solid #ccc;
}
}
.collapsible {
    background-color: #777;
    color: white;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
    font-size: 15px;
}

.active, .collapsible:hover {
    background-color: #555;
}

.collapse,#id {
    padding: 0 18px;
    display: none;
    overflow: hidden;
    background-color: #f1f1f1;
}
</style>
</head>
<body>
  <div id="navbar">
<a class="active" href="/">Home</a>
<a href="/feedback">Contact</a>
</div>
        <div class="page-header">
            <h1><a href="/">Artifact List</a></h1>
        </div>



{% for artifact in artifacts %}
    <div class = "artifact">
      <br>
      <br>
      <br>
        <div class="container">
        <h1><p>{{ artifact.artifact_name }}</p></h1>
        <button class="collapsible">Artifact Information</button>
        <div id="demo" class="collapse">
        <p>Room number : {{ artifact.room_no }} , Artifact number: {{ artifact.artifact_no}} </p>
        {{ artifact.artifact_description|linebreaksbr }}
        </div></div>
    <br>
  <br>
{% endfor %}
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
</script>

</body>
</html>
"""


def artifact_list(request):
    artifacts = ArtifactDetail.objects.filter(artifact_no__contains="1").order_by('room_no')
    return render(request, 'details/artifact_list.html', {'artifacts':artifacts})




def room(request,i):
    artifacts = ArtifactDetail.objects.filter(room_no__contains=str(i))
    fila=open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates/details/'+"room_number"+str(i)+".html"),'w+')
    fila.write(room_template)
    fila.close()
    return render(request,'details/room_number'+str(i)+'.html',{'artifacts':artifacts})


def success(request):
    return render(request,'details/success.html')

def aravind(request):
    return render(request,'details/aravind.html')


from details.forms import FeedbackForm

def feedback(request):
    form_class = FeedbackForm
    return render(request,'details/feedbackform.html',{'form':form_class})
