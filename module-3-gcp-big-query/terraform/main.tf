terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.15.0"
    }
  }
}

provider "google" {
  project = "zoomcamp-terraform-intro"
  region  = "US"
}

resource "google_storage_bucket" "venren-zoomcamp-module3-hw" {
  name          = var.gcp_storage_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "hw3_dataset" {
  dataset_id                  = "hw3_dataset"
  friendly_name               = "hw3_dataset"
  description                 = "Home work 3 datasets"
  location                    = "US"
  default_table_expiration_ms = 3600000

  labels = {
    env = "default"
  }
}