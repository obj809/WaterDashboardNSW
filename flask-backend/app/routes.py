# flask-backend/app/routes.py

from flask import Blueprint, jsonify, request
from .models import Dam, DamResource, LatestData
from datetime import datetime, timedelta
import subprocess
import json

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return 'Sydney Dam Monitoring'

@main.route('/latestdata/<string:dam_id>', methods=['GET'])
def get_latest_data(dam_id):
    data = LatestData.query.filter_by(dam_id=dam_id).first()
    if not data:
        return jsonify({'error': 'Dam not found'}), 404

    latitude = float(data.dam.latitude)
    longitude = float(data.dam.longitude)

    response = {
        'dam_id': data.dam_id,
        'dam_name': data.dam_name,
        'date': data.date.isoformat(),
        'storage_volume': float(data.storage_volume),
        'percentage_full': float(data.percentage_full),
        'storage_inflow': float(data.storage_inflow),
        'storage_release': float(data.storage_release),
        'latitude': latitude,
        'longitude': longitude
    }
    return jsonify(response)

@main.route('/damresources/<string:dam_id>', methods=['GET'])
def get_dam_resources(dam_id):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    resources = DamResource.query.filter(
        DamResource.dam_id == dam_id,
        DamResource.date >= start_date,
        DamResource.date <= end_date
    ).order_by(DamResource.date).all()

    response = [{
        'date': resource.date.isoformat(),
        'percentage_full': float(resource.percentage_full),
        'storage_inflow': float(resource.storage_inflow),
        'storage_release': float(resource.storage_release)
    } for resource in resources]

    return jsonify(response)

@main.route('/damsdata/<string:group_name>', methods=['GET'])
def get_dams_data(group_name):
    dam_groups = {
        'sydney_dams': ['212232', '212220', '212211', '212205', '213210', '213240', '212212', '215235'],
        'popular_dams': ['212243', '212232', '212220', '212211', '212205', '213210', '215212', '213240'],
        'large_dams': ['212243', '410102', '412010', '418035', '410131', '421078', '210097', '419080'],
        'small_dams': ['219033', '215235', '215212', '42510037', '219027', '203042', '210102', '412107'],
        'greatest_released': ['410102', '410131', '421078', '418035', '210117', '210097', '419041', '412010'],
    }

    if group_name not in dam_groups:
        return jsonify({'error': 'Group not found'}), 404

    dam_ids = dam_groups[group_name]
    data = LatestData.query.filter(LatestData.dam_id.in_(dam_ids)).all()

    response = [{
        'dam_id': d.dam_id,
        'dam_name': d.dam_name,
        'date': d.date.isoformat(),
        'storage_volume': float(d.storage_volume),
        'percentage_full': float(d.percentage_full),
        'storage_inflow': float(d.storage_inflow),
        'storage_release': float(d.storage_release),
        'latitude': float(d.dam.latitude),
        'longitude': float(d.dam.longitude)
    } for d in data]

    return jsonify(response)

@main.route('/damnames', methods=['GET'])
def get_dam_names():
    dams = Dam.query.with_entities(Dam.dam_name).all()
    dam_names = [dam.dam_name for dam in dams]
    return jsonify(dam_names)

@main.route('/damdata', methods=['GET'])
def get_dam_data_by_name():
    dam_name = request.args.get('dam_name')
    data = LatestData.query.filter_by(dam_name=dam_name).first()
    if not data:
        return jsonify({'error': 'Dam not found'}), 404

    latitude = float(data.dam.latitude)
    longitude = float(data.dam.longitude)

    response = {
        'dam_id': data.dam_id,
        'dam_name': data.dam_name,
        'date': data.date.isoformat(),
        'storage_volume': float(data.storage_volume),
        'percentage_full': float(data.percentage_full),
        'storage_inflow': float(data.storage_inflow),
        'storage_release': float(data.storage_release),
        'latitude': latitude,
        'longitude': longitude
    }
    return jsonify(response)

