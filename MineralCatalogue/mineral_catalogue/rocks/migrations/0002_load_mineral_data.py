import json
from django.db import migrations



def load_minerals(apps, schema_editor):
   # fix <app_name> with your app name.
   Mineral = apps.get_model('rocks', 'Mineral')


# Now open your minerals.json file, read it in.
# Iterate over each item in the list of dicts
# use Mineral.objects.create() to create each mineral.
   with open('rocks/minerals.json', encoding='utf-8') as f:
       # This will make sure it doesnt matter which Operating System the person is running Python on it will
       # still read the `json` file using the same encoding type every time, which its best to use `utf-8`.
       # This is a subtle detail that can cause problems on some operating systems and not others.
       rocks = json.load(f)
       for thing in rocks:
           Mineral.objects.create(name=thing.get('name', ''),
                                  image_filename=thing.get('image_filename', ''),
                                  image_caption=thing.get('image_caption', ''),
                                  category=thing.get('category', ''),
                                  formula=thing.get('formula', ''),
                                  strunz_classification=thing.get('strunz_classification', ''),
                                  color=thing.get('color', ''),
                                  crystal_system=thing.get('crystal_system', ''),
                                  unit_cell=thing.get('unit_cell', ''),
                                  crystal_symmetry=thing.get('crystal_symmetry',''),
                                  cleavage=thing.get('cleavage', ''),
                                  mohs_scale_hardness=thing.get('mohs_scale_hardness', ''),
                                  luster=thing.get('luster', ''),
                                  streak=thing.get('streak', ''),
                                  diaphaneity=thing.get('diaphaneity', ''),
                                  optical_properties=thing.get('optical_properties', ''),
                                  refractive_index=thing.get('refractive_index',''),
                                  crystal_habit=thing.get('crystal_habit',''),
                                  specific_gravity=thing.get('specific_gravity',''))


class Migration(migrations.Migration):
   dependencies = [
       # fix this <app_name> with your app name
       ('rocks', '0001_initial'),
   ]

   operations = [
       migrations.RunPython(load_minerals, reverse_code=migrations.RunPython.noop),
   ]