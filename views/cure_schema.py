# -*- coding: utf-8 -*-
from collections import OrderedDict

from .. import app, db
from ..forms import CureSchemaForm, SearchForm
from ..models import CureSchema, Dosage
from flask import render_template, flash, redirect, request, url_for


@app.route('/cure_schema<id>', methods=['GET', 'POST'])
def cure_schema_edit(id):
    cure = CureSchema.query.get(id)
    form = CureSchemaForm(obj=cure)
    if request.method == 'POST':
        form = CureSchemaForm(request.form, obj=cure)
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(cure)
                db.session.add(cure)
                db.session.commit()
                flash(u"Сохранено")
    ctx = dict(form=form, title=cure.title)
    return render_template('cure_schema/edit.html', **ctx)


@app.route('/cure_schemaadd', methods=['GET', 'POST'])
def cure_schema_add():
    medicine = CureSchema()
    form = CureSchemaForm(request.form, instance=medicine)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(medicine)
                db.session.add(medicine)
                db.session.commit()
                flash(u"Сохранено")
                return redirect(url_for('cure_schema_list'))
    return render_template('cure_schema/edit.html',
                           title=u'Схемы лечения',
                           form=form)


@app.route('/cure_schema', methods=['GET', 'POST'])
@app.route('/cure_schema/<int:page>', methods=['GET', 'POST'])
def cure_schema_list(page=1, query=None):
    cure_schemas = CureSchema.query
    if query:
        cure_schemas = cure_schemas.filter(CureSchema.title.ilike(u"{0}%".format(query)))
    cure_schemas = cure_schemas.order_by('title').paginate(page, 10, False)
    ctx = dict(cure_schemas=cure_schemas, title=u'Схемы лечения', search_form=SearchForm())
    return render_template('cure_schema/list.html', **ctx)
