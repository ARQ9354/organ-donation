from django.shortcuts import render
import pdfkit
from django.conf import settings
from django.db.models import Q
from donors.models import DonationRequests, Appointments
import json
from django.http import JsonResponse, HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import string
import secrets
import ast
import random
from donors.models import DonationRequests, Appointments
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import StringIO, BytesIO
from xhtml2pdf import pisa
from PyPDF2 import PdfFileMerger, PdfFileReader


# Create your views here.


def home(request):
    if request.POST:
        pass
    return render(request, "hospital-main-page.html")


def search_donations(request):
    if request.POST:
        pass
    else:
        search_keyword = request.GET.get('keyword', '')
        status = "Approved"
        # Search for donations based on organ type/blood type/donor name
        donations = DonationRequests.objects.filter((Q(organ_type__iexact=search_keyword) | Q(blood_type__startswith=search_keyword) | Q(donor__first_name__iexact=search_keyword) | Q(donor__last_name__iexact=search_keyword)) & Q(donation_status__iexact=status))
        print(donations)
        # Search for donations based on donation id
        if not donations:
            if search_keyword.isdigit():
                donations = DonationRequests.objects.filter(Q(id=int(search_keyword)) & Q(donation_status__iexact=status))

        donation_list = []
        for donation in donations:
            print(donation.donation_status)
            temp_dict = {}
            temp_dict["donor"] = f"{donation.donor.first_name} {donation.donor.last_name}"
            temp_dict["organ"] = donation.organ_type
            temp_dict["donation_id"] = donation.id
            temp_dict["blood_group"] = donation.blood_type
            donation_list.append(temp_dict)
        search_list = json.dumps(donation_list)
        print("hi", search_list)
        return HttpResponse(search_list)


def search_donation_details(request):
    if request.POST:
        pass
    else:
        # Fetching donation details
        donation_id_from_UI = request.GET.get('donation_id', '')
        donations = Appointments.objects.filter(Q(donation_request__id=int(donation_id_from_UI)))
        donation_list = []
        for donation in donations:
            temp_dict = {}
            # Donor details
            temp_dict["user_name"] = donation.donation_request.donor.username
            temp_dict["first_name"] = donation.donation_request.donor.first_name
            temp_dict["last_name"] = donation.donation_request.donor.last_name
            temp_dict["email"] = donation.donation_request.donor.email
            temp_dict["contact_number"] = donation.donation_request.donor.contact_number
            temp_dict["city"] = donation.donation_request.donor.city
            temp_dict["country"] = donation.donation_request.donor.country
            temp_dict["province"] = donation.donation_request.donor.province
            # Donation details
            temp_dict["organ"] = donation.donation_request.organ_type
            temp_dict["donation_id"] = donation.donation_request.id
            temp_dict["blood_group"] = donation.donation_request.blood_type
            temp_dict["donation_status"] = donation.donation_request.donation_status
            temp_dict["approved_by"] = donation.hospital.hospital_name
            temp_dict["family_member_name"] = donation.donation_request.family_relation_name
            temp_dict["family_member_relation"] = donation.donation_request.family_relation
            temp_dict["family_member_contact"] = donation.donation_request.family_contact_number
            donation_list.append(temp_dict)
        donation_details = json.dumps(donation_list)

        return HttpResponse(donation_details)


def fetch_appointments(request):
    if request.POST:
        pass
    else:
        appointments = Appointments.objects.filter(hospital__id=request.user.id, appointment_status="Pending")
        
        appointment_list = []
        for appointment in appointments:
            temp_dict = {
                "id": appointment.id,
                "donor_name": f"{appointment.donation_request.donor.first_name} {appointment.donation_request.donor.last_name}",
                "organ_type": appointment.donation_request.organ_type,
                "date": appointment.date,
                "time": appointment.time,
                "status": appointment.appointment_status
            }
            appointment_list.append(temp_dict)
        
        return JsonResponse({"appointments": appointment_list})


