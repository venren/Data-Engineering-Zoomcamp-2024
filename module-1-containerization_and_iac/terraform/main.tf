terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  project = "zoomcamp-terraform-intro"
  region  = "europe-west2-c"
}

resource "google_storage_bucket" "terraform-venren-demo-bucket" {
  name          = "terraform-venren-demo-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}