def run_pyspark_analysis(dam_id=None):
    try:
        command = ['python3', '/Users/softdev/Desktop/SydneyDamMonitoringDevelopment/flask-backend/app/pyspark_analysis.py']
        if dam_id:
            command.append(dam_id)
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            raise Exception(f"PySpark script failed with error: {stderr.decode('utf-8')}")
        
        stdout_str = stdout.decode('utf-8').strip()
        stderr_str = stderr.decode('utf-8').strip()
        
        print("PySpark stdout:", stdout_str)
        print("PySpark stderr:", stderr_str)
        
        if not stdout_str:
            raise Exception("No output from PySpark script")

        json_lines = [line for line in stdout_str.splitlines() if line.startswith("{") and line.endswith("}")]
        if not json_lines:
            raise Exception("No JSON output from PySpark script")
        
        result = json.loads(json_lines[0])
        return result
    except Exception as e:
        print(f"Error running PySpark script: {e}")
        raise

@main.route('/average_percentage_full/12_months', methods=['GET'])
def average_percentage_full_12_months():
    try:
        averages = run_pyspark_analysis()
        return jsonify({"avg_percentage_full_12_months": averages["avg_percentage_full_12_months"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/average_percentage_full/5_years', methods=['GET'])
def average_percentage_full_5_years():
    try:
        averages = run_pyspark_analysis()
        return jsonify({"avg_percentage_full_5_years": averages["avg_percentage_full_5_years"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/average_percentage_full/20_years', methods=['GET'])
def average_percentage_full_20_years():
    try:
        averages = run_pyspark_analysis()
        return jsonify({"avg_percentage_full_20_years": averages["avg_percentage_full_20_years"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/average_percentage_full/<string:dam_id>/12_months', methods=['GET'])
def average_percentage_full_12_months_dam(dam_id):
    try:
        averages = run_pyspark_analysis(dam_id)
        return jsonify({"avg_percentage_full_12_months": averages["avg_percentage_full_12_months"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/average_percentage_full/<string:dam_id>/5_years', methods=['GET'])
def average_percentage_full_5_years_dam(dam_id):
    try:
        averages = run_pyspark_analysis(dam_id)
        return jsonify({"avg_percentage_full_5_years": averages["avg_percentage_full_5_years"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/average_percentage_full/<string:dam_id>/20_years', methods=['GET'])
def average_percentage_full_20_years_dam(dam_id):
    try:
        averages = run_pyspark_analysis(dam_id)
        return jsonify({"avg_percentage_full_20_years": averages["avg_percentage_full_20_years"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/damdata/12_months/<string:group_name>', methods=['GET'])
def get_dam_data_12_months(group_name):
    dam_groups = {
        'sydney_dams': ['212232', '212220', '212211', '212205', '213210', '213240', '212212', '215235'],
        'popular_dams': ['212243', '212232', '212220', '212211', '212205', '213210', '215212', '213240'],
        'large_dams': ['212243', '410102', '412010', '418035', '410131', '421078', '210097', '419080'],
        'small_dams': ['219033', '215235', '215212', '42510037', '219027', '203042', '210102', '412107'],
        'greatest_released': ['410102', '410131', '421078', '418035', '210117', '210097', '419041', '412010'],
    }

    if group_name not in dam_groups:
        return jsonify({'error': 'Group not found'}), 404

    dam_ids = dam_groups[group_name]
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    data = DamResource.query.join(Dam).filter(
        DamResource.dam_id.in_(dam_ids),
        DamResource.date >= start_date,
        DamResource.date <= end_date
    ).order_by(DamResource.date).all()

    response = [{
        'dam_id': d.dam_id,
        'dam_name': d.dam.dam_name,
        'date': d.date.isoformat(),
        'percentage_full': float(d.percentage_full)
    } for d in data]

    return jsonify(response)
