from flask import request
from flask import current_app as app
from .models import Report
from .utils import ResponseObj
import json



@app.route('/survey/report', methods=['GET'])
def select_report():
    """
    Select the report list.
    :return: report list
    :exception: pymysql exception
    """
    page_no = request.args.get('pageNo', default=1, type=int)
    page_size = request.args.get('pageSize', default=10, type=int)
    try:
        response = ResponseObj(None, 200, u'请求成功')
    except Exception as exc:
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, indent=4, sort_keys=True, default=str),
                              mimetype='app/json')


@app.route('/survey/report/<id>', methods=['GET'])
def select_report_detail(id):
    """
    Select the report detail.
    :param id: report id
    :return: report detail
    :exception: pymysql exception
    """
    try:
        report_json = Report.query.get(id)
        response = ResponseObj(report_json, 200, u'请求成功')
    except Exception as exc:
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, indent=4, sort_keys=True, default=str),
                              mimetype='app/json')


@app.route('/about/contact', methods=['POST'])
def submit_contact():
    """
    Submit the contact info.
    :return: http status
    """
    json = request.get_json(force=True)
    name = json['name']
    mail = json['mail']
    content = json['content']
    try:
        response = ResponseObj(None, 200, u'请求成功')
    except Exception as exc:
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, indent=4, sort_keys=True, default=str),
                              mimetype='app/json')


@app.route('/about/project', methods=['POST'])
def submit_project():
    """
    Submit the project info.
    :return: http status
    """
    json = request.get_json(force=True)
    name = json['name']
    website = json['website']
    doc_addr = json['doc_addr']
    contact = json['contact']
    github = json['github']
    mail = json['mail']
    remarks = json['remarks']
    attachment = json['attachment']
    try:
        response = ResponseObj(None, 200, u'请求成功')
    except Exception as exc:
        response = ResponseObj(None, 500, u'服务器内部错误')
    return app.response_class(response=json.dumps(response.__dict__, indent=4, sort_keys=True, default=str),
                              mimetype='app/json')
