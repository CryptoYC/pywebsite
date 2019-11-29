from flask import request
from flask import current_app as app
from werkzeug.utils import secure_filename
from . import db
from .models import Report, Contact, Project
from .utils import ResponseObj
from .data import *
import json
import os


@app.route('/survey/report/<id>', methods=['GET'])
def select_report_detail(id):
    """
    Select the report detail.
    :param id: report id
    :return: report detail
    :exception: pymysql exception
    """
    try:
        report = Report.query.get(id)
        report_json = report.to_json()
        response = ResponseObj(report_json, 200, u'请求成功')
    except Exception as exc:
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, default=str), mimetype='application/json')


@app.route('/survey/data/<id>', methods=['GET'])
def select_data_detail(id):
    switch = {'1': chaininfo, '2': troytrade, '3': sncrating}
    try:
        js = switch[id]()
        response = ResponseObj(js, 200, u'请求成功')
    except BaseException as exc:
        print(exc)
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, default=str), mimetype='application/json')


@app.route('/about/contact', methods=['POST'])
def submit_contact():
    """
    Submit the contact info.
    :return: http status
    """
    try:
        form = request.form
        name = form['name']
        mail = form['mail']
        content = form['content']
        contact = Contact(name=name, mail=mail, content=content)
        db.session.add(contact)
        db.session.commit()
        response = ResponseObj(None, 200, u'请求成功')
    except Exception as exc:
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, default=str), mimetype='application/json')


@app.route('/survey/project', methods=['POST'])
def submit_project():
    """
    Submit the project info.
    :return: http status
    """
    try:
        form = request.form
        files = request.files
        name = form['name']
        website = form['website']
        doc_addr = form['doc_addr']
        contact = form['contact']
        github = form['github']
        mail = form['mail']
        remark = form['remarks']
        attachment = files['attachment']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, r'''static\uploads''', secure_filename(attachment.filename))
        attachment.save(upload_path)
        project = Project(name=name, website=website, doc_addr=doc_addr, contact=contact, github=github, mail=mail,
                          remark=remark, attachment=attachment.filename)
        db.session.add(project)
        db.session.commit()
        response = ResponseObj(None, 200, u'请求成功')
    except Exception as exc:
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, default=str), mimetype='application/json')
