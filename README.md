# Soar Platform API

Requirements:
- python >= 3.10

## Getting started with docker

#### Build docker image:
```bash
docker build -t soar:dev .
```

#### Start container:
Note: .env.example - this file required, it contains zoom's S2S OAuth2 api credentials. You can name it anyhow you want. Or you can pass ENV variables into container with `-e FOO='bar' -e MOO='baz'` options. 
```Bash
docker run --env-file ./.env.example -p 127.0.0.1:5000:5000 soar:dev
```