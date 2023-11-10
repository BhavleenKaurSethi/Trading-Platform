provider "google" {
  project = "trading-platform-404001"
  region  = "australia-southeast1"
}

resource "google_cloud_run_service" "default" {
  name     = "my-react-app"
  location = "australia-southeast1"

  template {
    spec {
      containers {
        image = "gcr.io/trading-platform-404001/frontend"

        resources {
          limits = {
            memory = "1Gi"  
          }
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Make sure the Cloud Run service is publicly accessible
resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.default.location
  project     = google_cloud_run_service.default.project
  service     = google_cloud_run_service.default.name

  policy_data = <<EOF
{
  "bindings": [
    {
      "role": "roles/run.invoker",
      "members": [
        "allUsers"
      ]
    }
  ]
}
EOF
}
