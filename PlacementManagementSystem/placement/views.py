# from datetime import date
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from . forms import  LoginForm
# from .models import *
# # - Authentication models and functions
# from django.contrib.auth.models import auth ,User
# from django.core.files.storage import default_storage


# def homepage(request):
#     request.session['user'] = ''
#     return render(request, 'home.html')

# def placement_login(request):
#     error = ""

#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)

#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username=username, password=password)
#             try:
#                 if user is not None and user.is_staff==True:

#                     auth.login(request, user)
#                     error = "no"
#                 else:
#                     error = "yes"
#                     messages.error(request, "Invalid Username or Password")
#             except:
#                 error = "yes"
#     return render(request, 'pologin.html', locals())
    

# def student_login(request):
#     error = ""
#     if request.method == "POST":
#         student_id = request.POST.get('studentId')
#         password = request.POST.get('password')

#         user = Student.objects.filter(student_id=student_id,password=password).first()
#         if user is not None:
#             request.session['user']=student_id
#             error = "no"  # Redirect after successful login
#         else:
#             error = "yes"
#             messages.error(request, "Invalid student ID or Password")

#     return render(request, 'stlogin.html', locals())

# def student_signup(request):
#     error = ""
#     if request.method == "POST":
#         student_id = request.POST.get('student_id')
#         password = request.POST.get('password')
#         password2 = request.POST.get('confirm_password')
#         if password == password2:
#             result = Student(student_id=student_id,password=password)
#             result.save()
#             error = "no"
#             return render(request, 'stlogin.html')
#         else:
#             error = "yes"
        
#     return render(request, 'signup.html', locals())

# def student_forgot(request):
#     error = ""
#     if request.method == "POST":
#         stud_id = request.POST.get('student_id')
#         student_id = Student.objects.filter(student_id=stud_id).first()
#         if student_id is not None:
#             error = "no"
#             return render(request, 'stpassword.html', locals())
#         else:
#             error = "yes"
        
#     return render(request, 'stforgotpassword.html', locals())

# def student_password(request):
#     if request.method == "POST":
#         student_id = request.POST.get('student_id')
#         password = request.POST.get('password')
#         password2 = request.POST.get('confirm_password')
#         if password == password2:
#             result = Student.objects.get(student_id=student_id)
#             result.password=password
#             result.save()
#             return render(request, 'stlogin.html')
        
#     return render(request, 'signup.html', locals())

# def alumni_login(request):
#     error = ""
#     if request.method == "POST":
#         alumni_id = request.POST.get('alumniId')
#         password = request.POST.get('password')

#         user = Alumni.objects.filter(alumni_id=alumni_id,password=password).first()
#         # user = User.objects.get(password=password)
#         print(user)
#         if user is not None:
#             request.session['user']=alumni_id
#             error = "no"  # Redirect after successful login
#         else:
#             error = "yes"
#             messages.error(request, "Invalid Alumni ID or Password")

#     return render(request, 'allogin.html', locals())


# def alumni_signup(request):
#     error = ""
#     if request.method == "POST":
#         alumni_id = request.POST.get('alumniId')
#         password = request.POST.get('password')
#         password2 = request.POST.get('confirmPassword')
#         if password == password2:
#             result = Alumni(alumni_id=alumni_id,password=password)
#             result.save()
#             error = "no"
#             return render(request, 'allogin.html')
#         else:
#             error = "yes"
        
#     return render(request, 'alsign.html', locals())

# def alumni_dashboard(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     alumni = Alumni.objects.get(alumni_id=request.session['user'])  # Assuming username is student_id
#     companies = Company.objects.all()  # Fetch all company names 
    
#     if request.method == "POST":
#         alumni.name = request.POST.get("name")
#         alumni.company_id = Company.objects.get(company_id=request.POST.get("company"))
#         alumni.position = request.POST.get("position")
#         alumni.previous_status = request.POST.get("previous")
#         alumni.contact = request.POST.get("contact")
#         alumni.email = request.POST.get("email")
#         alumni.linkedin = request.POST.get("linkedin")
#         alumni.branch = request.POST.get("branch")
#         alumni.passout_year = request.POST.get("passout")
        
#         if request.FILES.get("profile"):
#             if alumni.profile_picture:
#                 default_storage.delete(alumni.profile_picture.path)
#             alumni.profile_picture = request.FILES["profile"]
        
#         alumni.save()
#         messages.success(request, "Profile updated successfully!")
#         return redirect("alumni_dashboard")
    
#     return render(request, "aldash.html", {"alumni": alumni, "companies": companies})

# def al_student_profile(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     students = Student.objects.all()  
#     return render(request, 'al_student_profile.html', {'students': students})


# def alapplied_students(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     # Get logged-in alumni's company
#     alumni = Alumni.objects.get(alumni_id=request.session['user'])  # Assuming alumni_id is stored in session

