FROM python:3.10-slim-bullseye

WORKDIR /app

# 🔥 FIX: force HTTPS for Debian repos
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    mpg123 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["bash"]