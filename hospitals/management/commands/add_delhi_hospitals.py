from django.core.management.base import BaseCommand
from hospitals.models import User

class Command(BaseCommand):
    help = 'Add sample hospitals from Delhi, India'

    def handle(self, *args, **options):
        hospitals = [
            {
                'username': 'aiims_delhi',
                'hospital_name': 'All India Institute of Medical Sciences',
                'email': 'admin@aiims.edu',
                'city': 'New Delhi',
                'province': 'Delhi',
                'country': 'India',
                'contact_number': '1126588500'
            },
            {
                'username': 'safdarjung_hospital',
                'hospital_name': 'Safdarjung Hospital',
                'email': 'admin@safdarjung.gov.in',
                'city': 'New Delhi',
                'province': 'Delhi',
                'country': 'India',
                'contact_number': '1126165060'
            },
            {
                'username': 'ram_manohar_lohia',
                'hospital_name': 'Ram Manohar Lohia Hospital',
                'email': 'admin@rmlh.nic.in',
                'city': 'New Delhi',
                'province': 'Delhi',
                'country': 'India',
                'contact_number': '1123404040'
            },
            {
                'username': 'fortis_escorts',
                'hospital_name': 'Fortis Escorts Heart Institute',
                'email': 'admin@fortisescorts.in',
                'city': 'New Delhi',
                'province': 'Delhi',
                'country': 'India',
                'contact_number': '1147135000'
            },
            {
                'username': 'max_saket',
                'hospital_name': 'Max Super Speciality Hospital Saket',
                'email': 'admin@maxhealthcare.com',
                'city': 'New Delhi',
                'province': 'Delhi',
                'country': 'India',
                'contact_number': '1126515050'
            }
        ]

        for hospital_data in hospitals:
            if not User.objects.filter(username=hospital_data['username']).exists():
                user = User()
                user.username = hospital_data['username']
                user.set_password('hospital123')
                user.email = hospital_data['email']
                user.first_name = hospital_data['hospital_name']
                user.hospital_name = hospital_data['hospital_name']
                user.city = hospital_data['city']
                user.province = hospital_data['province']
                user.country = hospital_data['country']
                user.contact_number = hospital_data['contact_number']
                user.is_staff = True
                user.save()
                self.stdout.write(f"Added hospital: {hospital_data['hospital_name']}")
            else:
                self.stdout.write(f"Hospital already exists: {hospital_data['hospital_name']}")

        self.stdout.write(self.style.SUCCESS('Successfully added Delhi hospitals'))