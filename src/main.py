from fastapi import FastAPI, Request
from tinydb import TinyDB, Query

from sys import path
path.append('../utils')
from utils import validated_field


app = FastAPI()
db = TinyDB("test_db.json")
FormTemplate = Query()


@app.post('/get_form')
async def get_form(request: Request):
    data = await request.form()
    field_names = list(data.keys())
    field_values = list(data.values())

    form_templates = db.search(FormTemplate.name.exists())
    for template in form_templates:
        template_fields = list(template.keys())
        template_fields.remove('name')
        if set(template_fields).issubset(set(field_names)):
            for i, template_field in enumerate(template_fields):
                if template_field != validated_field(field_values[i]):
                    break
            else:
                return template['name']

    result = {}
    for i in range(len(field_names)):
        result[field_names[i]] = validated_field(field_values[i])
    return result
