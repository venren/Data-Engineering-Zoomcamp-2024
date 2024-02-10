terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.15.0"
    }
  }
}

provider "google" {
 credentials = "./keys/creds.json"
  project = "my-project-id"
  region  = "us-central1"
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