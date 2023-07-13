import base64
import requests

class GithubFileFetcher():
	def __init__(self, auth_token: str=None):
		self.auth_token = auth_token

	def fetch(self, owner: str, repo: str, file_path: str):
		r = requests.get(
			f'https://api.github.com/repos/{owner}/{repo}/contents/{file_path}',
			headers={'Authorization': f'Bearer {self.auth_token}'} if self.auth_token else {}
		)
		assert r.status_code == 200, f'github api error todo: {r.text}'
		return base64.b64decode(r.json()['content']).decode()

if __name__ == '__main__':
	import os
	f = GithubFileFetcher(auth_token=os.getenv("GITHUB_AUTH_TOKEN"))
	f.fetch('shaojiajun314', 'web-template', 'README.md')
		