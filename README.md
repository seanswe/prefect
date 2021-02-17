Setup
===========

Set prefect backend to cloud:

```
prefect backend cloud
````

Get login token from prefect cloud and then login. I stored mine in an environment variable:

```
prefect auth login -t $PREFECT_AUTH_LOGIN

```

Create runner token with:

```
prefect auth create-token -n my-runner-token -s RUNNER
```

Launch prefect Docker agent with:

```
prefect agent docker start
```