def fetch_donations(request):
    if request.POST:
        pass
    else:
        # Debug: Check all donations first
        all_donations = DonationRequests.objects.all()
        print(f"Total donations in database: {all_donations.count()}")
        for d in all_donations:
            print(f"Donation ID: {d.id}, Status: {d.donation_status}, Donor: {d.donor.first_name}")
        
        # Get all pending donation requests
        donations = DonationRequests.objects.filter(donation_status="Pending")
        print(f"Pending donations found: {donations.count()}")
        
        donation_list = []
        for donation in donations:
            temp_dict = {
                "id": donation.id,
                "donor_name": f"{donation.donor.first_name} {donation.donor.last_name}",
                "organ_type": donation.organ_type,
                "blood_type": donation.blood_type,
                "request_date": donation.request_datetime.strftime("%Y-%m-%d"),
                "status": donation.donation_status
            }
            donation_list.append(temp_dict)
        
        return JsonResponse({"donations": donation_list})


def hospital_register(request):

    # If method is post
    if request.POST:
        user = User()
        user.username = request.POST.get("username", "")
        user.set_password(request.POST.get("password", ""))
        user.email = request.POST.get("email", "")
        user.first_name = request.POST.get("hospital_name", "")
        user.hospital_name = request.POST.get("hospital_name", "")
        user.city = request.POST.get("city", "")
        user.province = request.POST.get("province", "")
        user.country = request.POST.get("country", "")
        user.contact_number = request.POST.get("contact_number", "")
        user.is_staff = True
        user.save()
        return redirect('hospital-login')

    return render(request, "hospital-registration.html")

def hospital_login(request):
    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.is_staff:

                 #                msg = """Logged in successfully. The homepage is with the other developer who is working on it. But,
                                        # the remaining functionality works the exact same way it does on donor side. Hence, you
                                        # are being redirected to same login page."""
                    login(request, user)
                    return redirect(request.POST.get("next", "home"))
        else:
            msg = "Invalid password"
            success = 1
            return render(request, "hospital-login.html", {"success": success, "msg": msg})

    return render(request, "hospital-login.html")


def fetch_appointment_details(request):
    if request.POST:
        pass
    else:
        appointment_id = request.GET.get('id', '')
        try:
            appointment = Appointments.objects.get(id=int(appointment_id))
            details = {
                "Donor Name": f"{appointment.donation_request.donor.first_name} {appointment.donation_request.donor.last_name}",
                "Email": appointment.donation_request.donor.email,
                "Contact": appointment.donation_request.donor.contact_number,
                "City": appointment.donation_request.donor.city,
                "Province": appointment.donation_request.donor.province,
                "Organ Type": appointment.donation_request.organ_type,
                "Blood Group": appointment.donation_request.blood_type,
                "Appointment Date": appointment.date,
                "Appointment Time": appointment.time,
                "Status": appointment.appointment_status,
                "Family Contact": appointment.donation_request.family_relation_name
            }
            return JsonResponse(details)
        except Appointments.DoesNotExist:
            return JsonResponse({"error": "Appointment not found"})


def fetch_donation_details(request):
    if request.POST:
        pass
    else:
        donation_id = request.GET.get('id', '')
        try:
            donation = DonationRequests.objects.get(id=int(donation_id))
            details = {
                "Donor Name": f"{donation.donor.first_name} {donation.donor.last_name}",
                "Email": donation.donor.email,
                "Contact": donation.donor.contact_number,
                "City": donation.donor.city,
                "Province": donation.donor.province,
                "Organ Type": donation.organ_type,
                "Blood Group": donation.blood_type,
                "Request Date": donation.request_datetime.strftime("%Y-%m-%d"),
                "Status": donation.donation_status,
                "Family Contact": donation.family_relation_name,
                "Family Relation": donation.family_relation
            }
            return JsonResponse(details)
        except DonationRequests.DoesNotExist:
            return JsonResponse({"error": "Donation not found"})


@csrf_exempt
def approve_appointments(request):
    if request.POST:
        appointment_id = request.POST.get('id', '')
        action = request.POST.get('action', '')
        
        try:
            appointment = get_object_or_404(Appointments, id=appointment_id)
            if action == 'approve':
                appointment.appointment_status = 'Approved'
            elif action == 'deny':
                appointment.appointment_status = 'Denied'
            appointment.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False})


@csrf_exempt
def approve_donations(request):
    if request.POST:
        donation_id = request.POST.get('id', '')
        action = request.POST.get('action', '')
        
        try:
            donation = get_object_or_404(DonationRequests, id=donation_id)
            if action == 'approve':
                donation.donation_status = 'Approved'
            elif action == 'deny':
                donation.donation_status = 'Denied'
            donation.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False})


