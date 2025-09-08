from django.core.management.base import BaseCommand
from hospitals.models import User
from donors.models import DonationRequests

class Command(BaseCommand):
    help = 'Create a test donor account'

    def handle(self, *args, **options):
        # Create donor
        if not User.objects.filter(username='testdonor').exists():
            donor = User()
            donor.username = 'testdonor'
            donor.set_password('donor123')
            donor.email = 'donor@test.com'
            donor.first_name = 'Test Donor'
            donor.city = 'New Delhi'
            donor.province = 'Delhi'
            donor.country = 'India'
            donor.contact_number = '9999999999'
            donor.is_staff = False
            donor.save()
            self.stdout.write('Created test donor: testdonor / donor123')
            
            # Create a test donation request
            donation = DonationRequests()
            donation.donation_request = 'Test donation request'
            donation.organ_type = 'Kidney'
            donation.blood_type = 'O+'
            donation.family_relation = 'Brother'
            donation.family_relation_name = 'Test Family'
            donation.family_contact_number = '9999999998'
            donation.donation_status = 'Approved'
            donation.donor = donor
            donation.family_consent = True
            donation.donated_before = False
            donation.save()
            self.stdout.write('Created test donation request')
        else:
            self.stdout.write('Test donor already exists')