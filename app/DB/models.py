# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group

models.options.DEFAULT_NAMES +=('verbose_genus',) # m = maskulin, f = feminin, n = neutrum(default)

class sys_importdatei(models.Model):
	zu_app			= models.CharField(max_length=255																		, verbose_name="Zu App")
	zu_tabelle		= models.CharField(max_length=255																		, verbose_name="Zu Tabelle")
	zu_pk			= models.IntegerField(																					  verbose_name="Zu PK")
	datei			= models.CharField(max_length=255																		, verbose_name="Datei")
	zeit			= models.DateTimeField(																					  verbose_name="Zeit")
	erledigt		= models.BooleanField(									   default=False								, verbose_name="Erledigt")
	def __str__(self):
		return '{}->{}->{} <- {} ({}) Erledigt: {}"'.format(self.zu_app,self.zu_tabelle,self.zu_pk,self.datei,self.zeit,self.erledigt)
	class Meta:
		verbose_name = "Importdatei"
		verbose_name_plural = "Importdateien"
		ordering = ('zu_app','zu_tabelle','zu_pk',)
		default_permissions = ()
		permissions = (('dateien', 'Dateien anzeigen. (Zugriffsrechte für Verzeichnisse beachten!)'),('csvimport', 'CSV-Dateien importieren'),)

class user_verzeichniss(models.Model):
	user				= models.ForeignKey(User											, on_delete=models.CASCADE		, verbose_name="ID zu User")
	Verzeichniss		= models.CharField(max_length=511,			blank=True, null=True									, verbose_name="Verzeichniss")
	RECHTE_DATEN = (
		(0, 'Keine'),
		(1, 'Anzeigen'),
		(2, 'Anzeigen | Dateien hochladen und löschen'),
		(3, 'Anzeigen | Dateien hochladen und löschen | Unterverzeichnisse erstellen und löschen'),
		(4, 'Anzeigen | Dateien hochladen und löschen | Unterverzeichnisse erstellen und rekursiv löschen'),
	)
	Rechte				= models.PositiveIntegerField(				blank=True, null=True, choices=RECHTE_DATEN				, verbose_name="Rechte")
	def __str__(self):
		return "{} -> {} ({})".format(self.user,self.Verzeichniss,self.Rechte)
	class Meta:
		verbose_name = "Zugriffsrecht für Verzeichniss"
		verbose_name_plural = "Zugriffsrechte für Verzeichnisse"
		verbose_genus = "n"
		ordering = ('user',)
		default_permissions = ()

class group_verzeichniss(models.Model):
	group				= models.ForeignKey(Group											, on_delete=models.CASCADE		, verbose_name="ID zu Gruppe")
	Verzeichniss		= models.CharField(max_length=511,			blank=True, null=True									, verbose_name="Verzeichniss")
	RECHTE_DATEN_G = (
		(0, 'Keine'),
		(1, 'Anzeigen'),
		(2, 'Anzeigen | Dateien hochladen und löschen'),
		(3, 'Anzeigen | Dateien hochladen und löschen | Unterverzeichnisse erstellen und löschen'),
		(4, 'Anzeigen | Dateien hochladen und löschen | Unterverzeichnisse erstellen und rekursiv löschen'),
	)
	Rechte				= models.PositiveIntegerField(				blank=True, null=True, choices=RECHTE_DATEN_G			, verbose_name="Rechte")
	def __str__(self):
		return "{} -> {} ({})".format(self.group,self.Verzeichniss,self.Rechte)
	class Meta:
		verbose_name = "Zugriffsrecht für Verzeichniss"
		verbose_name_plural = "Zugriffsrechte für Verzeichnisse"
		verbose_genus = "n"
		ordering = ('group',)
		default_permissions = ()

class sys_filesystem(models.Model):
	def __str__(self):
		return '{}'.format(self.pk)
	class Meta:
		verbose_name = "Dateisystem"
		verbose_name_plural = "Dateisysteme"
		default_permissions = ()

class sys_user_addon(models.Model):
	user = models.OneToOneField(User														, on_delete=models.CASCADE		, verbose_name="ID zu User")
	last_visit = models.DateTimeField(																						  verbose_name="Zeit")
