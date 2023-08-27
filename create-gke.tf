terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.81.0"
    }
  }
}

provider "google" {
  credentials = file("/home/ishansharma1320/csci-5409-s23-f8c4f33c3999.json")
  project     = "csci-5409-s23"
  region      = "us-central1"
}
resource "google_container_cluster" "primary" {
  name     = "k8s-assignment-gke"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count = 1
}
resource "google_container_node_pool" "k8s-node-pool" {
  name       = "k8s-assignment-node-pool"
  cluster    = google_container_cluster.primary.name
  location   = google_container_cluster.primary.location
  node_count = 1

  node_config {
    machine_type = "e2-micro"
    disk_size_gb = 10
    disk_type    = "pd-standard"
    image_type   = "COS_CONTAINERD"
  }
}
output "cluster_endpoint" {
  value = google_container_cluster.primary.endpoint
}