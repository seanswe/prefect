Setup
------------

This setup assumes the Docker agent will be run on a VM or locally. There is no need to install any flow dependencies on the machine. Dependencies are specified in the flow when using a Docker agent and the image is built from the Prefect base image when the flow is registered. 

Set prefect backend to cloud:

```sh
prefect backend cloud
````

Get login token from prefect cloud and then login. 

```sh
prefect auth login -t $PREFECT_AUTH_LOGIN
```

Create runner token with:

```sh
prefect auth create-token -n my-runner-token -s RUNNER
```

Launch prefect Docker agent with:

```sh
prefect agent docker start
```