from dataclasses import dataclass


# Data Ingestion Artifact Entity
@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 

# Data Validation Artifact Entity
@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str

# Data Transformation Artifact Entity
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

# Model Metrics Artifact Entity
@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float

# Model Trainer Artifact Entity
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact

# Model Evaluation Artifact Entity
@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str

# Model Pusher Artifact Entity
@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str