def fetch_counts(request):
    if request.POST:
        pass
    else:
        appointment_count = Appointments.objects.filter(hospital__id=request.user.id, appointment_status="Pending").count()
        donation_count = DonationRequests.objects.filter(donation_status="Pending").count()
        
        print(f"fetch_counts - Appointments: {appointment_count}, Donations: {donation_count}")
        
        result = {
            "appointments": appointment_count,
            "donations": donation_count
        }
        return JsonResponse(result)


def send_mail(send_from, send_to, subject, body_of_msg, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    message = MIMEMultipart()
    message['From'] = send_from
    message['To'] = send_to
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = subject
    message.attach(MIMEText(body_of_msg))
    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, message.as_string())
    smtp.quit()


def hospital_forgot_password(request):
    success = 0
    if request.POST:
        username = request.POST.get("username", "")
        try:
            user = User.objects.get(username=username)
            email = user.email
            password = random.randint(1000000, 999999999999)
            user.set_password(password)
            user.save()
            send_mail("foodatdalteam@gmail.com", email, "Password reset for your organ donation account",
                      """Your request to change password has been processed.\nThis is your new password: {}\n
                            If you wish to change password, please go to your user profile and change it.""".format(password),
                      server="smtp.gmail.com", username="foodatdalteam@gmail.com", password="foodatdal")
            success = 1
            msg = "Success. Check your registered email for new password!"
            return render(request, "hospital-forgot-password.html", {"success": success, "msg": msg})
        except:
            success = 1
            msg = "User does not exist!"
            return render(request, "hospital-forgot-password.html", {"success": success, "msg": msg})

    return render(request, "hospital-forgot-password.html", {"success": success})


def form_to_PDF(request, donor_id=1):

    donation_request = DonationRequests.objects.get(id=donor_id)
    user = donation_request.donor
    donations = DonationRequests.objects.filter(donor=user)
    template = get_template("user-details.html")
    html = template.render({'user': user, 'donors': donations})
    config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF)
    try:
        pdf = pdfkit.from_string(html, False, configuration=config)
    except Exception as e:
        print(e)
        pass
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    userpdf = PdfFileReader(BytesIO(pdf))
    usermedicaldoc = donation_request.upload_medical_doc.read()
    usermedbytes = BytesIO(usermedicaldoc)
    usermedicalpdf = PdfFileReader(usermedbytes)
    merger = PdfFileMerger()
    merger.append(userpdf)
    merger.append(usermedicalpdf)
    merger.write(response)
    return response


def email_donor(request, donor_id=1):
    donor = DonationRequests.objects.get(id=donor_id).donor
    send_mail("foodatdalteam@gmail.com", donor.email, "Organ Donation",
              """You've been requested by {} to donate organ. Thanks!""".format(request.user.hospital_name),
              server="smtp.gmail.com", username="foodatdalteam@gmail.com", password="foodatdal")
    return HttpResponse("Success")


def get_user_details(request):
    if request.POST:
        pass
    else:
        hospital = User.objects.get(id=request.user.id)
        user_details = [{
            "hospital_name": hospital.hospital_name or hospital.first_name,
            "hospital_email": hospital.email,
            "hospital_city": hospital.city,
            "hospital_province": hospital.province,
            "hospital_contact": hospital.contact_number
        }]
        return JsonResponse(user_details, safe=False)


@csrf_exempt
def update_user_details(request):
    if request.POST:
        try:
            user = User.objects.get(id=request.user.id)
            user.hospital_name = request.POST.get('name', '')
            user.first_name = request.POST.get('name', '')
            user.email = request.POST.get('email', '')
            user.city = request.POST.get('city', '')
            user.province = request.POST.get('province', '')
            user.contact_number = request.POST.get('contact', '')
            user.save()
            return HttpResponse("success")
        except Exception as e:
            return HttpResponse("error")
    return HttpResponse("error")


@csrf_exempt
def update_pwd_details(request):
    if request.POST:
        user = authenticate(username=request.user.username, password=request.POST.get("old_password", ""))
        if user is not None:
            user.set_password(request.POST.get("new_password", ""))
            user.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    return HttpResponse("error")

def hospital_logout(request):
    logout(request)
    return redirect("hospital-login")