#     # Get placements posted by the alumni's company
#     placements = Placement.objects.filter(company_id=alumni.company_id)

#     # Get applications for those placements
#     applications = Application.objects.filter(placement_id__in=placements).select_related('placement_id', 'student_id')

#     return render(request, 'alapplied_students.html', {'applications': applications})

# @login_required(login_url="logout")
# def placement_dashboard(request):
#     companies = Company.objects.all()  # Fetch all company names
    
#     if request.method == "POST":
#         company = Company.objects.get(company_id=request.POST.get("company"))
#         email = request.POST.get("email")
#         contact_number = request.POST.get("contact_number")
#         position = request.POST.get("position")
#         skill = request.POST.get("skill")
#         date_of_drive = request.POST.get("date_of_drive")
#         backlogs = request.POST.get("backlogs")
#         cgpa = request.POST.get("cgpa")

#         Placement.objects.create(
#             company_id=company,
#             email=email,
#             contact_number=contact_number,
#             position=position,
#             skill=skill,
#             date_of_drive=date_of_drive,
#             backlogs=backlogs,
#             cgpa=cgpa
#         )
        
#         messages.success(request, "New Placement Added Successfully!")
#         return redirect("placement_dashboard")
#     return render(request, 'pdash.html', {"companies": companies})

# @login_required(login_url="logout")
# def addcompany(request):
#     if request.method == "POST":
#         company = request.POST.get('company')
#         result = Company(company_name=company)
#         result.save()
#         return render(request, 'pdash.html')
        
#     return render(request, 'addcompany.html')

# def student_dashboard(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     student = Student.objects.get(student_id=request.session['user'])  # Assuming username is student_id
    
#     if request.method == "POST":
#         student.name = request.POST.get("student_name")
#         student.Gender = request.POST.get("gender")
#         student.Birth_date = request.POST.get("dob")
#         student.contact = request.POST.get("contact")
#         student.email = request.POST.get("email")
#         student.branch = request.POST.get("branch")
#         student.sslc_per = request.POST.get("sslc")
#         student.passout_year_sslc = request.POST.get("sslc_year")
#         student.hsc_per = request.POST.get("hsc")
#         student.passout_year_hsc = request.POST.get("hsc_year")
#         student.skill = request.POST.get("skill")
        
#         if request.FILES.get("resume"):
#             if student.resume:
#                 default_storage.delete(student.resume.path)
#             student.resume = request.FILES["resume"]
        
#         if request.FILES.get("profile_pic"):
#             if student.profile_picture:
#                 default_storage.delete(student.profile_picture.path)
#             student.profile_picture = request.FILES["profile_pic"]
        
#         student.save()
#         messages.success(request, "Profile updated successfully!")
#         return redirect("student_dashboard")
    
#     return render(request, "stdash.html", {"student": student})

# def stplacement_details(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     current_date = date.today()
    
#     # Fetch all placement details
#     placements = Placement.objects.all()
    
#     # Fetch all applications made by the current student
#     applications = Application.objects.filter(student_id=request.session['user']).values_list('placement_id', flat=True)

#     return render(request, 'stplacement_details.html', {
#         'placements': placements,
#         'current_date': current_date,
#         'applied_placements': list(applications)  # Convert to a list
#     })

# def placement_apply(request,placement_id):
#     if request.session['user'] == '':
#         return redirect("logout")
#     current_year = date.today().year
#     student = request.session['user']
#     placement = Placement.objects.get(placement_id=placement_id)
#     #placement = placement_id
     
#     if request.method == "POST":
#         cgpa = request.POST.get("cgpa")
#         passout_year = request.POST.get("passout_year")
#         backlogs = request.POST.get("backlogs")
#         student = Student.objects.get(student_id=request.session['user'])

#         # Save application
#         application = Application(
#             placement_id=placement,
#             student_id=student,
#             cgpa=cgpa,
#             passout_year=passout_year,
#             backlogs=backlogs,
#             status="Applied"
#         )
#         application.save()
#         return redirect("stplacement_details")

#     return render(request, "placement_apply.html", {"placement": placement, "student": student,"current_year":current_year})


# def stapplication_details(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     # Fetch all applications made by the current student
#     applications = Application.objects.filter(student_id=request.session['user']).all()
#     # Get all placements related to the applications
#     placement_ids = applications.values_list('placement_id', flat=True)  # Extract placement IDs
#     placements = Placement.objects.filter(placement_id__in=placement_ids)

#     return render(request, 'stapplication_details.html', {
#         'placements': placements,
#         'applications': applications
#     })


# def st_alumni(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     alumnis = Alumni.objects.all() 
#     companies = Company.objects.all()  # Fetch all company names 
#     return render(request, 'st_alumni.html', {"alumnis": alumnis, "companies": companies})

