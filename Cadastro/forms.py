# -*- coding: utf-8 -*-

from django.db import models

from django.forms import ModelForm
from models import *

class ContatoForm(ModelForm):
        class Meta:
          model = contato

