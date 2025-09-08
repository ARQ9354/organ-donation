from django.core.management.base import BaseCommand
from hospitals.models import User

class Command(BaseCommand):
    help = 'Add 100+ hospitals from Delhi and NCR, India'

    def handle(self, *args, **options):
        hospitals = [
            # Government Hospitals Delhi
            {'username': 'aiims_delhi', 'hospital_name': 'All India Institute of Medical Sciences', 'city': 'New Delhi', 'contact': '1126588500'},
            {'username': 'safdarjung_hospital', 'hospital_name': 'Safdarjung Hospital', 'city': 'New Delhi', 'contact': '1126165060'},
            {'username': 'ram_manohar_lohia', 'hospital_name': 'Ram Manohar Lohia Hospital', 'city': 'New Delhi', 'contact': '1123404040'},
            {'username': 'lady_hardinge', 'hospital_name': 'Lady Hardinge Medical College', 'city': 'New Delhi', 'contact': '1123408820'},
            {'username': 'maulana_azad', 'hospital_name': 'Maulana Azad Medical College', 'city': 'New Delhi', 'contact': '1123239271'},
            {'username': 'lnjp_hospital', 'hospital_name': 'Lok Nayak Jai Prakash Hospital', 'city': 'New Delhi', 'contact': '1123357301'},
            {'username': 'gb_pant', 'hospital_name': 'Govind Ballabh Pant Hospital', 'city': 'New Delhi', 'contact': '1123234242'},
            {'username': 'deen_dayal', 'hospital_name': 'Deen Dayal Upadhyay Hospital', 'city': 'New Delhi', 'contact': '1125881000'},
            {'username': 'guru_teg_bahadur', 'hospital_name': 'Guru Teg Bahadur Hospital', 'city': 'New Delhi', 'contact': '1122590404'},
            {'username': 'rajiv_gandhi', 'hospital_name': 'Rajiv Gandhi Super Speciality Hospital', 'city': 'New Delhi', 'contact': '1122059090'},
            
            # Private Hospitals Delhi
            {'username': 'fortis_escorts', 'hospital_name': 'Fortis Escorts Heart Institute', 'city': 'New Delhi', 'contact': '1147135000'},
            {'username': 'max_saket', 'hospital_name': 'Max Super Speciality Hospital Saket', 'city': 'New Delhi', 'contact': '1126515050'},
            {'username': 'apollo_delhi', 'hospital_name': 'Apollo Hospital Delhi', 'city': 'New Delhi', 'contact': '1126925858'},
            {'username': 'medanta_gurgaon', 'hospital_name': 'Medanta The Medicity', 'city': 'Gurgaon', 'contact': '1244141414'},
            {'username': 'artemis_gurgaon', 'hospital_name': 'Artemis Hospital', 'city': 'Gurgaon', 'contact': '1244511111'},
            {'username': 'fortis_gurgaon', 'hospital_name': 'Fortis Memorial Research Institute', 'city': 'Gurgaon', 'contact': '1244962200'},
            {'username': 'max_gurgaon', 'hospital_name': 'Max Hospital Gurgaon', 'city': 'Gurgaon', 'contact': '1244200000'},
            {'username': 'columbia_asia', 'hospital_name': 'Columbia Asia Hospital', 'city': 'Gurgaon', 'contact': '1244251000'},
            {'username': 'paras_gurgaon', 'hospital_name': 'Paras Hospital', 'city': 'Gurgaon', 'contact': '1244166666'},
            {'username': 'manipal_delhi', 'hospital_name': 'Manipal Hospital Delhi', 'city': 'New Delhi', 'contact': '1145440000'},
            
            # More Delhi Hospitals
            {'username': 'batra_hospital', 'hospital_name': 'Batra Hospital & Medical Research Centre', 'city': 'New Delhi', 'contact': '1129958888'},
            {'username': 'sir_ganga_ram', 'hospital_name': 'Sir Ganga Ram Hospital', 'city': 'New Delhi', 'contact': '1142251000'},
            {'username': 'indraprastha_apollo', 'hospital_name': 'Indraprastha Apollo Hospital', 'city': 'New Delhi', 'contact': '1126925858'},
            {'username': 'max_patparganj', 'hospital_name': 'Max Super Speciality Hospital Patparganj', 'city': 'New Delhi', 'contact': '1142335000'},
            {'username': 'fortis_shalimar_bagh', 'hospital_name': 'Fortis Hospital Shalimar Bagh', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'psri_hospital', 'hospital_name': 'PSRI Hospital', 'city': 'New Delhi', 'contact': '1142521000'},
            {'username': 'blk_hospital', 'hospital_name': 'BLK Super Speciality Hospital', 'city': 'New Delhi', 'contact': '1130403040'},
            {'username': 'dharamshila', 'hospital_name': 'Dharamshila Narayana Superspeciality Hospital', 'city': 'New Delhi', 'contact': '1143066200'},
            {'username': 'holy_family', 'hospital_name': 'Holy Family Hospital', 'city': 'New Delhi', 'contact': '1126692901'},
            {'username': 'st_stephens', 'hospital_name': 'St. Stephens Hospital', 'city': 'New Delhi', 'contact': '1125951000'},
            
            # Noida Hospitals
            {'username': 'fortis_noida', 'hospital_name': 'Fortis Hospital Noida', 'city': 'Noida', 'contact': '1206713000'},
            {'username': 'max_noida', 'hospital_name': 'Max Multi Speciality Hospital Noida', 'city': 'Noida', 'contact': '1206629000'},
            {'username': 'apollo_noida', 'hospital_name': 'Apollo Hospital Noida', 'city': 'Noida', 'contact': '1206140000'},
            {'username': 'jaypee_noida', 'hospital_name': 'Jaypee Hospital', 'city': 'Noida', 'contact': '1206900000'},
            {'username': 'kailash_noida', 'hospital_name': 'Kailash Hospital Noida', 'city': 'Noida', 'contact': '1206900000'},
            {'username': 'yatharth_noida', 'hospital_name': 'Yatharth Hospital', 'city': 'Noida', 'contact': '1206900000'},
            {'username': 'sharda_noida', 'hospital_name': 'Sharda Hospital', 'city': 'Greater Noida', 'contact': '1206900000'},
            {'username': 'felix_noida', 'hospital_name': 'Felix Hospital', 'city': 'Noida', 'contact': '1206900000'},
            {'username': 'metro_noida', 'hospital_name': 'Metro Hospital Noida', 'city': 'Noida', 'contact': '1206900000'},
            {'username': 'cloudnine_noida', 'hospital_name': 'Cloudnine Hospital', 'city': 'Noida', 'contact': '1206900000'},
            
            # Faridabad Hospitals
            {'username': 'fortis_faridabad', 'hospital_name': 'Fortis Hospital Faridabad', 'city': 'Faridabad', 'contact': '1294289999'},
            {'username': 'asian_faridabad', 'hospital_name': 'Asian Hospital', 'city': 'Faridabad', 'contact': '1294289999'},
            {'username': 'metro_faridabad', 'hospital_name': 'Metro Hospital Faridabad', 'city': 'Faridabad', 'contact': '1294289999'},
            {'username': 'mamc_faridabad', 'hospital_name': 'MAMC Hospital', 'city': 'Faridabad', 'contact': '1294289999'},
            {'username': 'sarvodaya_faridabad', 'hospital_name': 'Sarvodaya Hospital', 'city': 'Faridabad', 'contact': '1294289999'},
            
            # More Gurgaon Hospitals
            {'username': 'park_hospital', 'hospital_name': 'Park Hospital', 'city': 'Gurgaon', 'contact': '1244251000'},
            {'username': 'w_pratiksha', 'hospital_name': 'W Pratiksha Hospital', 'city': 'Gurgaon', 'contact': '1244251000'},
            {'username': 'cdi_gurgaon', 'hospital_name': 'Centre for Digestive Diseases', 'city': 'Gurgaon', 'contact': '1244251000'},
            {'username': 'signature_gurgaon', 'hospital_name': 'Signature Hospital', 'city': 'Gurgaon', 'contact': '1244251000'},
            {'username': 'mayom_gurgaon', 'hospital_name': 'Mayom Hospital', 'city': 'Gurgaon', 'contact': '1244251000'},
            
            # Additional Delhi Hospitals
            {'username': 'aakash_delhi', 'hospital_name': 'Aakash Healthcare', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'venkateshwar_delhi', 'hospital_name': 'Venkateshwar Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'pushpawati_delhi', 'hospital_name': 'Pushpawati Singhania Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'jaipur_golden', 'hospital_name': 'Jaipur Golden Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'rockland_delhi', 'hospital_name': 'Rockland Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'primus_delhi', 'hospital_name': 'Primus Super Speciality Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'indian_spinal', 'hospital_name': 'Indian Spinal Injuries Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'national_heart', 'hospital_name': 'National Heart Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'delhi_heart', 'hospital_name': 'Delhi Heart & Lung Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'cygnus_delhi', 'hospital_name': 'Cygnus Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Eye & Specialty Hospitals
            {'username': 'aiims_eye', 'hospital_name': 'AIIMS Eye Centre', 'city': 'New Delhi', 'contact': '1126588500'},
            {'username': 'centre_sight', 'hospital_name': 'Centre for Sight', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'sharp_sight', 'hospital_name': 'Sharp Sight Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'drishti_eye', 'hospital_name': 'Drishti Eye Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'shroff_eye', 'hospital_name': 'Shroff Eye Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Cancer Hospitals
            {'username': 'rajiv_gandhi_cancer', 'hospital_name': 'Rajiv Gandhi Cancer Institute', 'city': 'New Delhi', 'contact': '1147022222'},
            {'username': 'action_cancer', 'hospital_name': 'Action Cancer Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'max_cancer', 'hospital_name': 'Max Cancer Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'fortis_cancer', 'hospital_name': 'Fortis Cancer Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Maternity Hospitals
            {'username': 'cloudnine_delhi', 'hospital_name': 'Cloudnine Hospital Delhi', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'motherhood_delhi', 'hospital_name': 'Motherhood Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'sitaram_bhartia', 'hospital_name': 'Sitaram Bhartia Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'max_smart', 'hospital_name': 'Max Smart Super Speciality Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Orthopedic Hospitals
            {'username': 'bone_joint', 'hospital_name': 'Bone & Joint Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'delhi_ortho', 'hospital_name': 'Delhi Orthopedic Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'indian_ortho', 'hospital_name': 'Indian Orthopedic Research Group', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Mental Health Hospitals
            {'username': 'ihbas_delhi', 'hospital_name': 'Institute of Human Behaviour & Allied Sciences', 'city': 'New Delhi', 'contact': '1122829000'},
            {'username': 'vimhans_delhi', 'hospital_name': 'Vimhans Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'tulsi_das', 'hospital_name': 'Tulsi Das Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Kidney & Urology Hospitals
            {'username': 'kidney_care', 'hospital_name': 'Kidney Care Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'delhi_urology', 'hospital_name': 'Delhi Urology Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'nephro_plus', 'hospital_name': 'NephroPlus Dialysis Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Cardiac Hospitals
            {'username': 'national_cardiac', 'hospital_name': 'National Cardiac Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'heart_care', 'hospital_name': 'Heart Care Foundation', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'cardiac_care', 'hospital_name': 'Cardiac Care Associates', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Gastro Hospitals
            {'username': 'gastro_liver', 'hospital_name': 'Gastro Liver Care', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'delhi_gastro', 'hospital_name': 'Delhi Gastroenterology Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Neuro Hospitals
            {'username': 'neuro_delhi', 'hospital_name': 'Delhi Neuroscience Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'brain_spine', 'hospital_name': 'Brain & Spine Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Pulmonology Hospitals
            {'username': 'chest_clinic', 'hospital_name': 'Chest Clinic Delhi', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'lung_care', 'hospital_name': 'Lung Care Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Skin & Cosmetic
            {'username': 'skin_care', 'hospital_name': 'Skin Care Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'derma_delhi', 'hospital_name': 'Delhi Dermatology Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # ENT Hospitals
            {'username': 'ent_delhi', 'hospital_name': 'Delhi ENT Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'hearing_care', 'hospital_name': 'Hearing Care Centre', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Dental Hospitals
            {'username': 'dental_delhi', 'hospital_name': 'Delhi Dental Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'smile_care', 'hospital_name': 'Smile Care Dental', 'city': 'New Delhi', 'contact': '1142777000'},
            
            # Additional Multi-specialty
            {'username': 'care_hospital', 'hospital_name': 'Care Hospital Delhi', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'star_hospital', 'hospital_name': 'Star Hospital Delhi', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'life_care', 'hospital_name': 'Life Care Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'health_plus', 'hospital_name': 'Health Plus Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'metro_heart', 'hospital_name': 'Metro Heart Institute', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'sunrise_hospital', 'hospital_name': 'Sunrise Hospital', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'city_hospital', 'hospital_name': 'City Hospital Delhi', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'prime_hospital', 'hospital_name': 'Prime Hospital Delhi', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'global_hospital', 'hospital_name': 'Global Hospital Delhi', 'city': 'New Delhi', 'contact': '1142777000'},
            {'username': 'elite_hospital', 'hospital_name': 'Elite Hospital Delhi', 'city': 'New Delhi', 'contact': '1142777000'}
        ]

        count = 0
        for hospital_data in hospitals:
            if not User.objects.filter(username=hospital_data['username']).exists():
                user = User()
                user.username = hospital_data['username']
                user.set_password('hospital123')
                user.email = f"admin@{hospital_data['username']}.com"
                user.first_name = hospital_data['hospital_name']
                user.hospital_name = hospital_data['hospital_name']
                user.city = hospital_data['city']
                user.province = 'Delhi'
                user.country = 'India'
                user.contact_number = hospital_data['contact']
                user.is_staff = True
                user.save()
                count += 1
                self.stdout.write(f"Added: {hospital_data['hospital_name']}")

        self.stdout.write(self.style.SUCCESS(f'Successfully added {count} hospitals from Delhi/NCR'))