# def stnotification(request):
#     if request.session['user'] == '':
#         return redirect("logout")
#     # Fetch all applications made by the current student
#     applications = Application.objects.filter(student_id=request.session['user'],status='Selected').all()
#     # Get all placements related to the applications
#     placement_ids = applications.values_list('placement_id', flat=True)  # Extract placement IDs
#     placements = Placement.objects.filter(placement_id__in=placement_ids)

#     return render(request, 'stnotification.html', {
#         'placements': placements,
#         'applications': applications
#     })


# @login_required(login_url="logout")
# def pl_placement_details(request):
#     placements = Placement.objects.all()  # Fetch all placement records
#     return render(request, 'pl_placement_details.html', {"placements": placements})

# @login_required(login_url="logout")
# def pl_student_profile(request):
#     students = Student.objects.all()  
#     return render(request, 'plstudent_profile.html', {'students': students})

# @login_required(login_url="logout")
# def pl_edit_student(request,student_id):
#     student = Student.objects.get(student_id=student_id)  # Assuming username is student_id
    
#     if request.method == "POST":
#         student.name = request.POST.get("student_name")
#         student.Gender = request.POST.get("gender")
#         student.Birth_date = request.POST.get("dob")
#         student.contact = request.POST.get("contact")
#         student.email = request.POST.get("email")
#         student.branch = request.POST.get("branch")
#         student.sslc_per = request.POST.get("sslc")
#         student.passout_year_sslc = request.POST.get("sslc_year")
#         student.hsc_per = request.POST.get("hsc")
#         student.passout_year_hsc = request.POST.get("hsc_year")
#         student.skill = request.POST.get("skill")
        
#         if request.FILES.get("resume"):
#             if student.resume:
#                 default_storage.delete(student.resume.path)
#             student.resume = request.FILES["resume"]
        
#         if request.FILES.get("profile_pic"):
#             if student.profile_picture:
#                 default_storage.delete(student.profile_picture.path)
#             student.profile_picture = request.FILES["profile_pic"]
        
#         student.save()
#         messages.success(request, "Profile updated successfully!")
#         return redirect("pl_student_profile")
    
#     return render(request, "pl_student_edit.html", {"student": student})

# @login_required(login_url="logout")
# def pl_applied_students(request):
#     applications = Application.objects.all()
#     return render(request, 'plapplied_students.html', {'applications': applications})

# @login_required(login_url="logout")
# def update_application_status(request, application_id, status):
#     application = get_object_or_404(Application, pk=application_id)
#     application.status = status
#     application.save()
#     return redirect('pl_applied_students')  # Redirect back to the applied students page


# @login_required(login_url="logout")
# def pl_alumni(request):
#     alumnis = Alumni.objects.all() 
#     companies = Company.objects.all()  # Fetch all company names 
#     return render(request, 'plalumni.html', {"alumnis": alumnis, "companies": companies})

# @login_required(login_url="logout")
# def pl_edit_alumni(request,alumni_id):
#     alumni = Alumni.objects.get(alumni_id=alumni_id)  # Assuming username is student_id
#     companies = Company.objects.all()  # Fetch all company names 
    
#     if request.method == "POST":
#         alumni.name = request.POST.get("name")
#         alumni.company_id = Company.objects.get(company_id=request.POST.get("company"))
#         alumni.position = request.POST.get("position")
#         alumni.previous_status = request.POST.get("previous")
#         alumni.contact = request.POST.get("contact")
#         alumni.email = request.POST.get("email")
#         alumni.linkedin = request.POST.get("linkedin")
#         alumni.branch = request.POST.get("branch")
#         alumni.passout_year = request.POST.get("passout")
        
#         if request.FILES.get("profile"):
#             if alumni.profile_picture:
#                 default_storage.delete(alumni.profile_picture.path)
#             alumni.profile_picture = request.FILES["profile"]
        
#         alumni.save()
#         messages.success(request, "Profile updated successfully!")
#         return redirect("pl_alumni")
    
#     return render(request, "pl_edit_alumni.html", {"alumni": alumni, "companies": companies})

# def user_logout(request):
#     request.session['user']=''
#     logout(request)
#     return redirect('homepage')  # Redirect to home after logout





from datetime import date
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from .forms import LoginForm
from .models import Student, Alumni, Placement, Application, Company

# Authentication models and functions
from django.contrib.auth.models import User


def homepage(request):
    request.session['user'] = ''
    return render(request, 'home.html')


def placement_login(request):
    error = ""
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('placement_dashboard')  # Redirect to the dashboard
            else:
                error = "yes"
                messages.error(request, "Invalid Username or Password")

    return render(request, 'pologin.html', {'form': form, 'error': error})


