import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import time
from datetime import datetime

# Convert string to datetime type


def to_datetime(time):
    try:
        # first, try to convert with second
        return datetime.strptime(time, '%m/%d/%Y %H:%M:%S')
    except:
        pass

    # fallback, try to convert without second
    return datetime.strptime(time, '%m/%d/%Y %H:%M')

# Convert DynamicRecord to convert datetime column
# Separate year, month for partition column


def convertDateTime(rec):
    rec['starttime'] = to_datetime(rec['starttime'])
    rec['stoptime'] = to_datetime(rec['stoptime'])
    rec['year'] = rec['starttime'].year
    rec['month'] = rec['starttime'].month
    return rec


# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Create a Glue context
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Data Source
source_dyf = glueContext.create_dynamic_frame.from_catalog(
    database='junsjangdb', table_name="raw_tripdata")

# Convert mapping
mapping_applied_dyf = source_dyf.applyMapping(mappings=[
    ('tripduration', 'int', 'tripduration', 'int'),
    ('starttime', 'string', 'starttime', 'string'),
    ('stoptime', 'string', 'stoptime', 'string'),
    ('bikeid', 'int', 'bikeid', 'int'),
    ('usertype', 'string', 'usertype', 'string'),
    ('gender', 'string', 'gender', 'tinyint'),
    ('start station id', 'int', 'start_station_id', 'int'),
    ('start station name', 'string', 'start_station_name', 'string'),
    ('start station latitude', 'double', 'start_station_latitude', 'double'),
    ('start station longitude', 'double', 'start_station_longitude', 'double'),
    ('end station id', 'int', 'end_station_id', 'int'),
    ('end station name', 'string', 'end_station_name', 'string'),
    ('end station latitude', 'double', 'end_station_latitude', 'double'),
    ('end station longitude', 'double', 'end_station_longitude', 'double'),
    ('birth year', 'string', 'birth_year', 'smallint')
], transformation_ctx='Convert column type and name')

# Convert to datetime format column
datetime_dyf = mapping_applied_dyf.map(
    convertDateTime, transformation_ctx='Convert time string to datetime')

# Write to transformed location
glueContext.write_dynamic_frame.from_options(
    frame=datetime_dyf,
    connection_type='s3',
    connection_options={
        'path': 's3://junsjang-citibike-ap-northeast-1-013610758945/transformed/tripdata',
        'partitionKeys': ['year', 'month']
    },
    format='glueparquet'
)

# Execute job
job.commit()
