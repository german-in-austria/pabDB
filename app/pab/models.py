from django.db import models
from django.core.validators import MaxValueValidator

models.options.DEFAULT_NAMES +=('verbose_genus',) # m = maskulin, f = feminin, n = neutrum(default)

class tbl_informanten(models.Model):
	inf_sigle		= models.CharField(max_length=255, unique=True													, verbose_name="Informant/in Sigle")
	nachname		= models.CharField(max_length=255																, verbose_name="Nachname")
	vorname			= models.CharField(max_length=255																, verbose_name="Vorname")
	geb_datum		= models.DateField(					blank=True, null=True										, verbose_name="Geburtsdatum")
	alter			= models.IntegerField(				blank=True, null=True										, verbose_name="Alter")
	weiblich		= models.NullBooleanField(default=None, blank=True, null=True									, verbose_name="Weiblich")
	strasse_hausnr	= models.CharField(max_length=255,	blank=True, null=True										, verbose_name="Strasse mit Nr.")
	ort				= models.ForeignKey('tbl_orte',		blank=True, null=True, on_delete=models.SET_NULL			, verbose_name="Ort")
	plz				= models.CharField(max_length=6,	blank=True, null=True										, verbose_name="PLZ")
	mail1			= models.CharField(max_length=45,	blank=True, null=True										, verbose_name="E-Mail 1")
	mail2			= models.CharField(max_length=45,	blank=True, null=True										, verbose_name="E-Mail 2")
	festnetz1		= models.CharField(max_length=45,	blank=True, null=True										, verbose_name="Festnetz 1")
	festnetz2		= models.CharField(max_length=45,	blank=True, null=True										, verbose_name="Festnetz 2")
	mobil1			= models.CharField(max_length=45,	blank=True, null=True										, verbose_name="Mobil 1")
	mobil2			= models.CharField(max_length=45,	blank=True, null=True										, verbose_name="Mobil 2")
	def __str__(self):
		return self.inf_sigle
	class Meta:
		verbose_name = "Informant"
		verbose_name_plural = "Informanten"
		verbose_genus = "m"
		ordering = ('nachname',)
		default_permissions = ()
		permissions = (('edit', 'Kann PersonenDB in DB bearbeiten'),('pab_maskView', 'Kann Maskeneingaben einsehen'),('pab_maskAdd', 'Kann Maskeneingaben hinzufügen'),('pab_maskEdit', 'Kann Maskeneingaben bearbeiten'),)

class tbl_orte(models.Model):
	ort_namekurz	= models.CharField(max_length=255,	blank=True, null=True										, verbose_name="Ortsname (kurz)")
	ort_namelang	= models.CharField(max_length=255																, verbose_name="Ortsname (lang)")
	lat				= models.CharField(max_length=255,	blank=True, null=True										, verbose_name="lat")
	lon				= models.CharField(max_length=255,	blank=True, null=True										, verbose_name="lon")
	osm_id			= models.BigIntegerField(			blank=True, null=True										, verbose_name="OSM-ID")
	osm_type		= models.CharField(max_length=255,	blank=True, null=True										, verbose_name="OSM-Type")
	def __str__(self):
		return self.ort_namelang
	class Meta:
		verbose_name = "Ort"
		verbose_name_plural = "Orte"
		verbose_genus = "m"
		ordering = ('ort_namelang',)
		default_permissions = ()
		permissions = (('edit', 'Kann Orte in DB bearbeiten'),('pab_maskView', 'Kann Maskeneingaben einsehen'),('pab_maskAdd', 'Kann Maskeneingaben hinzufügen'),('pab_maskEdit', 'Kann Maskeneingaben bearbeiten'),)

