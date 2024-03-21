from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/tesla/callback")
async def callback_get():
    return {"message": f"ok"}


@app.post("/tesla/callback")
async def callback_post():
    return {"message": f"ok"}


@app.get("/.well-known")
async def well_known():
    return 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC3DvbvEHpgKDETj7zTgo5p4yBhoYUrQjwfLOWTaWd9C8YaPtngyFFLNyVgS1X9f+hhbDxOv0MHlEa+uyg39/tdJLNtfQmix++yb7Sxw7/8uZmhF2+uOEpNx7SUCRx59H1rE8jDS4UnhTTWItRUMw9vCBORqvM4OqY4+2Ujpd886h166YwMGDAJ20hPAapsSjNgEXGBqmY9+DhgSrYOx3cNgpDrZRUIu3id1mvwS9Q7v+QV9aPefJ9/HaUg/sQQ4D6MnKlcXcd8wmXQdS0loD1q0c4T4g0F4TI9Ji7weDD+HnrAEyUAd11d+lrcajfWLLLEFuCYoSZhaUvmpZ0oBlR/azg+RQTp3AExVmZJGPfnTcKYKxrRUvYdn7NXGdJ8Cvj0lq0nRdTUIIEcncF4OCcEtiiLdl4naSnOshH4Qf32OqdgnJDjJt8V0SjTVgVVgCPqrb7v+w/gI7a1kGJvPvYOs9ydxgmlszvJoASSImGQ2idqPdPsL1ALYgJkSVXGlzE= generated-by-azure'


@app.get("/.well-known/appspecific/com.tesla.3p.public-key.pem")
async def well_known():
    return 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC3DvbvEHpgKDETj7zTgo5p4yBhoYUrQjwfLOWTaWd9C8YaPtngyFFLNyVgS1X9f+hhbDxOv0MHlEa+uyg39/tdJLNtfQmix++yb7Sxw7/8uZmhF2+uOEpNx7SUCRx59H1rE8jDS4UnhTTWItRUMw9vCBORqvM4OqY4+2Ujpd886h166YwMGDAJ20hPAapsSjNgEXGBqmY9+DhgSrYOx3cNgpDrZRUIu3id1mvwS9Q7v+QV9aPefJ9/HaUg/sQQ4D6MnKlcXcd8wmXQdS0loD1q0c4T4g0F4TI9Ji7weDD+HnrAEyUAd11d+lrcajfWLLLEFuCYoSZhaUvmpZ0oBlR/azg+RQTp3AExVmZJGPfnTcKYKxrRUvYdn7NXGdJ8Cvj0lq0nRdTUIIEcncF4OCcEtiiLdl4naSnOshH4Qf32OqdgnJDjJt8V0SjTVgVVgCPqrb7v+w/gI7a1kGJvPvYOs9ydxgmlszvJoASSImGQ2idqPdPsL1ALYgJkSVXGlzE= generated-by-azure'
