Setup
------------

Set prefect backend to cloud:

```sh
prefect backend cloud
````

Get login token from prefect cloud and then login. I stored mine in an environment variable:

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