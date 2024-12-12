generate-nginx-certs:
		openssl req -x509 -newkey rsa:2048 -nodes -keyout nginx/certs/domain.key -out nginx/certs/domain.crt -days 365 -subj "/CN=nginx.local"

start-nginx:
	docker compose -f nginx/compose.yaml up --remove-orphans --force-recreate --build

down-nginx:
	docker compose -f nginx/compose.yaml down --rmi all --volumes