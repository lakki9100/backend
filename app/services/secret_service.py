from google.cloud import secretmanager
import google.auth

class SecretService:
    def __init__(self):
        self.credentials, self.project_id = google.auth.default()
        self.client = secretmanager.SecretManagerServiceClient(credentials=self.credentials)

    def get(self, secret_id: str, default: str = None) -> str:
        try:
            name = f"projects/{self.project_id}/secrets/{secret_id}/versions/latest"
            response = self.client.access_secret_version(name=name)
            return response.payload.data.decode("utf-8")
        except Exception as e:
            print(f"[SecretService] Failed to fetch {secret_id}: {e}")
            return default
