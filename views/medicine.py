# -*- coding: utf-8 -*-
from collections import OrderedDict

from .. import app, db
from ..forms import MedicineForm, SearchForm
from ..models import Medicine, Dosage
from flask import render_template, flash, redirect, request, url_for


@app.route('/medicine<id>', methods=['GET', 'POST'])
def medicine_edit(id):
    medicine = Medicine.query.get(id)
    form = MedicineForm(obj=medicine)
    if request.method == 'POST':
        form = MedicineForm(request.form, obj=medicine)
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(medicine)
                db.session.add(medicine)
                db.session.commit()
                flash(u"Сохранено")
    ctx = dict(form=form, title=medicine.title)
    return render_template('medicine/edit.html', **ctx)


@app.route('/medicineadd', methods=['GET', 'POST'])
def medicine_add():
    medicine = Medicine()
    form = MedicineForm(request.form, instance=medicine)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(medicine)
                db.session.add(medicine)
                db.session.commit()
                flash(u"Сохранено")
                return redirect(url_for('medicine_list'))
    return render_template('medicine/edit.html',
                           title=u'Лекарства',
                           form=form)


def get_fast_links(query):
    result = OrderedDict()
    for obj in query:
        if obj.title[:1] not in result:
            result[obj.title[:1]] = url_for('medicine_list', query=obj.title[:1])
    return result


@app.route('/medicine', methods=['GET', 'POST'])
@app.route('/medicine/<int:page>', methods=['GET', 'POST'])
@app.route('/medicine/<query>/', methods=['GET', 'POST'])
@app.route('/medicine/<query>/<int:page>', methods=['GET', 'POST'])
def medicine_list(page=1, query=None):
    medicines = Medicine.query
    if query:
        medicines = medicines.filter(Medicine.title.ilike(u"{0}%".format(query)))
    medicines = medicines.order_by('title').paginate(page, 10, False)
    ctx = dict(medicines=medicines, title=u'Препараты', search_form=SearchForm())
    ctx['fast_links'] = get_fast_links(Medicine.query.order_by('title'))
    return render_template('medicine/list.html', **ctx)


@app.route('/medicine_search', methods=['POST'])
def medicine_search():
    form = SearchForm(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('medicine_list'))
    return redirect(url_for('medicine_list', query=form.search.data))