def student_login(request):
    error = ""

    if request.method == "POST":
        student_id = request.POST.get('studentId')
        password = request.POST.get('password')

        user = Student.objects.filter(student_id=student_id, password=password).first()
        if user:
            request.session['user'] = student_id
            return redirect("student_dashboard")  # Redirect after successful login
        else:
            error = "yes"
            messages.error(request, "Invalid Student ID or Password")

    return render(request, 'stlogin.html', {'error': error})


def student_signup(request):
    error = ""

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password == password2:
            Student.objects.create(student_id=student_id, password=password)
            return redirect('stlogin')
        else:
            error = "yes"

    return render(request, 'signup.html', {'error': error})


def student_forgot(request):
    error = ""

    if request.method == "POST":
        stud_id = request.POST.get('student_id')
        student = Student.objects.filter(student_id=stud_id).first()

        if student:
            return redirect("student_password")
        else:
            error = "yes"

    return render(request, 'stforgotpassword.html', {'error': error})


def student_password(request):
    error = ""

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        # Check if passwords match
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'stforgotpassword.html', {'error': "yes"})

        # Check if student exists
        student = Student.objects.filter(student_id=student_id).first()
        if student is None:
            messages.error(request, "Invalid Student ID!")
            return render(request, 'stforgotpassword.html', {'error': "yes"})

        # Update password
        student.password = password
        student.save()

        messages.success(request, "Password updated successfully! Please login.")
        return redirect('stlogin')

    return render(request, 'signup.html', {'error': error})

def alumni_login(request):
    error = ""

    if request.method == "POST":
        alumni_id = request.POST.get('alumniId')
        password = request.POST.get('password')

        user = Alumni.objects.filter(alumni_id=alumni_id, password=password).first()
        if user:
            request.session['user'] = alumni_id
            return redirect("alumni_dashboard")  # Redirect after successful login
        else:
            error = "yes"
            messages.error(request, "Invalid Alumni ID or Password")

    return render(request, 'allogin.html', {'error': error})


def alumni_signup(request):
    error = ""

    if request.method == "POST":
        alumni_id = request.POST.get('alumniId')
        password = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')

        if password == password2:
            Alumni.objects.create(alumni_id=alumni_id, password=password)
            return redirect('allogin')
        else:
            error = "yes"

    return render(request, 'alsign.html', {'error': error})


@login_required(login_url="logout")
def placement_dashboard(request):
    companies = Company.objects.all()

    if request.method == "POST":
        company = get_object_or_404(Company, company_id=request.POST.get("company"))
        Placement.objects.create(
            company_id=company,
            email=request.POST.get("email"),
            contact_number=request.POST.get("contact_number"),
            position=request.POST.get("position"),
            skill=request.POST.get("skill"),
            date_of_drive=request.POST.get("date_of_drive"),
            backlogs=request.POST.get("backlogs"),
            cgpa=request.POST.get("cgpa"),
        )
        messages.success(request, "New Placement Added Successfully!")
        return redirect("placement_dashboard")

    return render(request, 'pdash.html', {"companies": companies})


@login_required(login_url="logout")
def addcompany(request):
    if request.method == "POST":
        Company.objects.create(company_name=request.POST.get('company'))
        return redirect('placement_dashboard')

    return render(request, 'addcompany.html')


@login_required(login_url="logout")
def update_application_status(request, application_id, status):
    application = get_object_or_404(Application, pk=application_id)
    application.status = status
    application.save()
    return redirect('pl_applied_students')  # Redirect back to the applied students page


def student_dashboard(request):
    if 'user' not in request.session or request.session['user'] == '':
        return redirect("logout")

    student = get_object_or_404(Student, student_id=request.session['user'])

    if request.method == "POST":
        student.name = request.POST.get("student_name")
        student.Gender = request.POST.get("gender")
        student.Birth_date = request.POST.get("dob")
        student.contact = request.POST.get("contact")
        student.email = request.POST.get("email")
        student.branch = request.POST.get("branch")
        student.sslc_per = request.POST.get("sslc")
        student.passout_year_sslc = request.POST.get("sslc_year")
        student.hsc_per = request.POST.get("hsc")
        student.passout_year_hsc = request.POST.get("hsc_year")
        student.skill = request.POST.get("skill")

        if request.FILES.get("resume"):
            if student.resume:
                default_storage.delete(student.resume.path)
            student.resume = request.FILES["resume"]

        if request.FILES.get("profile_pic"):
            if student.profile_picture:
                default_storage.delete(student.profile_picture.path)
            student.profile_picture = request.FILES["profile_pic"]

        student.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("student_dashboard")

    return render(request, "stdash.html", {"student": student})


def user_logout(request):
    request.session.flush()
    logout(request)
    return redirect('homepage')  # Redirect to home after logout