class tbl_antworten(models.Model):
	gesp_in_dateiname	=models.CharField(max_length=45																, verbose_name="Gespeichert in Dateiname")
	von_inf				= models.ForeignKey('tbl_informanten'						, on_delete=models.CASCADE		, verbose_name="von Person")
	ist_satz			= models.ForeignKey('tbl_saetze',	blank=True, null=True	, on_delete=models.SET_NULL		, verbose_name="Ist Satz")
	reihung				= models.IntegerField(				blank=True, null=True									, verbose_name="Reihung")
	silbenstr_abweich	= models.BooleanField(default=False															, verbose_name="Silbenstruktur abweichend")
	anzahl_praenukl		= models.IntegerField(				blank=True, null=True									, verbose_name="Anzahl Pränukl")
	akzenttyp			=models.CharField(max_length=45,	blank=True, null=True									, verbose_name="Akzenttyp")
	downstep			= models.BooleanField(				blank=True, null=False									, verbose_name="Downstep")
	Kommentar			= models.CharField(max_length=511,	blank=True, null=True									, verbose_name="Kommentar")
	def __str__(self):
		return "{}, {}".format(self.von_Inf,self.ist_satz)
	class Meta:
		verbose_name = "Antwort"
		verbose_name_plural = "Antworten"
		verbose_genus = "f"
		ordering = ('reihung',)
		default_permissions = ()
		permissions = (('edit', 'Kann Antworten in DB bearbeiten'),('auswertung', 'Kann Antworten auswerten'),('pab_maskView', 'Kann Maskeneingaben einsehen'),('pab_maskAdd', 'Kann Maskeneingaben hinzufuegen'),('pab_maskEdit', 'Kann Maskeneingaben bearbeiten'),)

class tbl_saetze(models.Model):
	satz_nr				= models.CharField(max_length=45,			blank=False, null=False							, verbose_name="Satznummer")
	transkript			= models.CharField(max_length=511,			blank=True, null=True							, verbose_name="Transkript")
	standardorth		= models.CharField(max_length=511,			blank=True, null=True							, verbose_name="Standardorth")
	kommentar			= models.CharField(max_length=511,			blank=True, null=True							, verbose_name="Kommentar")
	silbenstruktur_erw	= models.CharField(max_length=45,			blank=True, null=True							, verbose_name="erwartete Silbenstruktur")
	laenge_nukl_wort	= models.IntegerField(						blank=True, null=True							, verbose_name="Länge des Wortknukleus")
	laenge_nukl_fuss	= models.IntegerField(						blank=True, null=True							, verbose_name="Länge des Fußknukleus")
	abstand_phrasengrenze=models.IntegerField(						blank=True, null=True							, verbose_name="Abstand Phrasengrenze")
	fokus				= models.IntegerField(						blank=True, null=True							, verbose_name="Fokus")
	konsonant1			= models.CharField(max_length=45,			blank=True, null=True							, verbose_name="1. Konsonant")
	vokal				= models.CharField(max_length=45,			blank=True, null=True							, verbose_name="Vokal")
	konsonant2			= models.CharField(max_length=45,			blank=True, null=True							, verbose_name="2. Konsonant")
	def __str__(self):
		return "{}, {} ({})".format(self.satz_nr,self.standardorth,self.Kommentar)
	class Meta:
		verbose_name = "Satz"
		verbose_name_plural = "Sätze"
		verbose_genus = "m"
		ordering = ('satz_nr',)
		default_permissions = ()

class tbl_messung(models.Model):
	zu_antwort			= models.ForeignKey('tbl_antworten',		blank=False, null=False 						, verbose_name="zu Antwort")
	ist_kategorie		= models.ForeignKey('tbl_kategorien',		blank=False, null=False 						, verbose_name="ist kategorie")
	wert				= models.IntegerField(						blank=False, null=False							, verbose_name="Messwert")
	def __str__(self):
		return "{}, {}".format(self.ist_kategorie,self.zu_antwort)
	class Meta:
		verbose_name = "Messung"
		verbose_name_plural = "Messungen"
		verbose_genus = "f"
		ordering = ('ist_kategorie',)

class tbl_kategorien(models.Model):
	bezeichnung			= models.CharField(max_length=45,			blank=False, null=False							, verbose_name="Bezeichnung")
	einheit				= models.CharField(max_length=45,			blank=False, null=False							, verbose_name="Einheit")
	def __str__(self):
		return "{}".format(self.bezeichnung)
	class Meta:
		verbose_name = "Kategorie"
		verbose_name_plural = "Kategorien"
		verbose_genus = "f"
		ordering = ('bezeichnung',)
