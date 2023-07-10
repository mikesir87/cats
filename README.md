NOTE: This project is effectively a fork of a mini-lab of [DockerCon 2016 US Orchestration Lab](https://github.com/docker/dcus-hol-2016/tree/master/docker-orchestration).  Just pulled it into a standalone project for easier building.

## Running the App

```
docker container run --rm -tip 5000:5000 mikesir87/cats:1.0
OR
docker container run --rm -tip 5000:5000 mikesir87/cats:2.0
```

## Building

Since this project has three different demo versions and uses the same Dockerfile for each, the build command is a _little_ more complicated.

```
docker build -f Dockerfile -t mikesir87/cats:1.0 ./v1
```

To perform multi-architecture builds:

```
docker buildx build --push --platform linux/arm/v7,linux/arm64/v8,linux/amd64 --tag mikesir87/cats:1.0 -f Dockerfile ./v1
```
